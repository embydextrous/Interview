package multithreading.library;

import java.util.concurrent.TimeUnit;
import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReentrantLock;

public class Book {
    private int id;
    private Lock lock;

    Book(int id) {
        this.id = id;
        lock = new ReentrantLock(true);
    }

    public void read(Student student) throws InterruptedException {
        if (lock.tryLock(10, TimeUnit.SECONDS)) {
            try {
                System.out.println(student + " starts reading " + this);
                Thread.sleep(2000);
                System.out.println(student + " has finished reading " + this);
            } finally {
                lock.unlock();
            }
        }
    }

    @Override
    public String toString() {
        return "Book" + id;
    }
}
