package iterators.demo;

import java.util.ArrayList;
import java.util.Iterator;
import java.util.LinkedList;
import java.util.List;
import java.util.TreeSet;

import iterators.Flatten2DVectorIterator;

public class Flatten2DVectorDemo {
    public static void main(String[] args) {
        List<Integer> list1 = new ArrayList<>();
        list1.add(4);
        list1.add(7);
        list1.add(2);

        List<Integer> list2 = new LinkedList<>();
        list2.add(3);
        list2.add(7);
        list2.add(9);

        TreeSet<Integer> ts = new TreeSet<>();
        ts.add(9);
        ts.add(1);
        ts.add(3);
        ts.add(2);


        List<Iterator<Integer>> iterators = new LinkedList<>();
        iterators.add(list1.iterator());
        iterators.add(list2.iterator());
        iterators.add(ts.iterator());

        Flatten2DVectorIterator<Integer> iterator = new Flatten2DVectorIterator<>(iterators.iterator());
        while (iterator.hasNext()) {
            System.out.println(iterator.next());
        }
    }
}