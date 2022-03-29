package iterators;

import java.util.HashMap;
import java.util.Iterator;
import java.util.NoSuchElementException;

public class CombinationIterator implements Iterator<String> {
    private final String s;
    private final int L;
    private int mask;
    private final HashMap<Integer, Integer> indexMap = new HashMap<>();

    public CombinationIterator(String s, int n) {
        this.s = s;
        this.L = s.length();
        this.mask = (((1 << n) - 1)) << (L - n);
        int value = L-1;
        int key = 1;
        while(value >= 0) {
            indexMap.put(key, value);
            value -= 1;
            key *= 2;
        }
        System.out.println(mask);
        System.out.println(indexMap);
        System.out.println(L);
        System.out.println(s);
    }

    @Override
    public boolean hasNext() {
        return mask > 0;
    }

    @Override
    public String next() throws NoSuchElementException {
        if (hasNext()) {
            String combination = "";
            int maskToUse = mask;
            while(maskToUse > 0) {
                int indexKey = maskToUse & ~(maskToUse - 1);
                int index = indexMap.get(indexKey);
                combination = s.charAt(index) + combination;
                maskToUse = maskToUse ^ indexKey;
            }
            updateMask();
            return combination;
        } else {
            throw new NoSuchElementException();
        }
    }

    private void updateMask() {
        int t = mask + 1;
        int u = t ^ mask;
        int v = t & mask;
        mask = v - (v & -v) / (u + 1);
    }
}
