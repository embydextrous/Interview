package multithreading;

public class SimpleCountdownLatchDemo {
    public static void main(String[] args) throws InterruptedException {
        SimpleCountdownLatch latch = new SimpleCountdownLatch(3);

        new Thread(() -> {
            try {
                Thread.sleep(3000);
            } catch (InterruptedException e) {
                // TODO Auto-generated catch block
                e.printStackTrace();
            }
            latch.countDown();
        }).start();

        new Thread(() -> {
            try {
                Thread.sleep(1000);
            } catch (InterruptedException e) {
                // TODO Auto-generated catch block
                e.printStackTrace();
            }
            latch.countDown();
        }).start();

        new Thread(() -> {
            try {
                Thread.sleep(5000);
            } catch (InterruptedException e) {
                // TODO Auto-generated catch block
                e.printStackTrace();
            }
            latch.countDown();
        }).start();

        System.out.println("Waiting for latch...");
        latch.await();
        System.out.println("Latch down.");
    }
}

class SimpleCountdownLatch {
    private int count;
    
    public SimpleCountdownLatch(int count) {
        if (count < 0) {
            throw new IllegalArgumentException("Count cannot be less than zero.");
        }
        this.count = count;
    }

    public synchronized void await() throws InterruptedException {
        while(count > 0) {
            wait();
        }
    }

    public synchronized void countDown() {
        count--;
        if (count == 0) {
            notifyAll();
        }
    }
}
