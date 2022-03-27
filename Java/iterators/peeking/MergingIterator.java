package iterators.peeking;

import java.util.Iterator;
import java.util.NoSuchElementException;
import java.util.PriorityQueue;
import java.util.Queue;

public class MergingIterator<T extends Comparable<T>> implements Iterator<T> {
    private final Queue<PeekingIterator<T>> iters;

    public MergingIterator(Iterator<Iterator<T>> iterators) {
        this.iters = new PriorityQueue<>((i1, i2) -> i1.peek().compareTo(i2.peek()));
        while (iterators.hasNext()) {
            Iterator<T> iterator = iterators.next();
            if (iterator.hasNext()) {
                iters.add(new PeekingIterator<>(iterator));
            }
        }
    }

    @Override
    public boolean hasNext() {
        return !iters.isEmpty();
    }

    @Override
    public T next() throws NoSuchElementException {
        if (hasNext()) {
            PeekingIterator<T> iterator = iters.poll();
            T next = iterator.next();
            if (iterator.hasNext()) {
                iters.add(iterator);
            }
            return next;
        } else {
            throw new NoSuchElementException();
        }
    }
}
