package multithreading.forkjoin;

import java.util.Random;
import java.util.concurrent.ForkJoinPool;
import java.util.concurrent.RecursiveTask;

public class MaxDemo {

    public static void main(String[] args) {
        int n = 500_000_000;
        Random random = new Random();
        int[] nums = new int[n];
        for (int i = 0; i < n; i++) {
            nums[i] = random.nextInt(1_000_000);
        }

        FindMax findMax = new FindMax(nums);
        int max = findMax.serialMax();
        System.out.println("Serial max is: " + max);
        max = findMax.parallelMax();
        System.out.println("Parallel max is: " + max);
    }
    
    public static int getMax(int[] nums, int low, int high) {
        int max = Integer.MIN_VALUE;
        for (int i = low; i < high; i++) {
            if (nums[i] > max) {
                max = nums[i];
            }
        }
        return max;
    }
}

class FindMax {
    private final int[] nums;

    FindMax(int[] nums) {
        this.nums = nums;
    }

    int serialMax() {
        long start = System.nanoTime();
        int max = MaxDemo.getMax(nums, 0, nums.length);
        long end = System.nanoTime();
        System.out.println("Time to find max serially: " + (end - start) + "ns.");
        return max;
    }

    int parallelMax() {
        long start = System.nanoTime();
        ForkJoinPool forkJoinPool = new ForkJoinPool(Runtime.getRuntime().availableProcessors() * 2);
        ParallelMaxTask maxTask = new ParallelMaxTask(nums, 0, nums.length);
        forkJoinPool.submit(maxTask);
        int max = maxTask.join();
        long end = System.nanoTime();
        System.out.println("Time to find max in parallel: " + (end - start) + "ns.");
        return max;
    }
}

class ParallelMaxTask extends RecursiveTask<Integer> {
    private final int[] nums;
    private final int low;
    private final int high;

    ParallelMaxTask(int[] nums, int low, int high) {
        this.nums = nums;
        this.low = low;
        this.high = high;
    }

    @Override
    protected Integer compute() {
        if (high - low < 1000000) {
            return MaxDemo.getMax(nums, low, high);
        }
        int mid = low + (high - low) / 2;
        ParallelMaxTask task1 = new ParallelMaxTask(nums, low, mid);
        ParallelMaxTask task2 = new ParallelMaxTask(nums, mid, high);
        invokeAll(task1, task2);
        return Math.max(task1.join(), task2.join());
    }
}
