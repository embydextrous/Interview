package multithreading.grokking;

import java.util.Random;

public class RaceCondition {

    static Random random = new Random();
    static int s = 0;
    public static void main(String[] args) throws InterruptedException {
        Thread t1 = new Thread(new Runnable() {
            @Override
            public void run() {
                for(int i = 0; i < 1000000; i++) {
                    s = random.nextInt(10000);
                }
            }
        });

        Thread t2 = new Thread(new Runnable() {
            @Override
            public void run() {
                for(int i = 0; i < 1000000; i++) {
                    if (s % 5 == 0) {
                        System.out.print(s);
                    }
                }
            }
        });
        t1.start();
        t2.start();
        t1.join();
        t2.join();
    } 
}
