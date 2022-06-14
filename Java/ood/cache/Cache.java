package cache;

import cache.exceptions.CacheFullException;
import cache.exceptions.KeyNotFoundException;
import cache.policy.EvictionPolicy;
import cache.storage.Store;

public class Cache<Key, Value> {
    
    private final EvictionPolicy<Key> evictionPolicy;
    private final Store<Key, Value> store;
    
    public Cache(EvictionPolicy<Key> evictionPolicy, Store<Key, Value> store) {
        this.evictionPolicy = evictionPolicy;
        this.store = store;
    }

    public void put(Key key, Value value) {
        try {
            this.store.put(key, value);
            evictionPolicy.onKeyAccess(key);
        } catch(CacheFullException e) {
            Key toRemove = evictionPolicy.evictKey();
            if (toRemove == null) {
                throw new IllegalStateException("Storage Full and no keys to evict.");
            }
            store.remove(toRemove);
            put(key, value);
        }
    }
    
    public Value get(Key key) {
        try {
            Value value = store.get(key);
            evictionPolicy.onKeyAccess(key);
            return value;
        } catch (KeyNotFoundException e) {
            return null;
        }
    }

    public void print() {
        store.print();
    }
}
