package multithreading.parallel.metrics;

public class MetricsPrinter extends Thread {
    private final Metrics metrics;

    public MetricsPrinter(Metrics metrics) {
        this.metrics = metrics;
    }

    @Override
    public void run() {
        System.out.println("jhhhj");
        while(true) {
            try {
                Thread.sleep(100);
            } catch (InterruptedException e) {
                
            }
            System.out.println("Current Average is " + metrics.getAverage());
        }
    }
}
