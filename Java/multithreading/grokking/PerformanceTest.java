package multithreading.grokking;

public class PerformanceTest {
    public static void main(String[] args) throws InterruptedException {
        long n = 1000000000;
        oneThread(n);
        twoThreads(n);
        numCPUThreads(n);
    }

    static void oneThread(long n) {
        long start = System.nanoTime();
        long sum = sum(1, n);
        long end = System.nanoTime();
        System.out.println("Single thread final count = " + sum + " took " + (end - start));
    }

    static void twoThreads(long n) throws InterruptedException {
        long start = System.nanoTime();
        final long[] s = {0, 0};
        Thread t1 = new Thread(new Runnable() {
            @Override
            public void run() {
                s[0] = sum(1, n / 2);
            }
        });
        Thread t2 = new Thread(new Runnable() {
            @Override
            public void run() {
                s[1] = sum(n/2 + 1, n);
            }
        });
        t1.start();
        t2.start();
        t1.join();
        t2.join();
        long sum = s[0] + s[1];
        long end = System.nanoTime();
        System.out.println("Two threads final count = " + sum + " took " + (end - start));
    }

    static void numCPUThreads(long n) throws InterruptedException {
        long start = System.nanoTime();
        int numCPU = Runtime.getRuntime().availableProcessors();
        final long[] s = new long[numCPU];
        final long[] startPoints = new long[numCPU];
        startPoints[0] = 1;
        for (int i = 1; i < numCPU; i++) {
            startPoints[i] = startPoints[i-1] + n / numCPU;
        }
        Thread[] threads = new Thread[numCPU];
        for (int i = 0; i < numCPU; i++) {
            final int x = i;
            threads[i] = new Thread(new Runnable() {
                @Override
                public void run() {
                    if (x != numCPU - 1) {
                        s[x] = sum(startPoints[x], startPoints[x+1] - 1);
                    } else {
                        s[x] = sum(startPoints[x], n);
                    }
                }
            });
        }
        for (Thread t : threads) {
            t.start();
        }
        for (Thread t : threads) {
            t.join();
        }
        long sum = 0;
        for (int i = 0; i < numCPU; i++) {
            sum += s[i];
        }
        long end = System.nanoTime();
        System.out.println(numCPU + " threads final count = " + sum + " took " + (end - start));
    }

    static long sum(long from, long to) {
        long s = 0;
        for (long i = from; i <= to; i++) {
            s += i;
        }
        return s;
    }
}


