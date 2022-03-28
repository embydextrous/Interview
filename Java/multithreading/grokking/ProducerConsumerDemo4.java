package multithreading.grokking;

import java.util.LinkedList;
import java.util.Queue;
import java.util.Random;
import java.util.concurrent.Semaphore;

public class ProducerConsumerDemo4 {
    public static void main(String[] args) throws InterruptedException {
        Processor4 processor = new Processor4(10);
        Thread t1 = new Thread(new Runnable() {
            @Override
            public void run() {
                try {
                    processor.produce();
                } catch (InterruptedException e) {
                    // TODO Auto-generated catch block
                    e.printStackTrace();
                }
            }
        });
        Thread t2 = new Thread(new Runnable() {
            @Override
            public void run() {
                try {
                    processor.consume();
                } catch (InterruptedException e) {
                    // TODO Auto-generated catch block
                    e.printStackTrace();
                }
            }
        });
        t1.start();
        t2.start();
        t1.join();
        t2.join();
    }
}

class Processor4 implements Processor {
    private final Queue<Integer> list = new LinkedList<>();
    private final int capacity;
    private final Semaphore pSem;
    private final Semaphore cSem;
    
    Processor4(int capacity) {
        this.capacity = capacity;
        this.pSem = new Semaphore(10);
        this.cSem = new Semaphore(0);
    }

    @Override
    public void produce() throws InterruptedException {
        Random random = new Random();

        while (true) {
            try {
                pSem.acquire();
                synchronized(this) {
                    int val = random.nextInt(100);
                    list.add(val);
                    System.out.println("Adding " + val + ". " + "List is: " + list);
                }
                cSem.release();
                Thread.sleep(random.nextInt(100));
            } catch(Exception e) {
                pSem.release();
            }
        }
    }

    @Override
    public void consume() throws InterruptedException {
        Random random = new Random();

        while (true) {
            cSem.acquire();
            try {
                synchronized (this) {
                    int val = list.remove();
                    System.out.println("Removing " + val + ". " + "List is: " + list);
                }
                pSem.release();
                Thread.sleep(random.nextInt(400));
            } catch(Exception e) {
                cSem.release();
            }
        }
    }
}
