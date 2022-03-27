package multithreading.forkjoin;
import java.util.Arrays;
import java.util.Random;
import java.util.concurrent.ForkJoinPool;
import java.util.concurrent.RecursiveAction;

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
        parallelMergeSort.print();
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
        ForkJoinPool forkJoinPool = new ForkJoinPool(Runtime.getRuntime().availableProcessors());
        ParallelMergeSortTask parallelMergeSortTask = new ParallelMergeSortTask(nums, 0, nums.length - 1);
        forkJoinPool.submit(parallelMergeSortTask);
        parallelMergeSortTask.join();
    }
}

class ParallelMergeSortTask extends RecursiveAction {
    private int nums[];
    private int low;
    private int high;

    ParallelMergeSortTask(int[] nums, int low, int high) {
        this.nums = nums;
        this.low = low;
        this.high = high;
    }

    @Override
    protected void compute() {
        if (high - low < 1000000) {
            sort(low, high);
            return;
        }
        int mid = low + (high - low) / 2;
        ParallelMergeSortTask task1 = new ParallelMergeSortTask(nums, low, mid);
        ParallelMergeSortTask task2 = new ParallelMergeSortTask(nums, mid + 1, high);
        invokeAll(task1, task2);
        task1.join();
        task2.join();
    }

    private void sort(int low, int high) {
        if (low >= high) {
            return;
        }
        int mid = low + (high - low) / 2;
        sort(low, mid);
        sort(mid + 1, high);
        merge(low, mid, high);
    }

    private void merge(int low, int mid, int high) {
        int[] temp = Arrays.copyOfRange(nums, low, high + 1);
        int i = low;
        int j = mid + 1;
        int k = low;
        while (i <= mid && j <= high) {
            if (temp[i - low] <= temp[j - low]) {
                nums[k++] = temp[i++ - low];
            } else {
                nums[k++] = temp[j++ - low];
            }
        }
        while (i <= mid) {
            nums[k++] = temp[i++ - low];
            
        }
        while (j <= high) {
            nums[k++] = temp[j++ - low];
        }
    }
}