package iterators.revision;

import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.HashMap;
import java.util.Iterator;
import java.util.List;
import java.util.ListIterator;
import java.util.Map;
import java.util.NoSuchElementException;
import java.util.Queue;
import java.util.Stack;

import iterators.PeekingIterator;
import iterators.demo.Nested;
/*
            7
          /   \
         3     12
        / \    /
       1   5  8
          /    \
         4      11
*/
public class Revision {
    public static void main(String[] args) {
        Nested<Integer> n1 = new GenericNested<>(12);
        
        Nested<Integer> n21 = new GenericNested<>(8);
        
        Nested<Integer> n221 = new GenericNested(17);
        Nested<Integer> n222 = new GenericNested(19);
        Nested<Integer> n22 = new GenericNested<>(n221, n222);
       
        Nested<Integer> n23 = new GenericNested<>(9);
        
        Nested<Integer> n241 = new GenericNested<>(3);
        Nested<Integer> n242 = new GenericNested<>(1);
        Nested<Integer> n243 = new GenericNested<>(16);
        
        Nested<Integer> n24 = new GenericNested<>(n241, n242, n243);
        
        Nested<Integer> n2 = new GenericNested<>(n21, n22, n23, n24);
        
        Nested<Integer> n311 = new GenericNested<>(18);
        Nested<Integer> n31 = new GenericNested<>(n311);
        
        Nested<Integer> n32 = new GenericNested<>(14);
        
        Nested<Integer> n331 = new GenericNested<>(11);
        Nested<Integer> n332 = new GenericNested<>(6);
        Nested<Integer> n333 = new GenericNested<>(9);
        Nested<Integer> n33 = new GenericNested<>(n331, n332, n333);
        
        Nested<Integer> n3 = new GenericNested<>(n31, n32, n33);
        
        Nested<Integer> n41 = new GenericNested<>(Collections.emptyList());
        Nested<Integer> n4 = new GenericNested<>(n41);
        
        Nested<Integer> n5 = new GenericNested<>(21);

        List<Nested<Integer>> nestedList = new ArrayList<>();
        nestedList.add(n1);
        nestedList.add(n2);
        nestedList.add(n3);
        nestedList.add(n4);
        nestedList.add(n5);

        FlattenNestedListIterator<Integer> iterator = new FlattenNestedListIterator<>(nestedList);
        while(iterator.hasNext()) {
            System.out.println(iterator.next());
        }
    }
}

class FlattenNestedListIterator<T> implements Iterator<T> {
    private Stack<Nested<T>> stack;

    FlattenNestedListIterator(List<Nested<T>> nesteds) {
        stack = new Stack<>();
        ListIterator<Nested<T>> iterator = nesteds.listIterator(nesteds.size());
        while (iterator.hasPrevious()) {
            stack.push(iterator.previous());
        }
        prepareStack();
    }

    @Override
    public boolean hasNext() {
        return !stack.isEmpty();
    }

    @Override
    public T next() {
        if (hasNext()) {
            T next = stack.pop().get();
            prepareStack();
            return next;
        }
        throw new NoSuchElementException();
    }

    /**
     * /*
    * , 17, 19, 9, [3, 1, 16], [[18], 14, [11, 6, 9]], [[]], 21
    */
    public void prepareStack() {
        while(!stack.isEmpty() && stack.peek().isList()) {
            Nested<T> n1 = stack.pop();
            ListIterator<Nested<T>> iterator = n1.getList().listIterator(n1.getList().size());
            while (iterator.hasPrevious()) {
                stack.push(iterator.previous());
            }
        }
    }
}

class GenericNested<T> implements Nested<T> {
    private final T value;
    private final List<Nested<T>> list;

    public GenericNested(T value) throws IllegalArgumentException {
        if (value == null) {
            throw new IllegalArgumentException();
        }
        this.value = value;
        this.list = null;
    }

    public GenericNested(List<Nested<T>> list) {
        if (list == null) {
            this.list = new ArrayList<>();
        } else {
            this.list = list;
        }
        this.value = null;
    }

    public GenericNested(Nested<T>... nesteds) {
        this.list = Arrays.asList(nesteds);
        this.value = null;
    }
    
    @Override
    public boolean isList() {
        return value == null;
    }
    @Override
    public T get() {
        return value;
    }
    @Override
    public List<Nested<T>> getList() {
        return list;
    }
}

