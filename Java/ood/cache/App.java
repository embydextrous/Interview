package cache;

import java.util.Random;

import cache.factories.CacheFactory;

public class App {

    public static void main(String[] args) {
        Cache<Integer, Integer> cache = new CacheFactory<Integer, Integer>().defaultCache(5);

        Random random = new Random();
        for (int i = 0; i < 20; i++) {
            int op = random.nextInt(100) % 6;
            if (op == 1) {
                int key = random.nextInt(20);
                System.out.println("Getting " + key);
                cache.get(key);
                cache.print();
            } else {
                int key = random.nextInt(20);
                int value = random.nextInt(20);
                System.out.println("Puttin " + key + ":" + value);
                cache.put(key, value);
                cache.print();
            }
        }
    }
}
