package cache.storage;

import cache.exceptions.CacheFullException;
import cache.exceptions.KeyNotFoundException;

public interface Store<Key, Value> {
    void put(Key key, Value value) throws CacheFullException;
    void remove(Key key) throws KeyNotFoundException;
    Value get(Key key) throws KeyNotFoundException;
    void print();
}
