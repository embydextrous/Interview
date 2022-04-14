# https://www.geeksforgeeks.org/given-1s-2s-3s-ks-print-zig-zag-way/
'''
Given number of rows and columns. And given number of 1's, 2's, 3's ……k's which needs to be printed. 
Print them in a zig-zag way. 
It is guaranteed that n*m = number of 1's + 2's + 3's + …… + k's 
Examples: 
 
Input :  2 3
         2 1 2 1
Output : 1 1 2
         4 3 3
Explanation :
Here number of rows are 2 and number of columns are 3
and number of 1's are 2
    number of 2's are 1
    number of 3's are 2
    number of 4's are 1
    -----------
   | 1 | 1 | 2 |
   | 3 | 3 | 4 |
    -----------

Input :  4 3
         2 4 3 1 2
Output : 1 1 2
         2 2 2
         3 3 3
         5 5 4
Explanation :
Here number of rows are 4 and number of columns are 3
and number of 1's are 2
    number of 2's are 4 [Note that 2s are printed in]
    number of 3's are 3 [zig zag manner]
    number of 4's are 1
    number of 5's are 2
'''
def printPattern(n, m, num):
    i, j = 0, 0
    leftToRight = True
    while n > 0:
        count = 0
        jCount = 0
        while count < m:
            jCount = min(num[j], m - count)
            count += jCount
            if count == m:
                break
            j += 1
        step = 1 if leftToRight else -1
        start = i if leftToRight else j
        end = j + 1 if leftToRight else i - 1
        for k in range(start, end, step):
            times = num[k] if k != j else jCount
            while times > 0:
                print(k + 1, end = " ")
                num[k] -= 1
                times -= 1
        if j < m and num[j] == 0:
            i = j = j + 1
        else:
            i = j
        leftToRight = not leftToRight
        print()
        n -= 1
                
n = 4
m = 5
num = [1, 0, 7, 4, 8, 0]
printPattern(n, m, num)
