'''
Given a sorted dictionary (array of words) of an alien language, find order of characters in the language.

Examples:  

Input:  words[] = {"baa", "abcd", "abca", "cab", "cad"}
Output: Order of characters is 'b', 'd', 'a', 'c'
Note that words are sorted and in the given language "baa" 
comes before "abcd", therefore 'b' is before 'a' in output.
Similarly we can find other orders.

Input:  words[] = {"caa", "aaa", "aab"}
Output: Order of characters is 'c', 'a', 'b'
'''
from collections import deque, defaultdict

def getEdge(w1, w2):
    n1 = len(w1)
    n2 = len(w2)
    for i in range(min(n1, n2)):
        if w1[i] != w2[i]:
            return (w1[i], w2[i])
    return None

def dfs(g, u, ts, visited):
    visited.add(u)
    for v in g[u]:
        if v not in visited:
            dfs(g, v, ts, visited)
    ts.appendleft(u)

def topologicalOrder(g):
    ts = deque()
    visited = set()
    for u in g:
        if u not in visited:
            dfs(g, u, ts, visited)
    return ts

# If invalid input this can give wrong answer,
def findAlphabetOrder(words, alphabetSize):
    n = len(words)
    g = defaultdict(set)
    for i in range(n-1):
        edge = getEdge(words[i], words[i + 1])
        if edge != None:
            u, v = edge
            if u in g[v]:
                return "Cannot Determine Order"
            g[u].add(v)
            g[v]
    topo = topologicalOrder(g)
    if len(topo) != alphabetSize:
        return "Cannot Determine"
    n = len(topo)
    for i in range(n - 1):
        if topo[i+1] not in g[topo[i]]:
            return "Cannot Determine"
    return topo

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def findAlphabeticalOrder2(words, alphabetSize):
    nodeMap = { chr(ord('a') + i) : Node(chr(ord('a') + i)) for i in range(alphabetSize) }
    letters = set(nodeMap.keys())
    for i in range(len(words) - 1):
        edge = getEdge(words[i], words[i + 1])
        if edge != None:
            u, v = edge
            nodeMap[u].next = nodeMap[v]
            if v in letters:
                letters.remove(v)
    if len(letters) != 1:
        return "Cannot Determine Order"
    order = []
    current = nodeMap[letters.pop()]
    while current:
        order.append(current.data)
        current = current.next
    if len(order) != alphabetSize:
        return "Cannot Determine Order"
    return order

words = ["ab", "ba", "abb"]
print(findAlphabetOrder(words, 2))



