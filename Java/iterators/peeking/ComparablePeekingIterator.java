package iterators.peeking;

import java.util.Iterator;
import java.util.NoSuchElementException;

public class ComparablePeekingIterator<T extends Comparable<T>> implements Iterator<T>, Comparable<ComparablePeekingIterator<T>> {
    private Iterator<T> iterator;
    private T next;
    private boolean hasNext;

    public ComparablePeekingIterator(Iterator<T> iterator) {
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

    @Override
    public int compareTo(ComparablePeekingIterator<T> o) {
        if (o == null) {
            return -1;
        }
        T peek1 = peek();
        T peek2 = o.peek();
        if (peek1 != null && peek2 != null) {
            return peek1.compareTo(peek2);
        }
        if (peek1 == null && peek2 == null) {
            return 0;
        }
        return peek1 == null ? 1 : -1;
    }

    
}
