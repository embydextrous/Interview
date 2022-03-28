package multithreading.grokking;

import java.util.ArrayList;
import java.util.List;
import java.util.Random;
import java.util.concurrent.atomic.AtomicLong;
import java.util.concurrent.atomic.AtomicReference;
import java.util.concurrent.locks.LockSupport;

// Why atomic operations and CAS are faster?
// https://stackoverflow.com/questions/19623026/why-are-cas-atomic-operations-faster-than-synchronized-or-volatile-operations
public class AtomicStackDemo {
    public static void main(String[] args) throws InterruptedException {
        AtomicStack<Integer> stack = new AtomicStack<>();
        Random random = new Random();
        int pushingThreads = 4;
        int poppingThreads = 4;
        List<Thread> threads = new ArrayList<>();
        for (int i = 0; i < pushingThreads; i++) {
            Thread t = new Thread(() -> {
                while (true) {
                    stack.push(random.nextInt(1000));
                }
            });
            t.setDaemon(true);
            threads.add(t);
        }
        for (int i = 0; i < poppingThreads; i++) {
            Thread t = new Thread(() -> {
                while (true) {
                    stack.pop();
                }
            });
            t.setDaemon(true);
            threads.add(t);
        }

        for(Thread t : threads) {
            t.start();
        }
        int timeInSeconds = 5;
        Thread.sleep(1000 * timeInSeconds);
        System.out.println("Number of operations in " + timeInSeconds + " seconds: " + stack.getCounter());
    }
}

class StandardStack<T> {
    private StackNode<T> head;
    private volatile long counter = 0;

    public synchronized void push(T value) {
        StackNode<T> newHead = new StackNode<>(value);
        newHead.next = head;
        head = newHead;
        counter++;
    }

    public synchronized T pop() {
        if (head == null) {
            counter++;
            return null;
        }
        T value = head.value;
        head = head.next;
        counter++;
        return value;
    }

    public long getCounter() {
        return counter;
    }
}

class AtomicStack<T> {
    private AtomicReference<StackNode<T>> head = new AtomicReference<>();
    private AtomicLong counter = new AtomicLong(0);

    public void push(T value) {
        StackNode<T> newHead = new StackNode<>(value);
        while (true) {
            StackNode<T> currentHeadNode = head.get();
            newHead.next = currentHeadNode;
            if (head.compareAndSet(currentHeadNode, newHead)) {
                break;
            } else {
                LockSupport.parkNanos(1);
            }
        }
        counter.incrementAndGet();
    }

    public T pop() {
        StackNode<T> currentHead = head.get();
        StackNode<T> newHead;
        while (currentHead != null) {
            newHead = currentHead.next;
            if (head.compareAndSet(currentHead, newHead)) {
                break;
            } else {
                LockSupport.parkNanos(1);
                currentHead = head.get();
            }
        }
        counter.incrementAndGet();
        return currentHead != null ? currentHead.value : null;
    }

    public long getCounter() {
        return counter.get();
    }
}

class StackNode<T> {
    public T value;
    public StackNode<T> next;

    public StackNode(T value) {
        this.value = value;
    }
}
