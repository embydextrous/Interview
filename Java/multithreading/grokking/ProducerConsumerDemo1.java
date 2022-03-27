package multithreading.grokking;

import java.util.Random;
import java.util.concurrent.ArrayBlockingQueue;
import java.util.concurrent.BlockingQueue;

public class ProducerConsumerDemo1 {
    public static void main(String[] args) throws InterruptedException {
        Processor1 producerConsumer = new Processor1();
        Thread t1 = new Thread(new Runnable() {
            @Override
            public void run() {
                try {
                    producerConsumer.produce();
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
                    producerConsumer.consume();
                } catch (InterruptedException e) {
                    // TODO Auto-generated catch block
                    e.printStackTrace();
                }
            }
        });
        t1.start();
        t2.start();
        t1.join();
        t1.join();
    }
}

class Processor1 implements Processor {
    private BlockingQueue<Integer> queue = new ArrayBlockingQueue<>(10);

    public void produce() throws InterruptedException {
        Random random = new Random();
        while (true) {
            queue.put(random.nextInt(10));
        }
    }

    public void consume() throws InterruptedException {
        Random random = new Random();

        while (true) {
            Thread.sleep(100);
            System.out.println(queue);
            if (random.nextInt(10) == 0) {
                int value = queue.remove();
                System.out.println(value);
            }
        }
    }
}
