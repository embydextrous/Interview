package multithreading.problems.rwlock;

public class Demo {
    public static void main(String[] args) throws InterruptedException {
        ReadWriteLock rwLock = new ReadWriteLock();
        Thread w1 = new Thread(() -> {
            while (true) {
                try {
                    System.out.println("Attempting to acquire write lock in w1: " + System.currentTimeMillis());
                    rwLock.acquireWriteLock();
                    System.out.println("write lock acquired w1: " + System.currentTimeMillis());
                    Thread.sleep(300);
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
                System.out.println("Releasing write lock in w1: " + System.currentTimeMillis());
                rwLock.releaseWriteLock();
            }
        });

        Thread w2 = new Thread(() -> {
            try {
                System.out.println("Attempting to acquire write lock in w2: " + System.currentTimeMillis());
                rwLock.acquireWriteLock();
                System.out.println("write lock acquired w2: " + System.currentTimeMillis());
                Thread.sleep(700);
            } catch (InterruptedException e) {

            }
            rwLock.releaseWriteLock();
            System.out.println("Releasing write lock in w2: " + System.currentTimeMillis());
        });

        Thread r1 = new Thread(() -> {
            try {
                rwLock.acquireReadLock();
                System.out.println("Read lock acquired: " + System.currentTimeMillis());
                Thread.sleep(400);
            } catch (InterruptedException ie) {

            }
            System.out.println("Releasing read lock in r1: " + System.currentTimeMillis());
            rwLock.releaseReadLock();
        });

        Thread r2 = new Thread(() -> {
            try {
                rwLock.acquireReadLock();
                System.out.println("Read lock acquired: " + System.currentTimeMillis());
                Thread.sleep(500);
            } catch (InterruptedException ie) {

            }
            System.out.println("Releasing read lock in r2: " + System.currentTimeMillis());
            rwLock.releaseReadLock();
        });

        Thread r3 = new Thread(() -> {
            try {
                rwLock.acquireReadLock();
                System.out.println("Read lock acquired: " + System.currentTimeMillis());
                Thread.sleep(1000);
            } catch (InterruptedException ie) {

            }
            System.out.println("Releasing read lock in r2: " + System.currentTimeMillis());
            rwLock.releaseReadLock();
        });

        r1.start();
        w1.start();
        r2.start();
        Thread.sleep(600);
        w2.start();
        r3.start();
        r1.join();
        r1.join();
        w2.join();
        w1.join();
        r3.join();
    }
}
