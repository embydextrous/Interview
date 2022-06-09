# https://www.geeksforgeeks.org/longest-even-length-substring-sum-first-second-half/

'''
Given a string of digits, find the length of the longest substring, such that the length of the substring is 2k digits and sum of left k digits is equal to the sum of right k digits. 
Examples : 

Input: str = "123123"
Output: 6
The complete string is of even length and sum of first and second
half digits is same

Input: str = "1538023"
Output: 4
The longest substring with same first and second half sum is "5380"
'''
def findLongest(s):
    n = len(s)
    leftSum = [0] * (n + 1)
    for i in range(1, n + 1):
        leftSum[i] = leftSum[i-1] + int(s[i-1])
    length = (n // 2) * 2
    while length > 0:
        l = 0
        r = length
        while r <= n:
            m = l + (r - l) // 2
            if leftSum[r] - leftSum[l] == 2 * (leftSum[m] - leftSum[l]):
                return length
            l += 1
            r += 1
        length -= 2
    return 0

s = "12"
print(findLongest(s))
        