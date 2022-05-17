'''
Catalan numbers are a sequence of natural numbers that occurs in many interesting counting problems
like following.

1. Count the number of expressions containing n pairs of parentheses which are correctly matched. 
    For n = 3, possible expressions are ((())), ()(()), ()()(), (())(), (()()).
2. Count the number of possible Binary Search Trees with n keys.
3. Count the number of full binary trees (A rooted binary tree is full if every vertex has either two 
    children or no children) with n+1 leaves.
4. Given a number n, return the number of ways you can draw n chords in a circle with 2 x n points such 
    that no 2 chords intersect.
C(0) = 1
C(n+1) = C(0)C(n) + C(1)C(n-1).......... C(n)C(0) 
'''
def catalan(n):
    c = [0] * (n + 1)
    c[0] = 1
    for i in range(1, n + 1):
        for j in range(i):
            c[i] += c[j] * c[i-j-1]
    return c[n]

n = 5
print(catalan(4))