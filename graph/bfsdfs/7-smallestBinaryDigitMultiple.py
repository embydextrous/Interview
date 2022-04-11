'''
A decimal number is called a binary digit number if its digits are binary. For example, 102 is not a 
binary digit number and 101 is. We are given a decimal number N, we need to find the smallest multiple
of N which is a binary digit number, 
Examples:  

Input : N = 2
Output: 10
Explanation: 10 is a multiple of 2. 
              Note that 5 * 2 = 10

Input  : N = 17
Output : 11101
Explanation: 11101 is a multiple of 17. 
              Note that 653 * 17 = 11101

Recommended: Please try your approach on {IDE} first, before moving on to the s
'''
def smallestBinaryDigitMultiple(n):
    q = [1]
    while len(q) > 0:
        x = q.pop(0)
        if x % n == 0:
            return x
        q.append(10 * x + 0)
        q.append(10 * x + 1)

print(smallestBinaryDigitMultiple(13))