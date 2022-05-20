'''
You are given a set of n types of rectangular 3-D boxes, where the i^th box has height h(i), width w(i)
and depth d(i) (all real numbers). You want to create a stack of boxes which is as tall as possible, 
but you can only stack a box on top of another box if the dimensions of the 2-D base of the lower box 
are each strictly larger than those of the 2-D base of the higher box. Of course, you can rotate a box 
so that any side functions as its base. It is also allowable to use multiple instances of the same type of box. 
'''
def boxStacking(boxes):
    allBoxes = []
    for box in boxes:
        allBoxes.append(box)
        allBoxes.append([box[0], box[2], box[1]])
        allBoxes.append([box[1], box[2], box[0]])
    allBoxes.sort(key = lambda x : x[0] * x[1])
    dp = [allBoxes[i][2] for i in range(len(allBoxes))]
    for i in range(1, len(allBoxes)):
        for j in range(i):
            if allBoxes[i][0] > allBoxes[j][0] and allBoxes[i][1] > allBoxes[j][1]:
                dp[i] = max(dp[i], dp[j] + allBoxes[i][2])
            elif allBoxes[i][1] > allBoxes[j][0] and allBoxes[i][0] > allBoxes[j][1]:
                dp[i] = max(dp[i], dp[j] + allBoxes[i][2])
    print(dp)
    return max(dp)

# [1, 2, 3], [1, 3, 2], [2, 3, 1], [4, 5, 6], [4, 6, 5], [4, 6, 7], [4, 7, 6], [5, 6, 4], [6, 7, 4]
# [10, 12, 32], [10, 32, 12], [12, 32, 10]
# [3, 2, 4, 10, 9, 11, 9, 14, 18, 50, 30, 10]
boxes = [[4, 6, 7], [1, 2, 3], [4, 5, 6], [10, 12, 32]]
print(boxStacking(boxes))