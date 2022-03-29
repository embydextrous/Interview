package iterators.demo;

import java.util.LinkedList;
import java.util.List;

import iterators.CountingIterator;

public class CountingIteratorDemo {
    public static void main(String[] args) {
        String[] names = {"foo", "foo", "foo", "bar", "baz", "foo", "bar", "bar"};
        List<String> nameList = new LinkedList<>();
        for(String name : names) {
            nameList.add(name);
        }
        CountingIterator countingIterator = new CountingIterator(nameList.iterator());
        while(countingIterator.hasNext()) {
            System.out.println(countingIterator.next());
        }
    }
}
