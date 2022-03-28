package cache;

import java.util.Random;

public class LruCacheDemo {
    public static void main(String[] args) {
        Random random = new Random();
        LruCache<Integer, Integer> cache = new LruCache<>(4);
        random.nextInt(10);
        for (int i = 0; i < 20; i++) {
            int operationChooser = random.nextInt(10) % 4;
            if (operationChooser == 0) {
                int key = random.nextInt(10);
                int value = random.nextInt(100);
                cache.put(key, value);
                System.out.println("Putting key: " + key + ", value: " + value);
            } else {
                int key = random.nextInt(10);
                Integer value = cache.get(key);
                System.out.println("Getting value: " + value + ", for key: " + key);
            }
            cache.print();
            System.out.println();
        }
    }
}
