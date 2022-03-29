package iterators.demo;

import iterators.CompressedStringIterator;

public class CompressedStringIteratorDemo {
    public static void main(String[] args) {
        String compressedString = "a3b12c9d15";
        CompressedStringIterator iterator = new CompressedStringIterator(compressedString);
        while(iterator.hasNext()) {
            System.out.print(iterator.next());
        }
        System.out.println();
    }
}
