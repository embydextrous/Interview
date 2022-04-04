package multithreading.problems.countingsemaphore;

public class CountingSemaphoreDemo {
    public static void main(String[] args) throws InterruptedException {
        CountingSemaphore cs = new CountingSemaphore(2);

        Thread t1 = new Thread(() -> {
            for(int i = 0; i < 10; i++) {
                try {
                    cs.acquire();
                    System.out.println("Ping " + i);
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }
        });

        Thread t2 = new Thread(() -> {
            for(int i = 0; i < 10; i++) {
                try {
                    cs.release();
                    System.out.println("Pong " + i);
                } catch (InterruptedException e) {
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
