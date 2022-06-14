package cache.policy;

import java.security.Key;
import java.util.HashMap;
import java.util.Map;

import cache.algorithms.DLL;
import cache.algorithms.DLLNode;

public class LRUEvictionPolicy<Key> implements EvictionPolicy<Key> {

    private DLL<Key> dll;
    private Map<Key, DLLNode<Key>> mapper;

    public LRUEvictionPolicy() {
        this.dll = new DLL<>();
        this.mapper = new HashMap<>();
    }

    @Override
    public void onKeyAccess(Key key) {
        if (mapper.containsKey(key)) {
            dll.detachNode(mapper.get(key));
            dll.append(mapper.get(key));
        } else {
            DLLNode<Key> node = dll.append(key);
            mapper.put(key, node);
        }
    }

    @Override
    public Key evictKey() {
        DLLNode<Key> node = dll.first();
        if (node == null) {
            return null;
        }
        dll.detachNode(node);
        mapper.remove(node.element());
        return node.element();
    }
}
