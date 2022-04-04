package multithreading.problems.barrier;

public class SafeBarrier implements Barrier {
    private int count = 0;
    private final int barrierPoint;
    private int released = 0;

    SafeBarrier(int barrierPoint) {
        this.barrierPoint = barrierPoint;
    }

    @Override
    public synchronized void await() throws InterruptedException {
        while(count == barrierPoint) {
            wait();
        }
        count++;
        if (count == barrierPoint) {
            notifyAll();
            released = barrierPoint;
        } else {
            while(count < barrierPoint) {
                wait();
            }
        }
        released--;
        if (released == 0) {
            count = 0;
            notifyAll();
        }
    }
}
