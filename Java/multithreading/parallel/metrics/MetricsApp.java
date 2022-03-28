package multithreading.parallel.metrics;

public class MetricsApp {
    public static void main(String[] args) throws InterruptedException {
        Metrics metrics = new Metrics();
        BusinessLogic t1 = new BusinessLogic(metrics);
        BusinessLogic t2 = new BusinessLogic(metrics);
        BusinessLogic t3 = new BusinessLogic(metrics);
        MetricsPrinter metricsPrinter = new MetricsPrinter(metrics);
        t1.start();
        t2.start();
        t3.start();
        metricsPrinter.start();
    }
}
