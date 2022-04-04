package multithreading.problems.rwlock;

public class ReadWriteLock {
    private boolean isWriting = false;
    private int readers = 0;

    public synchronized void acquireWriteLock() throws InterruptedException {
        while (isWriting || readers > 0) {
            wait();
        }
        isWriting = true;
    }

    public synchronized void releaseWriteLock() {
        isWriting = false;
        notifyAll();
    }

    public synchronized void acquireReadLock() throws InterruptedException {
        while(isWriting) {
            wait();
        }
        readers++;
    }

    public synchronized void releaseReadLock() {
        readers--;
        notify();
    }
}
