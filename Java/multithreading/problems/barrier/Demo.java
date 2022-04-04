package multithreading.problems.barrier;

public class Demo {
    public static void main(String[] args) throws InterruptedException {
        Barrier barrier = new SafeBarrier(3);

        Thread t1 = new Thread(() -> {
            while(true) {
                try {
                    System.out.println("Thread 1 waiting for barrier..");
                    barrier.await();
                    System.out.println("Thread 1 crossed the barrier..");
                } catch (InterruptedException e) {
                    // TODO Auto-generated catch block
                    e.printStackTrace();
                }
            }
        });

        Thread t2 = new Thread(() -> {
            while(true) {
                try {
                    Thread.sleep(500);
                    System.out.println("Thread 2 waiting for barrier..");
                    barrier.await();
                    System.out.println("Thread 2 crossed the barrier..");
                } catch (InterruptedException e) {
                    // TODO Auto-generated catch block
                    e.printStackTrace();
                }
            }
        });

        Thread t3 = new Thread(() -> {
            while(true) {
                try {
                    Thread.sleep(1000);
                    System.out.println("Thread 3 waiting for barrier..");
                    barrier.await();
                    System.out.println("Thread 3 crossed the barrier..");
                } catch (InterruptedException e) {
                    // TODO Auto-generated catch block
                    e.printStackTrace();
                }
            }
        });

        t1.start();
        t2.start();
        t3.start();
        t1.join();
        t2.join();
        t3.join();
    }
}
