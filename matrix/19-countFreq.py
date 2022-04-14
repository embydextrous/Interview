'''
Given a matrix of size n*n. Count the frequency of given element k in that matrix. Here base index is 0.
Examples: 
 
Input : n = 4, k = 7
Output : 2
Explanation
The matrix will be
0 1 2 3 
1 2 3 4 
2 3 4 5 
3 4 5 6
in the given matrix where M(i, j) = i+j, 
frequency of 5 is 2
'''
# Assuming k is non-negative
def count(n, k):
    if k > 2 * n - 2:
        return 0
    return n - abs(n - k - 1)


for i in range(0, 10):
    print(str(i) + ": ", end = " ")
    print(count(5, i))