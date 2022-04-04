package multithreading.problems.blockingqueue;

import java.util.Arrays;

public class ArrayBlockingQueue<T> implements BlockingQueue<T> {

    private T[] array;
    private int capacity;
    private int head = 0;
    private int tail = 0;
    private int size = 0;

    public ArrayBlockingQueue(int capacity) {
        this.capacity = capacity;
        array = (T[]) new Object[capacity]; 
    }

    @Override
    public synchronized void enqueue(T item) throws InterruptedException {
        while(size == capacity) {
            wait();
        }
        array[tail] = item;
        tail = (tail + 1) % capacity;
        size++;
        System.out.println("Queue Size: " + size + ", Queue: " + Arrays.asList(array));
        /**
         * Why notifyAll() and not notify()?
         * 
         * Suppose we have two producer threads and the queue gets full. notify() may invoke other
         * producer thread which may go into wait() and the consumer threads are never notified.
         */
        notifyAll();
    }

    @Override
    public synchronized T dequeue() throws InterruptedException {
        while(size == 0) {
            wait();
        }
        T item = array[head];
        array[head] = null;
        head = (head + 1) % capacity;
        size--;
        System.out.println("Queue Size: " + size + ", Queue: " + Arrays.asList(array));
        notify();
        return item;
    }
}
