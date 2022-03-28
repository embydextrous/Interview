package iterators.demo;

import java.util.List;

public interface Nested<T> {
    public boolean isList();
    public T get();
    public List<Nested<T>> getList();
}