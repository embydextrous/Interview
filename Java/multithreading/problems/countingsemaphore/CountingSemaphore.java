package multithreading.problems.countingsemaphore;

public class CountingSemaphore {
    private final int MAX_PERMITS;
    private int usedPermits;

    public CountingSemaphore(int maxPermits) {
        this.MAX_PERMITS = maxPermits;
        this.usedPermits = 0;
    }

    public synchronized void acquire() throws InterruptedException {
        while(usedPermits == MAX_PERMITS) {
            wait();
        }
        usedPermits++;
        notify();
    }

    public synchronized void release() throws InterruptedException {
        while (usedPermits == 0) {
            wait();
        }
        usedPermits--;
        notify();
    }
}
