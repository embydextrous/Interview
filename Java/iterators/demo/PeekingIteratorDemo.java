package iterators.demo;

import java.util.LinkedList;
import java.util.List;

import iterators.PeekingIterator;

public class PeekingIteratorDemo {
    public static void main(String[] args) {
        List<String> names = new LinkedList<>();
        names.add("Ataullah");
        names.add("Harraffa");
        names.add("Modu");
        names.add("Madu");
        PeekingIterator<String> peekingIterator = new PeekingIterator<>(names.iterator());
        while (peekingIterator.hasNext()) {
            System.out.println(peekingIterator.peek());
            System.out.println(peekingIterator.next());
        }
    }
}
