package cache.policy;

public interface EvictionPolicy<Key> {
    void onKeyAccess(Key key);
    Key evictKey();
}
