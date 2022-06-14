package cache.factories;

import cache.Cache;
import cache.policy.LRUEvictionPolicy;
import cache.storage.HashMapBasedStore;

public class CacheFactory<Key, Value> {

    public Cache<Key, Value> defaultCache(final int capacity) {
        return new Cache<>(new LRUEvictionPolicy<Key>(), new HashMapBasedStore<Key, Value>(capacity));
    }
}
