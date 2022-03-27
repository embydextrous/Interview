package iterators.peeking;

import java.util.Arrays;
import java.util.List;

public class SkipIteratorDemo {
    public static void main(String[] args) {
        Integer[] intArr = {1, 3, 4, 2, 5, 4, 3, 2, 3, 2, 4, 5, 6};
        List<Integer> list = Arrays.asList(intArr);
        SkipIterator<Integer> skipIterator = new SkipIterator<>(list.iterator());
        System.out.println(skipIterator.next());
        skipIterator.skip(3);
        System.out.println(skipIterator.next());
        skipIterator.skip(2);
        skipIterator.skip(2);
        System.out.println(skipIterator.next());
        System.out.println(skipIterator.next());
        System.out.println(skipIterator.next());
        System.out.println(skipIterator.next());
        System.out.println(skipIterator.next());
        System.out.println(skipIterator.next());
    }
}
