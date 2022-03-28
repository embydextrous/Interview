package iterators;

import java.util.Iterator;
import java.util.NoSuchElementException;

public class UnionIterator<T extends Comparable<T>> implements Iterator<T> {
    private final PeekingIterator<T> peekIter1;
    private final PeekingIterator<T> peekIter2;
    private T next;

    public UnionIterator(Iterator<T> iter1, Iterator<T> iter2) {
        this.peekIter1 = new PeekingIterator<>(iter1);
        this.peekIter2 = new PeekingIterator<>(iter2);
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
            advanceIterator();
            return current;
        } else {
            throw new NoSuchElementException();
        }
    }
    
    private void advanceIterator() {
        if (!peekIter1.hasNext() && !peekIter2.hasNext()) {
            next = null;
            return;
        }
        if (!peekIter1.hasNext()) {
            next = peekIter2.next();
            return;
        }
        if (!peekIter2.hasNext()) {
            next = peekIter1.next();
            return;
        }
        T peek1 = peekIter1.peek();
        T peek2 = peekIter2.peek();
        int compareTo = peek1.compareTo(peek2);
        if (compareTo < 0) {
            next = peekIter1.next();
        } else if (compareTo > 0) {
            next = peekIter2.next();
        } else {
            next = peekIter1.next();
            peekIter2.next();
        }
    }
}
