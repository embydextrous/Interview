package multithreading.problems.deferredcallback;

import java.util.PriorityQueue;
import java.util.concurrent.RejectedExecutionException;
import java.util.concurrent.TimeUnit;
import java.util.concurrent.locks.Condition;
import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReentrantLock;

public class DeferredCallbackExecutor {

    private PriorityQueue<Callback> queue = new PriorityQueue<>(
            (cb1, cb2) -> (int) (cb1.executionTime - cb2.executionTime));
    private Lock lock = new ReentrantLock();
    private Condition condition = lock.newCondition();
    private boolean isTerminated = false;

    public void start() throws InterruptedException {
        long sleepFor = 0;
        while (true) {
            lock.lock();
            try {
                while (!isTerminated && queue.isEmpty()) {
                    condition.await();
                } 
                if (isTerminated && queue.isEmpty()) {
                    break;
                }
                while (!queue.isEmpty()) {
                    sleepFor = findSleepDuration();
                    if (sleepFor <= 0) {
                        break;
                    }
                    condition.await(sleepFor, TimeUnit.MILLISECONDS);
                }
                Callback cb = queue.poll();
                System.out.println("Executed at " + System.currentTimeMillis() + ", required at " + cb.executionTime);
                cb.execute();
            } finally {
                lock.unlock();
            }
        }
    }

    public void shutdown() {
        lock.lock();
        try {
            this.isTerminated = true;
        } finally {
            lock.unlock();
        }
    }

    private long findSleepDuration() {
        return queue.peek().executionTime - System.currentTimeMillis();
    }

    // Method to run callback
    public void registerCallback(Callback callback) throws RejectedExecutionException {
        lock.lock();
        try {
            if (isTerminated) {
                throw new RejectedExecutionException("Cannot accept callback after termination.");
            }
            queue.add(callback);
            condition.signal();
        } finally {
            lock.unlock();
        }
    }

    public static class Callback {
        private long executionTime;
        private Runnable runnable;

        public Callback(Runnable runnable, long executeAfter) {
            this.runnable = runnable;
            this.executionTime = System.currentTimeMillis() + executeAfter;
        }

        public long getExecutionTime() {
            return executionTime;
        }

        public void execute() {
            runnable.run();
        }
    }
}
