package iterators;

import java.util.Iterator;
import java.util.NoSuchElementException;
import java.util.Stack;

/**
 *              8
 *            /   \
 *           4     13
 *          / \    / \
 *         2   6  11  16
 *          \      \   \ 
 *           3      12   19
 *                     /
 *                    18
 */

public class BstIterator<T> implements Iterator<T> {
    private final Stack<Node<T>> stack = new Stack<>();
    private Node<T> next;

    public BstIterator(Node<T> root) {
        advanceIterator(root);
    }

    @Override
    public boolean hasNext() {
        return next != null;
    }

    @Override
    public T next() {
        if (hasNext()) {
            T value = next.data;
            advanceIterator(next.right);
            return value;
        }
        throw new NoSuchElementException();
    }

    private void advanceIterator(Node<T> current) {
        while (true) {
            if (current != null) {
                stack.push(current);
                current = current.left;
            } else {
                if (!stack.isEmpty()) {
                    next = stack.pop();
                    break;
                } else {
                    next = null;
                    break;
                }
            }
        }
    }

    static public class Node<T> {
        T data;
        public Node<T> left;
        public Node<T> right;
    
        public Node(T data) {
            this.data = data;
            this.left = null;
            this.right = null;
        }
    }
}