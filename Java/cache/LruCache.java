package cache;

import java.util.HashMap;
import java.util.LinkedList;
import java.util.Map;

public class LruCache<K, V> implements Cache<K, V> {
    private final int capacity;
    private LinkedList<CacheElement<K, V>> list = new LinkedList<>();
    private Map<K, CacheElement<K, V>> nodeMap = new HashMap<>();

    public LruCache(int capacity) {
        this.capacity = capacity;
    }

    @Override
    public void put(K key, V value) {
        if (nodeMap.containsKey(key)) {
            CacheElement<K, V> cacheElement = nodeMap.get(key);
            cacheElement.setValue(value);
            list.remove(cacheElement);
            list.addFirst(cacheElement);
        } else {
            CacheElement<K, V> newCacheElement = new CacheElement<>(key, value);
            if (list.size() == capacity) {
                CacheElement<K, V> cacheElement = list.removeLast();
                nodeMap.remove(cacheElement.getKey());   
            } 
            list.addFirst(newCacheElement);
            nodeMap.put(key, newCacheElement);
        }
    }

    @Override
    public V get(K key) {
        if (!nodeMap.containsKey(key)) {
            return null;
        }
        CacheElement<K, V> cacheElement = nodeMap.get(key);
        list.remove(cacheElement);
        list.addFirst(cacheElement);
        return cacheElement.getValue();
    }

    @Override
    public void print() {
        for(CacheElement<K, V> cacheElement : list) {
            System.out.println(cacheElement);
        }
    }
}
