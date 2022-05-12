package iterators.revision;

import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;
import java.util.NoSuchElementException;

public class Revision {
    public static void main(String[] args) {
        List<Integer> list1 = new ArrayList<>();
        list1.add(0);
        list1.add(1);
        list1.add(2);
        list1.add(4);
        list1.add(6);
        list1.add(7);

        List<Integer> list2 = new ArrayList<>();
        list2.add(0);
        list2.add(2);
        list2.add(5);
        list2.add(7);
        list2.add(8);
        List<Integer> list3 = new ArrayList<>();
        list3.add(1);
        List<Integer> list4 = new ArrayList<>();
        list4.add(0);
        list4.add(4);
        list4.add(6);
        List<Iterator<Integer>> lists = new ArrayList<>();
        lists.add(list1.iterator());
        lists.add(list2.iterator());
        lists.add(list3.iterator());
        lists.add(list4.iterator());
        UnionIterator<Integer> unionIterator = new UnionIterator<>(list1.iterator(), list2.iterator());
        while(unionIterator.hasNext()) {
            System.out.println(unionIterator.next());
        }
    }
}

class UnionIterator<T extends Comparable<T>> implements Iterator<T> {
    private PeekingIterator<T> p1;
    private PeekingIterator<T> p2;
    private T next;

    UnionIterator(Iterator<T> p1, Iterator<T> p2) {
        this.p1 = new PeekingIterator<>(p1);
        this.p2 = new PeekingIterator<>(p2);
        advanceIterator();
    }

    @Override
    public boolean hasNext() {
        return next != null;
    }

    @Override
    public T next() {
        if (hasNext()) {
            T value = next;
            advanceIterator();
            return value;
        }
        throw new NoSuchElementException();
    }

    private void advanceIterator() {
        next = null;
        if (p1.hasNext() && p2.hasNext()) {
            int c = p1.peek().compareTo(p2.peek());
            if (c == 0) {
                next = p1.next();
                p2.next();
            } else if (c < 0) {
                next = p1.next();
            } else {
                next = p2.next();
            }
        } else if (p1.hasNext()) {
            next = p1.next();
        } else if (p2.hasNext()) {
            next = p2.next();
        }
    }
}

class PeekingIterator<T> implements Iterator<T> {
    private Iterator<T> iterator;
    private T next;
    private boolean hasNext;

    PeekingIterator(Iterator<T> iterator) {
        this.iterator = iterator;
        advanceIterator();
    }

    @Override
    public boolean hasNext() {
        return hasNext;
    }

    public T peek() {
        return next;
    }

    @Override
    public T next() {
        if (hasNext) {
            T value = next;
            advanceIterator();
            return value;
        } else {
            throw new NoSuchElementException();
        }
    }

    private void advanceIterator() {
        hasNext = iterator.hasNext();
        if (hasNext) {
            next = iterator.next();
        } else {
            next = null;
        }
    }
}

