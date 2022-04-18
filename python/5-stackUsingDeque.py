from collections import deque

class Stack:
    def __init__(self):
        self._items = deque()

    def push(self, item):
        self._items.append(item)

    def pop(self):
        try:
            return self._items.pop()
        except IndexError:
            raise IndexError("dequeue from an empty queue") from None

    def peek(self):
        return self._items[-1] if len(self) > 0 else None

    def __len__(self):
        return len(self._items)

    def __contains__(self, item):
        return item in self._items

    def __iter__(self):
        yield from self._items

    def __reversed__(self):
        yield from reversed(self._items)

    def __repr__(self):
        return f"Queue({list(self._items)})"