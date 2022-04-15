# https://www.geeksforgeeks.org/direction-last-square-block/

'''
Given a R x C (1 <= R, C <= 1000000000) grid and initial position as top left corner and direction as east. 
Now we start running in forward direction and cross each square blocks of matrix. 
Whenever we find dead end or reach a cell that is already visited, we take right because we can not cross the 
visited square blocks again. Tell the direction when we will be at last square block.
For example : Consider the case with R = 3, C = 3. 
The path followed will be (0, 0) — (0, 1) — (0, 2) — (1, 2) — (2, 2) — (2, 1) — (2, 0) — (1, 0) — (1, 1). 
At this point, all squares have been visited, and is facing right. 
Examples : 
 

Input  :  R = 1, C = 1
Output :  Right

Input   :  R = 2, C = 2
Output  :  Left

Input   :  R = 3, C = 1
Output  :  Down

Input  :  R = 3, C = 3
Output :  Right
'''

# Observation
# R == C, R is even -> Direction at last block is "left"
# R == C, R is odd, -> Direction at last block is "right"
# R != C, R < C, R is even, Direction at last block is "left"
# R != C, R < C, R is odd, Direction at last block is "right"
# R != C, R > C, C is even, Direction at last block is "up"
# R != C, R > C, C is odd, Direction at last block is "down"

def findDirection(R, C):
    if R <= C:
        if R % 2 == 0:
            return "Left"
        else:
            return "Right"
    else:
        if C % 2 == 0:
            return "Up"
        else:
            return "Down"

R, C = 3, 3
print(findDirection(R, C))