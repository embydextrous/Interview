package multithreading.grokking;

public interface Processor {
    public void produce() throws InterruptedException;

    public void consume() throws InterruptedException;
}
