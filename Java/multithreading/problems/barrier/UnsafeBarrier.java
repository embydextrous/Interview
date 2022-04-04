package multithreading.problems.barrier;

public class UnsafeBarrier implements Barrier {
    private int count = 0;
    private final int barrierPoint;

    UnsafeBarrier(int barrierPoint) {
        this.barrierPoint = barrierPoint;
    }

    @Override
    public synchronized void await() throws InterruptedException {
        count++;
        if (count == barrierPoint) {
            notifyAll();
            count = 0;
        } else {
            // 1. Doesn't guard against spurious wakeups breaking Barrier contract
            wait();
        }
    }
}
