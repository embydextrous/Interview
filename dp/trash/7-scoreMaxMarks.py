'''
Given three integer n, h and p where n is the number of topics, h is the time left (in hours) and p is the passing marks. Also given two arrays marks[] and time[] 
where marks[i] is the marks for the ith topic and time[i] is the time required to learn the ith topic. The task is to find the maximum marks that can be obtained by 
studying maximum number of topics.
Examples: 
 

    Input: n = 4, h = 10, p = 10, marks[] = {6, 4, 2, 8}, time[] = {4, 6, 2, 7} 
    Output: 10 
    Either the topics with marks marks[2] and marks[3] 
    can be prepared or marks[0] and marks[1] can be prepared 
    Both cases will lead to 10 marks in total 
    which are equal to the passing marks.
    Input: n = 5, h = 40, p = 21, marks[] = {10, 10, 10, 10, 3}, time[] = {12, 16, 20, 24, 8} 
    Output: 36 
'''
def maxMarks(H, marks, time):
    n = len(marks)
    dp = [[0 for i in range(H+1)] for j in range(n+1)]
    for i in range(1, n+1):
        t = time[i-1]
        m = marks[i-1]
        for j in range(1, H + 1):
            if j < t:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j], m + dp[i-1][j-t])
    return dp[n][H]

H = 10
marks = [6, 4, 2, 8]
time = [4, 6, 2, 7]
print(maxMarks(H, marks, time))


H = 40
marks = [10, 10, 10, 10, 3]
time = [12, 16, 20, 24, 8]
print(maxMarks(H, marks, time))
