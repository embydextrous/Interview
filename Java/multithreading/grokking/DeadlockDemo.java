package multithreading.grokking;

import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReentrantLock;

public class DeadlockDemo {
    public static void main(String[] args) throws InterruptedException {
        TwoCounter twoCounter = new TwoCounter();
        Thread t1 = new Thread(new Runnable() {
            @Override
            public void run() {
                twoCounter.increment1Then2();
            }
        });
        Thread t2 = new Thread(new Runnable() {
            @Override
            public void run() {
                twoCounter.incremen2Then1();
            }
        });
        t1.start();
        t2.start();
        t1.join();
        t2.join();
    }
}

class TwoCounter {
    private int count1 = 0;
    private int count2 = 0;
    private Lock lock1 = new ReentrantLock();
    private Lock lock2 = new ReentrantLock();

    public void increment1Then2() {
        for (int i = 0; i < 100000; i++) {
            acquireLocks();
            try {
                count1++;
                count2++;
            } finally {
                lock1.unlock();
                lock2.unlock();
            }
        }
    }

    // Sample way to acquire locks to prevent accidental deadlocks
    private void acquireLocks() {
        while (true) {
            boolean gotFirstLock = false;
            boolean gotSecondLock = false;
            try {
                gotFirstLock = lock1.tryLock();
                gotSecondLock = lock2.tryLock();
            } finally {
                if (gotFirstLock && gotSecondLock) {
                    return;
                }
                if (gotFirstLock) {
                    lock1.unlock();
                }
                if (gotSecondLock) {
                    lock2.unlock();
                }
            }
            try {
                Thread.sleep(1); 
            } catch(InterruptedException e) {
                e.printStackTrace();
            }
        }
    }

    public void incremen2Then1() {
        for (int i = 0; i < 100000; i++) {
            acquireLocks();
            try {
                count2++;
                count1++;
            } finally {
                lock2.unlock();
                lock1.unlock();
            }
        }
    }
}