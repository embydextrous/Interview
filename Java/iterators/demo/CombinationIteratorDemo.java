package iterators.demo;

import iterators.CombinationIterator;

public class CombinationIteratorDemo {
    public static void main(String[] args) {
        String s = "abcd";
        CombinationIterator iterator = new CombinationIterator(s, 2);
        while (iterator.hasNext()) {
           System.out.println(iterator.next());
        }
    }
}
