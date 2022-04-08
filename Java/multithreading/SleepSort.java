package multithreading;

import java.util.Arrays;

public class SleepSort {
    public static void main(String[] args) throws InterruptedException {
        int[] a = {3, 7, 1, 9, 2, 8};
        int n = a.length;
        Thread[] threads = new Thread[n];
        final int[] j = {0};
        for(int i = 0; i < n; i++) {
            final int k = a[i];
            threads[i] = new Thread(() -> {
                try {
                    Thread.sleep(k * 1);
                    a[j[0]] = k;
                    j[0] += 1;
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            });
        }
        for(int i = 0; i < n; i++) {
            threads[i].start();
        }
        for(int i = 0; i < n; i++) {
            threads[i].join();
        }
        for(int i = 0; i < n; i++) {
            System.out.print(a[i] + " ");
        }
        System.out.println();
    }
}
