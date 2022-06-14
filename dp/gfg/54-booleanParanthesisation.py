'''
Given a boolean expression with following symbols. 

Symbols
    'T' ---> true 
    'F' ---> false 

And following operators filled between symbols 

Operators
    &   ---> boolean AND
    |   ---> boolean OR
    ^   ---> boolean XOR 

Count the number of ways we can parenthesize the expression so that the value of expression evaluates to true. 
Let the input be in form of two arrays one contains the symbols (T and F) in order and the other contains operators (&, | and ^}

Examples: 

Input: symbol[]    = {T, F, T}
       operator[]  = {^, &}
Output: 2
The given expression is "T ^ F & T", it evaluates true
in two ways "((T ^ F) & T)" and "(T ^ (F & T))"

Input: symbol[]    = {T, F, F}
       operator[]  = {^, |}
Output: 2
The given expression is "T ^ F | F", it evaluates true
in two ways "( (T ^ F) | F )" and "( T ^ (F | F) )". 

Input: symbol[]    = {T, T, F, T}
       operator[]  = {|, &, ^}
Output: 4
The given expression is "T | T & F ^ T", it evaluates true
in 4 ways ((T|T)&(F^T)), (T|(T&(F^T))), (((T|T)&F)^T) 
and (T|((T&F)^T))
'''
def booleanParanthesisation(values, operators):
    n = len(values)
    T = [[0 for i in range(n)] for j in range(n)]
    F = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        if values[i]:
            T[i][i] = 1
        else:
            F[i][i] = 1
    for size in range(2, n+1):
        for i in range(n - size + 1):
            j = i + size - 1
            for m in range(i, j):
                op = operators[m]
                if op == '|':
                    T[i][j] += T[i][m] * T[m+1][j] + F[i][m] * T[m+1][j] + T[i][m] * F[m+1][j]
                    F[i][j] += F[i][m] * F[m+1][j]
                elif op == '&':
                    T[i][j] += T[i][m] * T[m+1][j]
                    F[i][j] += F[i][m] * F[m+1][j] + F[i][m] * T[m+1][j] + T[i][m] * F[m+1][j]
                else:
                    F[i][j] += T[i][m] * T[m+1][j] + F[i][m] * F[m+1][j]
                    T[i][j] += F[i][m] * T[m+1][j] + T[i][m] * F[m+1][j]
    return T[0][n-1]

'''
i = 0
j = 1
m = 0
T
1 0 0
0 0 0
0 0 1  

F
0 0 0
0 1 0
0 0 0  
'''
values = [True, True, False, True]
operators = ['|', '&', '^']
print(booleanParanthesisation(values, operators))
