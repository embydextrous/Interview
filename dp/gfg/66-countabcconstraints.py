'''
Given a length n, count the number of strings of length n that can be made using 'a', 'b' and 'c' with at-most one 'b' and two 'c's allowed.
Examples : 
 

Input : n = 3 
Output : 19 
Below strings follow given constraints:
aaa aab aac aba abc aca acb acc baa
bac bca bcc caa cab cac cba cbc cca ccb 

Input  : n = 4
Output : 39
'''
def count(n):
    return 1 + n + (n ** 3 + n) // 2

print(count(50000))
