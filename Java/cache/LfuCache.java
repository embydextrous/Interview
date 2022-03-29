package cache;

import java.util.HashMap;
import java.util.LinkedList;
import java.util.Map;

public class LfuCache<K, V> implements Cache<K, V> {
    private final int capacity;
    private final Map<K, CacheElement<K, V>> nodeMap = new HashMap<>();
    private final Map<K, Integer> countMap = new HashMap<>();
    private final Map<Integer, LinkedList<CacheElement<K, V>>> countLists = new HashMap<>();
    private int currentMin = 0;
    private int size = 0;

    public LfuCache(int capacity) {
        this.capacity = capacity;
    }

    @Override
    public void put(K key, V value) {
        if (nodeMap.containsKey(key)) {
            CacheElement<K, V> existingCacheElement = nodeMap.get(key);
            existingCacheElement.setValue(value);
            handleExistingCacheElement(existingCacheElement);
        } else {
            CacheElement<K, V> newCacheElement = new CacheElement<K, V>(key, value);
            countMap.put(key, 1);
            nodeMap.put(key, newCacheElement);
            if (size == capacity) {
                if (currentMin == 1) {
                    countLists.get(1).removeLast();
                    countLists.get(1).addFirst(newCacheElement);
                } else {
                    if (countLists.get(currentMin).size() == 1) {
                        countLists.remove(currentMin);
                    } else {
                        countLists.get(currentMin).removeLast();
                    }
                    currentMin = 1;
                    createNewCountListForCount(1, newCacheElement);
                }
            } else {
                size += 1;
                if (countLists.containsKey(1)) {
                    countLists.get(1).addFirst(newCacheElement);
                } else {
                    createNewCountListForCount(1, newCacheElement);
                    currentMin = 1;
                }
            }
        }
    }

    private void createNewCountListForCount(int count, CacheElement<K, V> cacheElement) {
        LinkedList<CacheElement<K, V>> newCountList = new LinkedList<>();
        newCountList.add(cacheElement);
        countLists.put(count, newCountList);
    }

    @Override
    public V get(K key) {
        if (!nodeMap.containsKey(key)) {
            return null;
        }
        CacheElement<K, V> existingCacheElement = nodeMap.get(key);
        handleExistingCacheElement(existingCacheElement);
        return existingCacheElement.getValue();
    }

    private void handleExistingCacheElement(CacheElement<K, V> existingCacheElement) {
        K key = existingCacheElement.getKey();
        int count = countMap.get(key);
        countLists.get(count).remove(existingCacheElement);
        if (countLists.get(count).isEmpty()) {
            countLists.remove(count);
            if (count == currentMin) {
                currentMin = count + 1;
            }
        }
        countMap.put(key, count + 1);
        if (countLists.containsKey(count + 1)) {
            countLists.get(count + 1).addFirst(existingCacheElement);
        } else {
            createNewCountListForCount(count + 1, existingCacheElement);
        }
    }

    @Override
    public void print() {
       System.out.println(nodeMap);
       System.out.println(countMap);
       System.out.println(currentMin);
       for(Integer key : countLists.keySet()) {
            System.out.println("Key " + key + ": " + countLists.get(key));
       }
       System.out.println();
    }
}
