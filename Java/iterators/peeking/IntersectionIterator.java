package iterators.peeking;

import java.util.Iterator;
import java.util.NoSuchElementException;

public class IntersectionIterator<T extends Comparable<T>> implements Iterator<T> {
    private final PeekingIterator<T> peekingIter1;
    private final PeekingIterator<T> peekingIter2; 
    private T next;

    public IntersectionIterator(Iterator<T> iterator1, Iterator<T> iterator2) {
        peekingIter1 = new PeekingIterator<>(iterator1);
        peekingIter2 = new PeekingIterator<>(iterator2);
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
            peekingIter1.next();
            peekingIter2.next();
            advanceIterator();
            return current;
        } else {
            throw new NoSuchElementException();
        }
    }

    private void advanceIterator() {
        if (!peekingIter1.hasNext() || !peekingIter2.hasNext()) {
            next = null;
            return;
        }
        T peek1 = peekingIter1.peek();
        T peek2 = peekingIter2.peek();
        int compareTo = peek1.compareTo(peek2);
        if (compareTo < 0) {
            peekingIter1.next();
            advanceIterator();
        } else if (compareTo > 0) {
            peekingIter2.next();
            advanceIterator();
        } else {
            next = peek1;
        }
    }
}
