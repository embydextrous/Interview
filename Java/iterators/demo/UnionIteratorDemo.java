package iterators.demo;

import java.util.TreeSet;

import iterators.UnionIterator;

public class UnionIteratorDemo {
    public static void main(String[] args) {
        TreeSet<Integer> ts1 = new TreeSet<>();
        TreeSet<Integer> ts2 = new TreeSet<>();
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
        UnionIterator<Integer> unionIterator = new UnionIterator<>(ts1.iterator(), ts2.iterator());
        while (unionIterator.hasNext()) {
            System.out.println(unionIterator.next());
        }
    }
}
