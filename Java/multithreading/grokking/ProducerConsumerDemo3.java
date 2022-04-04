package multithreading.grokking;

import java.util.LinkedList;
import java.util.Queue;
import java.util.Random;
import java.util.concurrent.locks.Condition;
import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReentrantLock;

public class ProducerConsumerDemo3 {
    public static void main(String[] args) throws InterruptedException {
        Processor3 processor = new Processor3(10);
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

class Processor3 implements Processor {
    private final Queue<Integer> list = new LinkedList<>();
    private final int capacity;
    private Lock lock = new ReentrantLock();
    private Condition condition = lock.newCondition();

    Processor3(int capacity) {
        this.capacity = capacity;
    }

    @Override
    public void produce() throws InterruptedException {
        Random random = new Random();

        while (true) {
            lock.lock();
            while (list.size() == capacity) {
                condition.await();
            }
            try {
                int val = random.nextInt(100);
                list.add(val);
                System.out.println("Adding " + val + ". " + "List is: " + list);
                condition.signalAll();
            } finally {
                lock.unlock();
            }
            Thread.sleep(random.nextInt(100));
        }
    }

    @Override
    public void consume() throws InterruptedException {
        Random random = new Random();

        while (true) {
            lock.lock();
            while (list.size() == 0) {
                condition.await();
            }
            try {
                int val = list.remove();
                System.out.println("Removing " + val + ". " + "List is: " + list);
                condition.signalAll();
            } finally {
                lock.unlock();
            }
            Thread.sleep(random.nextInt(200));
        }
    }
}
