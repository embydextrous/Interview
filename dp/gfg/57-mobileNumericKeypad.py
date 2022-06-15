'''
Given the mobile numeric keypad. You can only press buttons that are up, left, right or down to the current button. 
You are not allowed to press bottom row corner buttons (i.e. * and # ).
 
Given a number N, find out the number of possible numbers of given length. 
Examples: 
For N=1, number of possible numbers would be 10 (0, 1, 2, 3, …., 9) 
For N=2, number of possible numbers would be 36 
Possible numbers: 00,08 11,12,14 22,21,23,25 and so on. 
If we start with 0, valid numbers will be 00, 08 (count: 2) 
If we start with 1, valid numbers will be 11, 12, 14 (count: 3) 
If we start with 2, valid numbers will be 22, 21, 23,25 (count: 4) 
If we start with 3, valid numbers will be 33, 32, 36 (count: 3) 
If we start with 4, valid numbers will be 44,41,45,47 (count: 4) 
If we start with 5, valid numbers will be 55,54,52,56,58 (count: 5) 
……………………………… 
………………………………
We need to print the count of possible numbers.

1 2 3
4 5 6
7 8 9
  0
'''
def mobileNumericKeypad(n):
    if n == 0:
        return n
    odd = [1] * 10
    even = [0] * 10
    for i in range(1, n):
        even[0] = odd[0] + odd[8]
        even[1] = odd[1] + odd[4] + odd[2]
        even[2] = odd[1] + odd[2] + odd[3] + odd[5]
        even[3] = odd[2] + odd[3] + odd[6]
        even[4] = odd[1] + odd[4] + odd[5] + odd[7]
        even[5] = odd[2] + odd[4] + odd[6] + odd[8] + odd[5]
        even[6] = odd[3] + odd[5] + odd[9] + odd[6]
        even[7] = odd[4] + odd[7] + odd[8]
        even[8] = odd[0] + odd[5] + odd[7] + odd[9] + odd[8]
        even[9] = odd[6] + odd[8] + odd[9]
        even, odd = odd, even
    print(odd)
    return sum(odd)

n = 2
print(mobileNumericKeypad(n))

