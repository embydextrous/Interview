package iterators;

import java.util.Iterator;
import java.util.NoSuchElementException;

public class PeekingIterator<T> implements Iterator<T> {
    private Iterator<T> iterator;
    private T next;
    private boolean hasNext;

    public PeekingIterator(Iterator<T> iterator) {
        this.iterator = iterator;
        advanceIterator();
    }
    
    @Override
    public T next() throws NoSuchElementException {
        if (hasNext) {
            T current = next;
            advanceIterator();
            return current;
        } else {
            throw new NoSuchElementException();
        }
    }

    public T peek() {
        return next;
    }

    @Override
    public boolean hasNext() {
        return hasNext;
    }

    private void advanceIterator() {
        hasNext = iterator.hasNext();
        next = hasNext ? iterator.next() : null;
    }
}
