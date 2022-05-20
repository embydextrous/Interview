package iterators.demo;

import iterators.BstIterator;
import iterators.BstIterator.Node;

/**
 *              8
 *            /   \
 *           4     13
 *          / \    / \
 *         2   6  11  16
 *          \      \   \ 
 *           3      12  19
 *                     /
 *                    18
 */

public class BstIteratorDemo {
    public static void main(String[] args) {
        Node<Integer> root = new Node<>(8); 
        root.left = new Node<>(4);
        root.right = new Node<>(13);
        root.left.left = new Node<>(2);
        root.left.right = new Node<>(6);
        root.right.left = new Node<>(11);
        root.right.right = new Node<>(16);
        root.left.left.right = new Node<>(3);
        root.right.left.right = new Node<>(12);
        root.right.right.right = new Node<>(19);
        root.right.right.right.left = new Node<>(18);

        BstIterator<Integer> iterator = new BstIterator<>(root);
        while(iterator.hasNext()) {
            System.out.println(iterator.next());
        }
    }
}
