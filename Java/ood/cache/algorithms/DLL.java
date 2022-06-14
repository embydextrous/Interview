package cache.algorithms;

public class DLL<T> {
    private DLLNode<T> dummyHead;
    private DLLNode<T> dummyTail;

    public DLL() {
        dummyHead = new DLLNode<T>(null);
        dummyTail = new DLLNode<T>(null);
        dummyHead.next = dummyTail;
        dummyTail.prev = dummyHead;
    }

    public void detachNode(DLLNode<T> node) {
        if (node != null) {
            node.prev.next = node.next;
            node.next.prev = node.prev;
        }
    }

    public void append(DLLNode<T> node) {
        DLLNode<T> tailPrev = dummyTail.prev;
        tailPrev.next = node;
        node.next = dummyTail;
        dummyTail.prev = node;
        node.prev = tailPrev;
    }

    public DLLNode<T> append(T element) {
        DLLNode<T> node = new DLLNode<T>(element);
        append(node);
        return node;
    }

    public boolean isEmpty() {
        return dummyHead.next == dummyTail;
    }

    public DLLNode<T> last() {
        if (isEmpty()) {
            return null;
        }
        return dummyTail.prev;
    }

    public DLLNode<T> first() {
        if (isEmpty()) {
            return null;
        }
        return dummyHead.next;
    }
}
