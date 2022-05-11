package iterators.revision;

import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;
import java.util.NoSuchElementException;
import java.util.PriorityQueue;
import java.util.Queue;

import iterators.PeekingIterator;

public class Revision {
    public static void main(String[] args) {
        List<Integer> list1 = new ArrayList<>();
        list1.add(1);
        list1.add(4);
        list1.add(5);
        list1.add(6);
        List<Integer> list2 = new ArrayList<>();
        list2.add(2);
        list2.add(3);
        list2.add(8);
        List<Integer> list3 = new ArrayList<>();
        list3.add(7);
        List<Iterator<Integer>> lists = new ArrayList<>();
        lists.add(list1.iterator());
        lists.add(list2.iterator());
        lists.add(list3.iterator());
        MergingIterator<Integer> mergingIterator = new MergingIterator<>(lists.iterator());
        while (mergingIterator.hasNext()) {
            System.out.println(mergingIterator.next());
        }
    }
}

class MergingIterator<T extends Comparable<T>> implements Iterator<T> {

    private Queue<PeekingIterator<T>> iterators;

    MergingIterator(Iterator<Iterator<T>> iters) {
        iterators = new PriorityQueue<>((i1, i2) -> i1.peek().compareTo(i2.peek()));
        while (iters.hasNext()) {
            Iterator<T> iterator = iters.next();
            if (iterator.hasNext()) {
                PeekingIterator<T> peekingIterator = new PeekingIterator<>(iterator);
                iterators.add(peekingIterator);
            }
        }
    }

    @Override
    public boolean hasNext() {
        return !iterators.isEmpty();
    }

    @Override
    public T next() {
        if (hasNext()) {
            PeekingIterator<T> iterator = iterators.poll();
            T value = iterator.next();
            if (iterator.hasNext()) {
                iterators.add(iterator);
            }
            return value;
        } else {
            throw new NoSuchElementException();
        }
    }
}
