package iterators.demo;

import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;
import java.util.TreeSet;

import iterators.MergingIterator;

public class MergingIteratorDemo {
    public static void main(String[] args) {
        TreeSet<Integer> ts1 = new TreeSet<>();
        TreeSet<Integer> ts2 = new TreeSet<>();
        TreeSet<Integer> ts3 = new TreeSet<>();
        TreeSet<Integer> ts4 = new TreeSet<>();
        ts1.add(1);
        ts1.add(4);
        ts1.add(6);
        ts1.add(7);
        ts1.add(9);

        ts2.add(1);
        ts2.add(2);
        ts2.add(3);
        ts2.add(6);
        ts2.add(7);
        ts2.add(8);
        ts2.add(9);

        ts3.add(2);
        ts3.add(4);
        ts3.add(5);
        ts3.add(8);

        ts4.add(0);
        ts4.add(1);
        ts4.add(6);
        ts4.add(8);
        ts4.add(10);

        List<Iterator<Integer>> iterators = new ArrayList<>();
        iterators.add(ts1.iterator());
        iterators.add(ts2.iterator());
        iterators.add(ts3.iterator());
        iterators.add(ts4.iterator());
        MergingIterator<Integer> mergingIterator = new MergingIterator<>(iterators.iterator());
        while (mergingIterator.hasNext()) {
            System.out.println(mergingIterator.next());
        }
    }
}
