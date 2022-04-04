package multithreading.problems.deferredcallback;

import java.util.HashSet;
import java.util.Set;

import multithreading.problems.deferredcallback.DeferredCallbackExecutor.Callback;

public class Demo {
    public static void main(String[] args) throws InterruptedException {
        Set<Thread> allThreads = new HashSet<Thread>();
        final DeferredCallbackExecutor deferredCallbackExecutor = new DeferredCallbackExecutor();

        Thread service = new Thread(new Runnable() {
            public void run() {
                try {
                    deferredCallbackExecutor.start();
                } catch (InterruptedException ie) {
                    System.out.println("Stopping Executor...");
                }
            }
        });

        service.start();

        for (int i = 0; i < 10; i++) {
            final int k = i;
            Thread thread = new Thread(new Runnable() {
                public void run() {
                    Callback cb = new Callback(() -> System.out.println("Running " + (k + 1)), k * 500);
                    deferredCallbackExecutor.registerCallback(cb);
                }
            });
            thread.setName("Thread_" + (i + 1));
            thread.start();
            allThreads.add(thread);
            Thread.sleep(1000);
        }

        for (Thread t : allThreads) {
            t.join();
        }
        deferredCallbackExecutor.shutdown();
        deferredCallbackExecutor.registerCallback(new Callback(() -> {}, 100));
    }
}
