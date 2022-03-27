package iterators.peeking;

import java.util.Iterator;
import java.util.TreeSet;

public class IntersectionIteratorDemo {
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
        IntersectionIterator<Integer> intersectionIterator = new IntersectionIterator<>(ts1.iterator(), ts2.iterator());
        while (intersectionIterator.hasNext()) {
            System.out.println(intersectionIterator.next());
        }
    }
}
