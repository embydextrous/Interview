package multithreading.problems.tokenbucket;

import java.util.concurrent.locks.Condition;
import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReentrantLock;

public class BackgroundThreadTokenBucket implements TokenBucket {
    private final int MAX_TOKENS;
    private int tokens;
    private final Lock lock = new ReentrantLock(true);
    private final Condition condition = lock.newCondition();

    BackgroundThreadTokenBucket(int maxTokens) {
        this.MAX_TOKENS = maxTokens;
    }

    @Override
    public void awaitToken() throws InterruptedException {
        lock.lock();
        try {
            while(tokens == 0) {
                condition.await();;
            }
            tokens--;
            System.out.println("Granted token to " + Thread.currentThread().getName()
                     + " at " + System.currentTimeMillis()/ 1000);
        } finally {
            lock.unlock();
        }
    }

    void init() {
        Thread t = new Thread(() -> {
            fillTokens();
        });
        t.setDaemon(true);
        t.start();
    }

    private void fillTokens() {
        while (true) {
            lock.lock();
            try {
                if (tokens < MAX_TOKENS) {
                    tokens++;
                    condition.signal();
                }
                try {
                    Thread.sleep(TOKEN_ISSUE_RATE_MS);
                } catch(InterruptedException e) {
                    // swallow exception
                }
            } finally {
                lock.unlock();
            }
        }
    }
}
