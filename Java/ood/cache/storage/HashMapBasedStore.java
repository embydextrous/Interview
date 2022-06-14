package cache.storage;

import java.security.Key;
import java.util.HashMap;
import java.util.Map;

import cache.exceptions.CacheFullException;
import cache.exceptions.KeyNotFoundException;

public class HashMapBasedStore<Key, Value> implements Store<Key, Value> {
    Map<Key, Value> store = new HashMap<>();
    private final int capacity;

    public HashMapBasedStore(int capacity) {
        this.capacity = capacity;
    }

    @Override
    public void put(Key key, Value value) throws CacheFullException {
        if (isFull()) {
            throw new CacheFullException("Cache full while inserting " + key);
        }
        store.put(key, value);
    }

    @Override
    public void remove(Key key) throws KeyNotFoundException {
        if (!store.containsKey(key)) {
            throw new KeyNotFoundException(key + " does not exist in cache.");
        }
        store.remove(key);
    }

    @Override
    public Value get(Key key) throws KeyNotFoundException {
        if (!store.containsKey(key)) {
            throw new KeyNotFoundException(key + " does not exist in cache.");
        }
        return store.get(key);
    }

    private boolean isFull() {
        return store.size() == capacity;
    }

    @Override
    public void print() {
        System.out.println(store);
    }
}
