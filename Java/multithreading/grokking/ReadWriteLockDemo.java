package multithreading.grokking;

import java.util.concurrent.atomic.AtomicLong;
import java.util.concurrent.locks.Condition;
import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReentrantLock;
import java.util.concurrent.locks.ReentrantReadWriteLock;
import java.util.concurrent.locks.StampedLock;

public class ReadWriteLockDemo {
    public static void main(String[] args) throws InterruptedException {
        OneLock one = new OneRWLock();
        Thread writer = new Thread(new Runnable() {
            @Override
            public void run() {
                while(true) {
                    one.increment();
                }
            }
        });
        Thread[] readerThreads = new Thread[10];
        for (int i = 0; i < 10; i ++) {
            readerThreads[i] = new Thread(new Runnable() {
                @Override
                public void run() {
                    while(true) {
                        one.read();
                    }
                }
            });
        }
        writer.setDaemon(true);
        writer.start();
        for (Thread readerThread : readerThreads) {
            readerThread.setDaemon(true);
            readerThread.start();
        }
        int timeInSeconds = 10;
        Thread.sleep(1000 * timeInSeconds);
        System.out.println("Number of operations in " + timeInSeconds + " seconds: " + one.getCounter());
    }
}

interface OneLock {
    void increment();
    int read();
    long getCounter();
}

class OneSimpleLock implements OneLock {
    private long count;
    private Lock lock = new ReentrantLock();

    @Override
    public void increment() {
        lock.lock();
        try {
            count++;
        } finally {
            lock.unlock();
        }
    }

    @Override
    public int read() {
        lock.lock();
        try {
            count++;
        } finally {
            lock.unlock();
        }
        return 0;
    }

    @Override
    public long getCounter() {
        return count;
    }
}

class OneRWLock implements OneLock {
    private AtomicLong count = new AtomicLong();
    private StampedLock lock = new StampedLock();

    @Override
    public void increment() {
        long stamp = lock.writeLock();
        try {
            count.incrementAndGet();
        } finally {
            lock.unlockWrite(stamp);
        }
    }

    @Override
    public int read() {
        long stamp = lock.tryOptimisticRead();
        if (!lock.validate(stamp)) {
            stamp = lock.readLock();
            try {
                count.incrementAndGet();
            } finally {
             lock.unlockRead(stamp);
            }
        }
        return 0;
    }

    @Override
    public long getCounter() {
        return count.get();
    }
}