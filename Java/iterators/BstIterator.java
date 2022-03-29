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

public class BstIterator implements Iterator<Integer> {
    private final Stack<Node> stack = new Stack<>();
    private Node next;

    public BstIterator(Node root) {
        locateNext(root);
    }
    
    @Override
    public boolean hasNext() {
        return next != null;
    }

    @Override
    public Integer next() throws NoSuchElementException {
        if (hasNext()) {
            Integer value = next.data;
            Node temp = next;
            next = null;
            locateNext(temp.right);
            return value;
        } else {
            throw new NoSuchElementException();
        }
    }

    private void locateNext(Node current) {
        if (next != null) {
            return;
        }
        while(true) {
            if (current != null) {
                stack.push(current);
                current = current.left;
            } else {
                if (!stack.isEmpty()) {
                    next = stack.pop();
                }
                break;
            }
        }
    }

    static public class Node {
        public int data;
        public Node left;
        public Node right;

        public Node(int data) {
            this.data = data;
        }
    }
}