package iterators.peeking;

import java.util.HashSet;
import java.util.Iterator;
import java.util.NoSuchElementException;
import java.util.PriorityQueue;
import java.util.Queue;
import java.util.Set;

public class UniqueIterator<T extends Comparable<T>> implements Iterator<T> {
    private final Queue<ComparablePeekingIterator<T>> iters;
    private T next;
    private final Set<T> doneElements;
    
    public UniqueIterator(Iterator<Iterator<T>> iterators) {
        this.iters = new PriorityQueue<>();
        this.doneElements = new HashSet<>();
        while (iterators.hasNext()) {
            Iterator<T> iterator = iterators.next();
            if (iterator.hasNext()) {
                iters.add(new ComparablePeekingIterator<>(iterator));
            }
        }
        advanceIterator();
    }

    @Override
    public boolean hasNext() {
        return next != null;
    }

    @Override
    public T next() throws NoSuchElementException {
        if (hasNext()) {
            T current = next;
            doneElements.add(current);
            advanceIterator();
            return current;
        } else {
            throw new NoSuchElementException();
        }
    }

    private void advanceIterator() {
        if (iters.isEmpty()) {
            next = null;
            return;
        }
        while(!iters.isEmpty()) {
            ComparablePeekingIterator<T> iterator = iters.poll();
            T peek = iterator.peek();
            if (doneElements.contains(peek)) {
                iterator.next();
                if (iterator.hasNext()) {
                    iters.add(iterator);
                }
            } else {
                next = iterator.next();
                if (iterator.hasNext()) {
                    iters.add(iterator);
                }
                break;
            }
        }
    }
}
