package iterators;

import java.util.HashMap;
import java.util.Iterator;
import java.util.Map;
import java.util.NoSuchElementException;

public class SkipIterator<T> implements Iterator<T> {
    private final PeekingIterator<T> peekingIterator;
    private final Map<T, Integer> skipMap;

    public SkipIterator(Iterator<T> iterator) {
        this.peekingIterator = new PeekingIterator<>(iterator);
        this.skipMap = new HashMap<>();
    }

    public void skip(T skip) {
        skipMap.compute(skip, (k,  v) -> v == null ? 1 : v + 1);
        if (peekingIterator.hasNext() && peekingIterator.peek().equals(skip)) {
            advanceIterator();
        }
    }

    @Override
    public boolean hasNext() {
        return peekingIterator.hasNext();
    }

    @Override
    public T next() throws NoSuchElementException {
        if (hasNext()) {
            T next = peekingIterator.next();
            advanceIterator();
            return next;
        } else {
            throw new NoSuchElementException();
        }
    }

    private void advanceIterator() {
        while (peekingIterator.hasNext() && skipMap.containsKey(peekingIterator.peek())) {
            T peek = peekingIterator.peek();
            int count = skipMap.get(peek);
            if (count > 1) {
                skipMap.put(peek, count - 1);
            } else {
                skipMap.remove(peek);
            }
            peekingIterator.next();
        }
    }
}
