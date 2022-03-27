package multithreading.grokking;

import java.util.Random;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.Semaphore;
import java.util.concurrent.TimeUnit;

public class SemaphoreDemo {
    public static void main(String[] args) throws InterruptedException {
        Connection connection = Connection.getInstance();
        Random random = new Random();

        ExecutorService executor = Executors.newCachedThreadPool();
        for (int i = 0; i < 200; i++) {
            executor.submit(new Runnable() {
                @Override
                public void run() {
                    try {
                        Thread.sleep(random.nextInt(500));
                    } catch(InterruptedException e) {
                        e.printStackTrace();
                    }
                    connection.connect();
                }
            });
        }
        executor.awaitTermination(1, TimeUnit.DAYS);
        executor.shutdown();
    }
}


class Connection {
    private static final Connection INSTANCE = new Connection();
    private int connections = 0;
    private Random random = new Random();
    private Semaphore sem = new Semaphore(10);

    private Connection() {}

    public static Connection getInstance() {
        return INSTANCE;
    }

    public void connect() {
        try {
            sem.acquire();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        try {
            synchronized(this) {
                connections++;
                System.out.println("Number of connections: " + connections);
            }

            try {
                Thread.sleep(random.nextInt(1000));
            } catch (InterruptedException e) {
                // TODO Auto-generated catch block
                e.printStackTrace();
            }

            synchronized(this) {
                connections--;
                System.out.println("Number of connections: " + connections);
            }
        } finally {
            sem.release();
        }
    }
}
