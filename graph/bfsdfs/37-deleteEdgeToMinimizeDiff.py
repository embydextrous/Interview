'''
Given an undirected tree whose each node is associated with a weight. We need to delete an edge in such a 
way that difference between sum of weight in one subtree to sum of weight in other subtree is minimized.

        2 -- 4
           /   \
          1     6
        /   \    \
       3     5    2
'''
# calculates sum of subtree at u after deleting its edge with parent
def dfs(g, parent, u, totalSum, subtree, res):
    sum = subtree[u]
    for v in g[u]:
        if v != parent:
            dfs(g, u, v, totalSum, subtree, res)
            sum += subtree[v]
    subtree[u] = sum
    # one side sum comes sum, otherside sum is total - sum, diff is total - 2 * sum
    # not doing this for u as its parent is -1 so there is no edge deletion
    if u != 0 and abs(totalSum - 2 * sum) < res[0]:
        res[0] = abs(totalSum - 2 * sum)

def getMinSubtreeDiff(vertex, edges): 
    n = len(vertex)
    totalSum = 0
    subtree = [None] * n
    for i in range(n): 
        subtree[i] = vertex[i] 
        totalSum += vertex[i] 
    g = {x : [] for x in range(n)}
    for edge in edges: 
        (u, v) = edge
        g[u].append(v)
        g[v].append(u)  
    res = [10 ** 9] 
    dfs(g, -1, 0, totalSum, subtree, res) 
    return res[0] 

vertex = [4, 2, 1, 6, 3, 5, 2] 
edges = [[0, 1], [0, 2], [0, 3], [2, 4], [2, 5], [3, 6]] 
print(getMinSubtreeDiff(vertex, edges)) 