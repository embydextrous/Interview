from dll import DoublyLinkedList, Node
from random import randint

class LRUCache:
    def __init__(self, capacity):
        self.d = {}
        self.capacity = capacity
        self.dll = DoublyLinkedList()
        self.size = 0

    def put(self, key, value):
        if key in self.d:
            # 1. write new value
            # 2. Move node to beginning of list
            dllNode = self.d[key]
            dllNode.data = (key, value) # write new value
            # Move to head if not already to make it most recently used
            if self.dll.head != dllNode:
                self.dll.delete(dllNode)
                self.dll.insertNodeBefore(self.dll.head, dllNode)
        else:
            if self.size == self.capacity:
                # Remove dll Node and remove corresponding key from map
                nodeToDelete = self.dll.tail
                self.d.pop(nodeToDelete.data[0])
                self.dll.delete(nodeToDelete)
                if self.dll.head is None:
                    self.dll.push((key, value))
                else:
                    self.dll.insertNodeBefore(self.dll.head, Node((key, value)))
                self.d[key] = self.dll.head
            else:
                # Create a node and enter into map
                # Push node into head of dll
                # Increment Size
                if self.dll.head is None:
                    self.dll.push((key, value))
                else:
                    self.dll.insertNodeBefore(self.dll.head, Node((key, value)))
                self.d[key] = self.dll.head
                self.size += 1


    def get(self, key):
        if key not in self.d:
            return None
        dllNode = self.d[key]
        kvPair = dllNode.data
        if self.dll.head != dllNode:
            self.dll.delete(dllNode)
            self.dll.insertNodeBefore(self.dll.head, dllNode)
        return kvPair[1]
    
    def print(self):
        print("Keys in cache are: " + str(self.d.keys()))
        print("DLL State: ", end = "")
        self.dll.print()

lruCache = LRUCache(5)

for i in range(25):
    op = randint(1, 100) % 4
    if op == 0:
        key = randint(1, 20)
        print("Result from cache for " + str(key) + " is " + str(lruCache.get(key)))
    else:
        key = randint(1, 20)
        value = randint(1, 20)
        print("Inserting key value pair in lruCache " + str((key, value)))
        lruCache.put(key, value)
    lruCache.print()

