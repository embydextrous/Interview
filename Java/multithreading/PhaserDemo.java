package multithreading;

import java.util.concurrent.Phaser;

public class PhaserDemo {
    public static void main(String[] args) throws InterruptedException{
        Phaser phaser = new Phaser();
        PhaserRunnable pr1 = new PhaserRunnable(1, phaser);
        PhaserRunnable pr2 = new PhaserRunnable(2, phaser);
        PhaserRunnable pr3 = new PhaserRunnable(3, phaser);
        Thread t1 = new Thread(pr1);
        Thread t2 = new Thread(pr2);
        Thread t3 = new Thread(pr3);

        t1.start();
        Thread.sleep(2000);
        t2.start();
        Thread.sleep(5000);
        t3.start();
        t1.join();
        t2.join();
        t3.join();
    }
}

class PhaserRunnable implements Runnable {
    private Phaser phaser;
    private int id;

    PhaserRunnable(int id, Phaser phaser) {
        this.id = id;
        this.phaser = phaser;
        phaser.register();
    }

    @Override
    public void run() {
        System.out.println("Thread" + id + " arrived at phaser.");
        phaser.arriveAndAwaitAdvance();
        try {
            Thread.sleep(id * 1000 * 3);
            System.out.println("Thread " + id + " wait completes..");
        } catch (InterruptedException e) {

        } finally {
            phaser.arriveAndDeregister();
        }
    }
}
