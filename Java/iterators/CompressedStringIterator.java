package iterators;

import java.util.Iterator;
import java.util.NoSuchElementException;

public class CompressedStringIterator implements Iterator<Character> {
    private final String compressedString;
    private Character currentChar;
    private int currentCount;
    private int currentIndex;

    public CompressedStringIterator(String compressedString) {
        this.compressedString = compressedString;
        locateNext();
    }

    @Override
    public boolean hasNext() {
        return currentChar != null;
    }

    @Override
    public Character next() throws NoSuchElementException {
        if (hasNext()) {
            char c = currentChar;
            currentCount--;
            if (currentCount == 0) {
                currentChar = null;
                locateNext();
            }
            return c;
        } else {
            throw new NoSuchElementException();
        }
    }
    
    private void locateNext() {
        if (currentIndex == compressedString.length()) {
            return;
        }
        currentChar = compressedString.charAt(currentIndex++);
        char c = compressedString.charAt(currentIndex++);
        while(isDigit(c)) {
            currentCount = 10 * currentCount + toDigit(c);
            if (currentIndex == compressedString.length()) {
                break;
            }
            c = compressedString.charAt(currentIndex);
            if (!isDigit(c)) {
                break;
            }
            currentIndex++;
        }
    }

    private boolean isDigit(char c) {
        return c >= '0' && c <= '9';
    }

    private int toDigit(char c) {
        return c - '0';
    }
}
