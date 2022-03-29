package iterators;

import java.util.Iterator;
import java.util.NoSuchElementException;
import iterators.CountingIterator.Pair;

public class CountingIterator<T> implements Iterator<Pair<T>> {
    private final PeekingIterator<T> peekingIterator;

    public CountingIterator(Iterator<T> iterator) {
        this.peekingIterator = new PeekingIterator<>(iterator);
    }

    @Override
    public boolean hasNext() {
        return peekingIterator.hasNext();
    }
    
    @Override
    public Pair<T> next() throws NoSuchElementException {
        if (hasNext()) {
            return advanceIterator();
        } else {
            throw new NoSuchElementException();
        }
    }
    
    private Pair<T> advanceIterator() {
        T next = peekingIterator.next();
        int count = 1;
        while (peekingIterator.peek() == next) {
            count++;
            peekingIterator.next();
        }
        return new Pair<T>(next, count);
    }

    static public class Pair<T> {
        private T value;
        private int count;
    
        public Pair(T value, int count) {
            this.value = value;
            this.count = count;
        }
    
        @Override
        public String toString() {
            return "Pair[value= " + value.toString() + ", count= " + count + "]";
        }
    }
}
