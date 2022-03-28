package iterators;

import java.util.Iterator;
import java.util.LinkedList;
import java.util.NoSuchElementException;

public class InterleavingIterator<T> implements Iterator<T> {
    private final LinkedList<Iterator<T>> iterators;

    public InterleavingIterator(Iterator<Iterator<T>> iterators) {
        this.iterators = new LinkedList<>();
        while(iterators.hasNext()) {
            Iterator<T> iterator = iterators.next();
            if (iterator.hasNext()) {
                this.iterators.add(iterator);
            }
        }
    }

    @Override
    public T next() throws NoSuchElementException {
        if (hasNext()) {
            Iterator<T> iterator = iterators.removeFirst();
            T value = iterator.next();
            if (iterator.hasNext()) {
                iterators.add(iterator);
            }
            return value;
        } else {
            throw new NoSuchElementException();
        }
    }

    @Override
    public boolean hasNext() {
        return !iterators.isEmpty();
    }
}
