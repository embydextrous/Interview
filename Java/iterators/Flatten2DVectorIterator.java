package iterators;

import java.util.Iterator;
import java.util.LinkedList;
import java.util.NoSuchElementException;

public class Flatten2DVectorIterator<T> implements Iterator<T> {
    private LinkedList<Iterator<T>> iterList;

    public Flatten2DVectorIterator(Iterator<Iterator<T>> iterators) {
        this.iterList = new LinkedList<>();
        while(iterators.hasNext()) {
            Iterator<T> iterator = iterators.next();
            if (iterator.hasNext()) {
                iterList.add(iterator);
            }
        }
    }

    @Override
    public boolean hasNext() {
        return !iterList.isEmpty();
    }

    @Override
    public T next() throws NoSuchElementException {
        if (hasNext()) {
            T next = iterList.getFirst().next();
            if (!iterList.getFirst().hasNext()) {
                iterList.removeFirst();
            }
            return next;
        } else {
            throw new NoSuchElementException();
        }
    }
}
