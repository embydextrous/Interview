# Assuming all urls start with https://
# Assuming url may contain lower case chars, ., / and -

from dll import DoublyLinkedList, Node

class TrieNode:
    def __init__(self):
        self.children = [None] * 29
        self.data = None
        self.state = 0

    def __str__(self) -> str:
        return f"{self.children}"

def charToIndex(c):
    if c == '.':
        return 26
    if c == '/':
        return 27
    if c == '-':
        return 28
    return ord(c) - ord('a')

def insert(url, p, dll):
    for c in url:
        index = charToIndex(c)
        if p.children[index] is None:
            p.children[index] = TrieNode()
        p = p.children[index]
    # Url already exists, need to remove from dll
    if p.data:
        if p.state == 0:
            dll.delete(p.data)
            p.state = 1
    else:
        dll.push(url)
        p.data = dll.head

def findLastUniqueUrl(urls):
    dll = DoublyLinkedList()
    root = TrieNode()
    for url in urls:
        insert(url, root, dll)
    if dll.head:
        return dll.head.data
    return None

urls = [
        "https://www.geeksforgeeks.org",
        "https://write.geeksforgeeks.org",
        "http://quiz.geeksforgeeks.org",
        "http://qa.geeksforgeeks.org",
        "https://practice.geeksforgeeks.org",
        "https://ide.geeksforgeeks.org",
        "http://quiz.geeksforgeeks.org",
        "https://practice.geeksforgeeks.org",
        "https://ide.geeksforgeeks.org",
        "http://quiz.geeksforgeeks.org",
        "http://qa.geeksforgeeks.org",
        "https://practice.geeksforgeeks.org"
]

print(findLastUniqueUrl(urls))