package multithreading.problems.blockingqueue;


public interface BlockingQueue<T> {
    public void enqueue(T item) throws InterruptedException;
    public T dequeue() throws InterruptedException;
}
