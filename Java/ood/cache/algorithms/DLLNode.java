package cache.algorithms;

public class DLLNode<T> {
    DLLNode<T> next;
    DLLNode<T> prev;
    T element;

    public DLLNode(T element) {
        this.element = element;
        this.next = null;
        this.prev = null;
    }

    public T element() {
        return element;
    }
}
