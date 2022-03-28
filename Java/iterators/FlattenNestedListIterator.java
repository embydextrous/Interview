package iterators;

import java.util.Iterator;
import iterators.demo.Nested;
import java.util.List;
import java.util.NoSuchElementException;
import java.util.Stack;

public class FlattenNestedListIterator<T> implements Iterator<T> {
    private final Stack<Nested<T>> stack = new Stack<>();   

    public FlattenNestedListIterator(List<Nested<T>> nestedList) {
        for(int i = nestedList.size() - 1; i >= 0; i--) {
            stack.push(nestedList.get(i));
        }
        prepareStack();
    }

    @Override
    public boolean hasNext() {
        return !stack.isEmpty() && !stack.peek().isList();
    }

    @Override
    public T next() throws NoSuchElementException {
        if (hasNext()) {
            T next = stack.pop().get();
            prepareStack();
            return next;
        } else {
            throw new NoSuchElementException();
        }
    }

    private void prepareStack() {
        while(!stack.empty() && stack.peek().isList()) {
            List<Nested<T>> nestedList = stack.pop().getList();
            for(int i = nestedList.size() - 1; i >= 0; i--) {
                stack.push(nestedList.get(i));
            }
        }
    }
}

