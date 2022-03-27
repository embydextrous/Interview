package multithreading.library;

import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.TimeUnit;

public class LibraryDemo {
    public static void main(String[] args) throws InterruptedException {
        Student[] students = new Student[Constants.NUM_STUDENTS];
        for (int i = 0; i < Constants.NUM_STUDENTS; i++) {
            students[i] = new Student(i + 1);
        }
        ExecutorService executor = Executors.newFixedThreadPool(Constants.NUM_STUDENTS);
        try {
            for (Student student : students) {
                executor.submit(student);
            }
            executor.awaitTermination(1, TimeUnit.MINUTES);
        } finally {
            executor.shutdown();
        }
    }
}
