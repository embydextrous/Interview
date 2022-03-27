package multithreading.library;

import java.util.Random;

public class Student implements Runnable {
    private int id;
    private Random random;

    public Student(int id) {
        this.id = id;
        this.random = new Random();
    }

    @Override
    public void run() {
        while (true) {
            int bookIndex = random.nextInt(Constants.books.length);
            Book book = Constants.books[bookIndex];
            try {
                book.read(this);
            } catch (InterruptedException e) {
               
            }
        }
    }

    @Override
    public String toString() {
        return "Student" + id;
    }
}
