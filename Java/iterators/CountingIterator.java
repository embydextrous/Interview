package iterators;

import java.util.Iterator;
import java.util.NoSuchElementException;
import iterators.CountingIterator.Pair;

public class CountingIterator implements Iterator<Pair> {
    private final PeekingIterator<String> peekingIterator;

    public CountingIterator(Iterator<String> iterator) {
        this.peekingIterator = new PeekingIterator<>(iterator);
    }

    @Override
    public boolean hasNext() {
        return peekingIterator.hasNext();
    }
    
    @Override
    public Pair next() throws NoSuchElementException {
        if (hasNext()) {
            return advanceIterator();
        } else {
            throw new NoSuchElementException();
        }
    }
    
    private Pair advanceIterator() {
        String next = peekingIterator.next();
        int count = 1;
        while (peekingIterator.peek() == next) {
            count++;
            peekingIterator.next();
        }
        return new Pair(next, count);
    }

    static public class Pair {
        private String value;
        private int count;
    
        public Pair(String value, int count) {
            this.value = value;
            this.count = count;
        }
    
        @Override
        public String toString() {
            return "Pair[value= " + value.toString() + ", count= " + count + "]";
        }
    }
}
