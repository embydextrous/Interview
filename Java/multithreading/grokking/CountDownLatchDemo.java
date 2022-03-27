package multithreading.grokking;

import java.util.concurrent.CountDownLatch;

public class CountDownLatchDemo {
    public static void main(String[] args) throws InterruptedException {
        CountDownLatch latch = new CountDownLatch(3);
        for (int i = 0; i < 3; i++) {
            Thread t = new Thread(new Worker(latch, i * 1000));
            t.start();
        }
        latch.await();
        System.out.println("Printed after latch is down to zero.");
    }
}

class Worker implements Runnable {
    private final CountDownLatch countDownLatch;
    private final long sleepTime;

    public Worker(CountDownLatch countDownLatch, long sleepTime) {
        this.countDownLatch = countDownLatch;
        this.sleepTime = sleepTime;
    }

    @Override
    public void run() {
        try {
            System.out.println(Thread.currentThread().getName() + " : " + sleepTime);
            Thread.sleep(sleepTime);
        } catch(InterruptedException E) {
            
        } finally {
            countDownLatch.countDown();
        } 
    }
}
