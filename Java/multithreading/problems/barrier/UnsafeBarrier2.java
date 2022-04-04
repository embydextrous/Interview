package multithreading.problems.barrier;

public class UnsafeBarrier2 implements Barrier {
    private int count = 0;
    private final int barrierPoint;
    private int released = 0;

    UnsafeBarrier2(int barrierPoint) {
        this.barrierPoint = barrierPoint;
    }

    @Override
    public synchronized void await() throws InterruptedException {
        // Deadlock Here, Suppose [t1, t2, t3] and t3 calls await again and scheduled before t1 and t2 exits. 
        // In that case count becomes 4. And so t1 and t2 won't be notified.
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
        }
    }
}
