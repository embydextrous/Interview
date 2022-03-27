package multithreading.grokking;

import java.util.LinkedList;
import java.util.Queue;
import java.util.Random;

public class ProducerConsumerDemo2 {
    public static void main(String[] args) throws InterruptedException {
        Processor2 processor2 = new Processor2(10);
        Thread t1 = new Thread(new Runnable() {
            @Override
            public void run() {
                try {
                    processor2.produce();
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
                    processor2.consume();
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

class Processor2 implements Processor {
    private final Queue<Integer> list = new LinkedList<>();
    private final int capacity;

    Processor2(int capacity) {
        this.capacity = capacity;
    }

    @Override
    public void produce() throws InterruptedException {
        Random random = new Random();

        while (true) {
            synchronized(this) {
                while(list.size() == capacity) {
                    System.out.println("List is full!");
                    wait();
                }
                int val = random.nextInt(100);
                list.add(val);
                System.out.println("Adding " + val + ". " + "List is: " + list);
                notify();
            }
            Thread.sleep(random.nextInt(100));
        }
    }

    @Override
    public void consume() throws InterruptedException {
        Random random = new Random();

        while (true) {
            synchronized(this) {
                while(list.size() == 0) {
                    System.out.println("List is empty!");
                    wait();
                }
                int val = list.remove();
                System.out.println("Removing " + val + ". " + "List is: " + list);
                notify();
            }
            Thread.sleep(random.nextInt(200));
        }
    }
}
