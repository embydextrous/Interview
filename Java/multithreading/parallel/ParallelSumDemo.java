package multithreading.parallel;

import java.util.LinkedList;
import java.util.List;
import java.util.Random;
import java.util.concurrent.Callable;
import java.util.concurrent.ExecutionException;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.Future;
import java.util.concurrent.TimeUnit;

public class ParallelSumDemo {
    public static void main(String[] args) {
        int n = 500_000_000;
        Random random = new Random();
        int[] nums = new int[n];
        for (int i = 0; i < n; i++) {
            nums[i] = random.nextInt(1_000_000);
        }
        SerialSum serialSum = new SerialSum(nums);
        serialSum.sum();
        serialSum.showBenchmark();

        ParallelSum parallelSum = new ParallelSum(nums);
        parallelSum.sum();
        parallelSum.showBenchmark();
    }
}

interface Sum {
    enum Type {
        Serial, Parallel
    }

    public long sum();
}

abstract class MeasurableSum implements Sum {
    protected final int[] nums;
    protected long timeTakenInMilliSeconds = 0;
    private Type type;
    private long sum;

    MeasurableSum(int[] nums, Type type) {
        this.nums = nums;
        this.type = type;
    }

    protected final void showBenchmark() {
        System.out.println(type + " Sum is: " + sum);
        System.out.println(
                type.name() + " Summation for " + nums.length + " items took " + timeTakenInMilliSeconds + "ns.");
    }

    @Override
    public final long sum() {
        long start = System.nanoTime();
        sum = sumInternal(0, nums.length);
        long end = System.nanoTime();
        timeTakenInMilliSeconds = end - start;
        return sum;
    }

    abstract long sumInternal(int from, int to);

    protected final long serialSum(int from, int to) {
        long sum = 0;
        for (int i = from; i < to; i++) {
            sum += nums[i];
        }
        return sum;
    }
}

class SerialSum extends MeasurableSum {

    SerialSum(int[] nums) {
        super(nums, Type.Serial);
    }

    @Override
    protected long sumInternal(int from, int to) {
        return serialSum(from, to);
    }
}

class ParallelSum extends MeasurableSum {
    private int numCPU = Runtime.getRuntime().availableProcessors() * 2;
    private ExecutorService executor = Executors.newFixedThreadPool(numCPU);

    ParallelSum(int[] nums) {
        super(nums, Type.Parallel);
    }

    @Override
    long sumInternal(int from, int to) {
        List<Future<Long>> futures = new LinkedList<>();
        int size = nums.length / numCPU;
        long sum = 0;
        for (int i = 0; i < numCPU; i++) {
            final int k = i;
            int end = i == numCPU - 1 ? nums.length : (k+1) * size;
            Future<Long> future = executor.submit(new Callable<Long>() {
                @Override
                public Long call() throws Exception {
                    return serialSum(size * k, end);
                }
            });
            futures.add(future);
        }
        executor.shutdown();
        try {
            executor.awaitTermination(1, TimeUnit.MINUTES);
        } catch (InterruptedException e) {
            return 0;
        } 
        for (Future<Long> future : futures) {
            try {
                sum += future.get();
            } catch (InterruptedException e) {
                return 0;
            } catch (ExecutionException e) {
                return 0;
            }
        }
        return sum;
    }
}
