package iterators;

import java.util.HashSet;
import java.util.Iterator;
import java.util.LinkedList;
import java.util.NoSuchElementException;
import java.util.Queue;
import java.util.Set;

public class UniqueIterator<T> implements Iterator<T> {
    private Queue<PeekingIterator<T>> q;
    private Set<T> doneElements;

    public UniqueIterator(Iterator<Iterator<T>> iters) {
        q = new LinkedList<>();
        doneElements = new HashSet<>();
        while(iters.hasNext()) {
            Iterator<T> iterator = iters.next();
            if (iterator.hasNext()) {
                q.add(new PeekingIterator<>(iterator));
            }
        }
    }

    @Override
    public boolean hasNext() {
        return !q.isEmpty();
    }

    @Override
    public T next() {
        if (hasNext()) {
            PeekingIterator<T> iterator = q.poll();
            T value = iterator.next();
            doneElements.add(value);
            if (iterator.hasNext()) {
                q.add(iterator);
            }
            advanceIterator();
            return value;
        } else {
            throw new NoSuchElementException();
        }
    }

    private void advanceIterator() {
        while (!q.isEmpty()) {
            PeekingIterator<T> iterator = q.peek();
            if (!doneElements.contains(iterator.peek())) {
                break;
            }
            q.poll();
            iterator.next();
            if (iterator.hasNext()) {
                q.add(iterator);
            }
        }
    }
}
