package multithreading.grokking;

public class VolatileDemo {
    public static void main(String[] args) throws InterruptedException {
        Worker1 worker = new Worker1();
        Thread t1 = new Thread(new Runnable() {
            @Override
            public void run() {
                worker.doWork();
            }
        });
        t1.start();
        Thread t2 = new Thread(new Runnable() {
            @Override
            public void run() {
                try {
                    Thread.sleep(3000);
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
                worker.setTerminated(true);
            }
        });
        t2.start();
        t1.join();
        t2.join();
    }
}

class Worker1 {
    private volatile boolean terminated;

    public void doWork() {
        while(!terminated) {
            System.out.println("Worker is running...");
            try {
                Thread.sleep(400);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }

    public void setTerminated(boolean terminated) {
        this.terminated = terminated;
    }
}
