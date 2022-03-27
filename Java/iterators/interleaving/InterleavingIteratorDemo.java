package iterators.interleaving;

import java.util.ArrayList;
import java.util.Iterator;
import java.util.LinkedList;
import java.util.List;
import java.util.TreeSet;

public class InterleavingIteratorDemo {
    public static void main(String[] args) {
        List<String> indianNames = new ArrayList<>();
        indianNames.add("Sachin");
        indianNames.add("Virat");
        indianNames.add("Rohit");
        indianNames.add("Kapil");
        List<String> westernNames = new LinkedList<>();
        westernNames.add("Biden");
        westernNames.add("Trump");
        westernNames.add("Clinton");
        TreeSet<String> pakistaniNames = new TreeSet<>();
        pakistaniNames.add("Shahid");
        pakistaniNames.add("Junaid");
        pakistaniNames.add("Sayeed");
        pakistaniNames.add("Saqlain");
        pakistaniNames.add("Wasim");
        List<Iterator<String>> iterators = new ArrayList<>();
        iterators.add(indianNames.iterator());
        iterators.add(westernNames.iterator());
        iterators.add(pakistaniNames.iterator());
        InterleavingIterator<String> interleavingIterator = new InterleavingIterator<>(iterators.iterator());
        while (interleavingIterator.hasNext()) {
            System.out.println(interleavingIterator.next());
        }
    }
}
