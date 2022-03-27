package multithreading.parallel;
import java.util.Arrays;
import java.util.Random;
import java.util.concurrent.ExecutionException;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.Future;

public class MergeSortDemo {
    public static void main(String[] args) {
        int n = 100_000_000;
        Random random = new Random();
        int[] nums = new int[n];
        for(int i = 0; i < n; i++) {
            nums[i] = random.nextInt(1_000_000);
        }
        SerialMergeSort serialMergeSort = new SerialMergeSort(nums);
        serialMergeSort.sort();
        serialMergeSort.showBenchmark();

        nums = new int[n];
        for(int i = 0; i < n; i++) {
            nums[i] = random.nextInt(1_000_000);
        }
        ParallelMergeSort parallelMergeSort = new ParallelMergeSort(nums);
        parallelMergeSort.sort();
        parallelMergeSort.showBenchmark();
    }
}

interface MergeSort {
    enum Type {
        Serial, Parallel
    }
    public void sort();
}

abstract class MeasurableMergeSort implements MergeSort {
    private int[] nums;
    protected long timeTakenInMilliSeconds = 0;
    private Type type;

    public MeasurableMergeSort(int[] nums, Type type) {
        this.nums = nums;
        this.type = type;
    }

    public final void sort() {
        long start = System.currentTimeMillis();
        mergeSort(nums);
        long end = System.currentTimeMillis();
        timeTakenInMilliSeconds = end - start;
    }

    abstract void mergeSort(int[] a);

    protected final void showBenchmark() {
        System.out.println(type.name() + " MergeSort for " + nums.length + " items took " + timeTakenInMilliSeconds + "ms.");
    }

    protected final void print() {
        System.out.print("[");
        for (int i = 0; i < nums.length - 1; i++) {
            System.out.print(nums[i] + ", ");
        }
        System.out.print(nums[nums.length - 1]);
        System.out.println("]");
    }

    protected final void mergeSortInternal(int[] a) {
        if (a.length <= 1)
			return;
		int mid = a.length / 2;
		int[] left = Arrays.copyOfRange(a, 0, mid);
		int[] right = Arrays.copyOfRange(a, mid, a.length);
		mergeSortInternal(left);
		mergeSortInternal(right);
		merge(left, right, a);
    }
   
    protected final void merge(int[] left, int[] right, int[] a) {
		int i = 0;
		int j = 0;
		int k = 0;
		
		while (i < left.length && j < right.length) {
			if (left[i] < right[j]) {
				a[k++] = left[i++];
            }
			else {
				a[k++] = right[j++];
            }
		}

		while (i < left.length) {
			a[k++] = left[i++];
        }

		while (j < right.length) {
			a[k++] = right[j++];
        }
	}
}

class SerialMergeSort extends MeasurableMergeSort {
    public SerialMergeSort(int[] nums) {
        super(nums, Type.Serial);
    }

    @Override
    public void mergeSort(int[] nums) {
        mergeSortInternal(nums);
    }
}

class ParallelMergeSort extends MeasurableMergeSort {

    public ParallelMergeSort(int[] nums) {
        super(nums, Type.Parallel);
    }

    @Override
    public void mergeSort(int[] nums) {
        int numThreads = Runtime.getRuntime().availableProcessors() * 4;
        parallelMergeSort(nums, numThreads);
    }

    private void parallelMergeSort(int[] a, int numThreads) {
        if (numThreads == 1 || a.length < 1_000_000) {
            mergeSortInternal(a);
            return;
        }
        ExecutorService executor = Executors.newFixedThreadPool(2);
        int mid = a.length / 2;
        int[] left = Arrays.copyOfRange(a, 0, mid);
		int[] right = Arrays.copyOfRange(a, mid, a.length);
        Future<?> f1 = executor.submit(new Runnable() {
            @Override
            public void run() {
                parallelMergeSort(left, numThreads / 2);
            }
        });
        Future<?> f2 = executor.submit(new Runnable() {
            @Override
            public void run() {
                parallelMergeSort(right, numThreads / 2);
            }
        });
        try {
            f1.get();
            f2.get();
        } catch (InterruptedException|ExecutionException e) {
            
        } finally {
            executor.shutdown();
            merge(left, right, a);
        }
    }
}