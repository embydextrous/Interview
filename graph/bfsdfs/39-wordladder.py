'''
Given a dictionary, and two words 'start' and 'target' (both of same length). Find length of the smallest chain from 'start' to 'target' if it exists, such that 
adjacent words in the chain only differ by one character and each word in the chain is a valid word i.e., it exists in the dictionary. It may be assumed that 
the 'target' word exists in dictionary and length of all dictionary words is same. 

Example: 

    Input: Dictionary = {POON, PLEE, SAME, POIE, PLEA, PLIE, POIN}, start = TOON, target = PLEA
    Output: 7
    Explanation: TOON -> POON -> POIN -> POIE -> PLIE -> PLEE -> PLEA

    Input: Dictionary = {ABCD, EBAD, EBCD, XYZA}, start = ABCV, target = EBAD
    Output: 4
    Explanation: ABCV -> ABCD -> EBCD -> EBAD
'''
from graph import UndirectedGraph
from collections import deque

def differsByOne(w1, w2):
    c = 0
    for i in range(len(w1)):
        if w1[i] != w2[i]:
            c += 1
            if c > 1:
                return False
    return c == 1


def createGraph(words):
    n = len(words)
    g = UndirectedGraph(n)
    for i in range(n):
        for j in range(i + 1, n):
            if differsByOne(words[i], words[j]):
                g.addEdge(i, j)
    g.print()
    return g

def wordLadder(words, start, target):
    words.append(start)
    n = len(words)
    g = createGraph(words)
    visited = set()
    visited.add(n-1)
    parentMap = {n-1:-1}
    q = deque([n-1])
    targetIndex = -1
    while len(q) > 0:
        u = q.popleft()
        if words[u] == target:
            targetIndex = u
            break
        for v in g.graph[u]:
            if v not in visited:
                parentMap[v] = u
                visited.add(v)
                q.append(v)
    if targetIndex == -1:
        return []
    q = deque()
    while targetIndex != -1:
        q.appendleft(words[targetIndex])
        targetIndex = parentMap[targetIndex]
    print(q)
     
    

    

words = ["POON", "PLEE", "SAME", "POIE", "PLEA", "PLIE", "POIN"]
wordLadder(words, "TOON", "PLEA")
