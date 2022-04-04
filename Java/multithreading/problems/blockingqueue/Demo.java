package multithreading.problems.blockingqueue;

import java.util.concurrent.ThreadLocalRandom;

public class Demo {
    public static void main(String args[]) throws Exception {
        final BlockingQueue<Integer> q = new ArrayBlockingQueue<>(10);
        ThreadLocalRandom random = ThreadLocalRandom.current();
        Thread t1 = new Thread(() -> {
            try {
                while (true) {
                    int i = random.nextInt(100);
                    q.enqueue(i);
                    System.out.println("Enqueued " + i);
                    Thread.sleep(50);
                }
            } catch (InterruptedException ie) {

            } 
        });

        Thread t2 = new Thread(new Runnable() {

            @Override
            public void run() {
                try {
                    while (true) {
                        System.out.println("Thread 2 dequeued " + q.dequeue());
                        Thread.sleep(100);
                    }
                } catch (InterruptedException ie) {
    
                } 
            }
        });

        Thread t3 = new Thread(new Runnable() {
            @Override
            public void run() {
                try {
                    while (true) {
                        System.out.println("Thread 3 dequeued " + q.dequeue());
                        Thread.sleep(100);
                    }
                } catch (InterruptedException ie) {
    
                } 
            }
        });

        t1.start();
        Thread.sleep(4000);
        t2.start();

        t2.join();

        t3.start();
        t1.join();
        t3.join();
    }
}
