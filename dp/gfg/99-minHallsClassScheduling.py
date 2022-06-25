'''
Given N lecture timings, with their start time and end time (both inclusive), the task is to find the minimum number of halls required to hold all the 
classes such that a single hall can be used for only one lecture at a given time. Note that the maximum end time can be 105.
Examples: 
 

    Input: lectures[][] = {{0, 5}, {1, 2}, {1, 10}} 
    Output: 3 
    All lectures must be held in different halls because 
    at time instance 1 all lectures are ongoing.
    Input: lectures[][] = {{0, 5}, {1, 2}, {6, 10}} 
    Output: 2 
'''
def minHalls(lectures):
    n = len(lectures)
    aux = []
    for i in range(n):
        aux.append([lectures[i][0], 0])
        aux.append([lectures[i][1], 1])
    aux.sort(key = lambda x : [x[0], x[1]])
    numHalls = 0
    maxNumHalls = 0
    for i in range(2*n):
        if aux[i][1] == 0:
            numHalls += 1
            maxNumHalls = max(maxNumHalls, numHalls)
        else:
            numHalls -= 1
    return maxNumHalls

lectures = [[0, 5], [1, 2], [6, 10]]
print(minHalls(lectures))
