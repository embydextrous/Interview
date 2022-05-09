'''
Given an undirected connected tree with N nodes (and N-1 edges), we need to find two paths in this 
tree such that they are non-intersecting and the product of their length is maximum. 

Examples: 

        1 -- 2 -- 3 -- 4

In above tree two paths which are non-intersecting
and have highest product are, 1-2 and 3-4, so answer
is 1*1 = 1

6 -- 5 -- 1 -- 3 -- 4 -- 8 -- 9
               |
               7
               |
               0 -- 2

In above tree two paths which are non-intersecting 
and has highest product are, 0-2-4  and  6-7-5-1 
(or 3-7-5-1), so answer is 3*2 = 6

Maximum product of two non-intersecting paths in a tree
'''
# Gives max len path in tree rooted at u ignoring edge between u and v
def maxLenPath(g, u, v, curMax):
    max1 = 0
    max2 = 0
    total = 0
    for i in g[u]:
        if i != v:
            # Necessary because a longer path may exist that may not contain root, have to preserve its length
            total = max(total, maxLenPath(g, i, u, curMax))
            # we need to find two max depths whose sum will be maxPathLen including u
            if (curMax[0] > max1):
                max2 = max1 
                max1 = curMax[0]
            else:
                max2 = max(max2, curMax[0])
    # Necessary because a longer path may exist that may not contain root, have to preserve its length
    # Can be ignored if u is to be included in the path
    total = max(total, max1 + max2)
    # this basically gives the current maxDepth
    curMax[0] = max1 + 1
    return total

def maxProduct(edges):
    V = len(edges) + 1
    g = { i : [] for i in range(V) }
    result = 0
    for (u, v) in edges:
        g[u].append(v)
        g[v].append(u)
    for (u, v) in edges:
        curMax = [0]
        maxPath1 = maxLenPath(g, u, v, curMax)
        curMax = [0]
        maxPath2 = maxLenPath(g, v, u, curMax)
        result = max(result, maxPath1 * maxPath2)
        print(u, v, maxPath1, maxPath2)
    return result

edges = [[0, 7], [1, 5], [2, 0], [4, 2], [6, 7], [7, 3], [7, 5]]
edges = [[0, 7], [0, 2], [1, 3], [1, 5], [3, 4], [3, 7], [4, 8], [5, 6], [8, 9]]
print(maxProduct(edges))
