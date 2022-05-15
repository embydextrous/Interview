'''
There are n-pairs and therefore 2n people. everyone has one unique number ranging from 1 to 2n. 
All these 2n persons are arranged in random fashion in an Array of size 2n. We are also given who is 
partner of whom. Find the minimum number of swaps required to arrange these pairs such that all pairs 
become adjacent to each other.
Example: 

Input:
n = 3  
pairs[] = {1->3, 2->6, 4->5}  // 1 is partner of 3 and so on
arr[] = {3, 5, 6, 4, 1, 2}

Output: 2
We can get {3, 1, 5, 4, 6, 2} by swapping 5 & 6, and 6 & 1
'''
def minSwapsUtil(a, n, pairs, x, indexMap):
    if x == n - 1:
        return 0
    if pairs[a[2*x]] == a[2*x+1]:
        return minSwapsUtil(a, n, pairs, x + 1, indexMap)
    i, j = indexMap[pairs[a[2*x]]], indexMap[pairs[a[2*x+1]]]
    a[i], a[2*x+1] = a[2*x+1], a[i]
    f1 = 1 + minSwapsUtil(a, n, pairs, x + 1, indexMap)
    a[i], a[2*x+1] = a[2*x+1], a[i]
    a[j], a[2*x] = a[2*x], a[j]
    f2 = 1 + minSwapsUtil(a, n, pairs, x + 1, indexMap)
    a[j], a[2*x] = a[2*x], a[j]
    return min(f1, f2)

def minSwaps(a, n, pairs):
    for (k, v) in pairs.copy().items():
        pairs[v] = k
    indexMap = {}
    for i in range(len(a)):
        indexMap[a[i]] = i
    return minSwapsUtil(a, n, pairs, 0, indexMap)

a = [9, 1, 7, 0, 4, 6, 2, 8, 5, 3]
pairs = {3:5, 9:1, 4:6, 2:8, 7:0}
n = 5
print(minSwaps(a, n, pairs))


    
    