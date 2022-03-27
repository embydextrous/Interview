package multithreading.grokking;

public class ThreadLocalDemo {
    public static void main(String[] args) throws InterruptedException {
        Counter counter = new Counter();
        Thread[] tasks = new Thread[100];

        for (int i = 0; i < 100; i++) {
            Thread t = new Thread(() -> {
                for (int j = 0; j < 100; j++)
                    counter.increment();
                System.out.println("Counter value is: " + counter.counter.get());
            });
            tasks[i] = t;
            t.start();
        }

        for (int i = 0; i < 100; i++) {
            tasks[i].join();
        }

        System.out.println("The value of counter is: " + counter.counter.get());
    }
}

class Counter {
    ThreadLocal<Integer> counter = ThreadLocal.withInitial(() -> 0);

    public Counter() {
        this.counter.set(10);
    }

    public void increment() {
        counter.set(counter.get() + 1);
    }
}
