from matrix import printS

def findDistinctCommonElements(m):
    resultSet = set()
    firstRowSet = None
    for i in range(len(m)):
        if i == 0:
            firstRowSet = set(m[i])
        else:
            for key in m[i]:
                if key in firstRowSet:
                    resultSet.add(key)
            firstRowSet = resultSet
            resultSet = set()
    return firstRowSet

mat = [[2, 1, 4, 3],
       [1, 2, 3, 2],
       [3, 6, 2, 3],
       [5, 2, 5, 3]]
 
print(findDistinctCommonElements(mat))