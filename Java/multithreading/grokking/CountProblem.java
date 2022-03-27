package multithreading.grokking;

public class CountProblem {
    static int singleThreadCount = 0;
    static int twoThreadCount = 0;
    public static void main(String[] args) throws InterruptedException {
        int n = 1_000_000;
        for(int i = 0; i < n; i++) {
            singleThreadCount += 1;
        }
        Thread t1 = new Thread(new Runnable() {
            @Override
            public void run() {
                for(int i = 0; i < n / 2; i++) {
                    twoThreadCount += 1;
                }
            }
        });
        Thread t2 = new Thread(new Runnable() {
            @Override
            public void run() {
                for(int i = 0; i < n / 2; i++) {
                    twoThreadCount += 1;
                }
            }
        });
        t1.start();
        t2.start();
        t1.join();
        t2.join();
        System.out.println("Single thread count is: " + singleThreadCount); // this is 1000000
        System.out.println("Two threads count is: " + twoThreadCount); // this won't be 1000000
    }
}
