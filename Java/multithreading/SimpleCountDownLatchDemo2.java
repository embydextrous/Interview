package multithreading;

import java.util.concurrent.Semaphore;

public class SimpleCountDownLatchDemo2 {
    public static void main(String[] args) throws InterruptedException {
        SimpleCountdownLatch2 latch = new SimpleCountdownLatch2(3);

        new Thread(() -> {
            try {
                Thread.sleep(3000);
            } catch (InterruptedException e) {
                // TODO Auto-generated catch block
                e.printStackTrace();
            }
            latch.countDown();
        }).start();

        new Thread(() -> {
            try {
                Thread.sleep(1000);
            } catch (InterruptedException e) {
                // TODO Auto-generated catch block
                e.printStackTrace();
            }
            latch.countDown();
        }).start();

        new Thread(() -> {
            try {
                Thread.sleep(5000);
            } catch (InterruptedException e) {
                // TODO Auto-generated catch block
                e.printStackTrace();
            }
            latch.countDown();
        }).start();

        System.out.println("Waiting for latch...");
        latch.await();
        System.out.println("Latch down.");
    }
}

class SimpleCountdownLatch2 {
    private final Semaphore sem;

    public SimpleCountdownLatch2(int count) {
        if (count < 0) {
            throw new IllegalArgumentException("Count should be greater than or equal to zero");
        }
        this.sem = new Semaphore(-1 * count + 1);
    }

    public void await() throws InterruptedException {
        sem.acquire();
        sem.release();
    }

    public void countDown() {
        sem.release();
    }
}
