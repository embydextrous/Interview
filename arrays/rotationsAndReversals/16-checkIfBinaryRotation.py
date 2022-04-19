'''
Given two positive integers x and y, check if one integer is obtained by rotating bits of other.
 

Input constraint: 0 < x, y < 2^32 

Bit Rotation: A rotation (or circular shift) is an operation similar to shift except that the bits that fall 
off at one end are put back to the other end.
More information on bit rotation can be found here
Example 1 : 
 

Input : a = 8, b = 1
Output : yes

Explanation :
Representation of a = 8 : 0000 0000 0000 0000 0000 0000 0000 1000
Representation of b = 1 : 0000 0000 0000 0000 0000 0000 0000 0001
If we rotate a by 3 units right we get b, hence answer is yes

Example 2 : 
 

Input : a = 122, b = 2147483678
Output : yes

Explanation :
Representation of a = 122        : 0000 0000 0000 0000 0000 0000 0111 1010
Representation of b = 2147483678 : 1000 0000 0000 0000 0000 0000 0001 1110
If we rotate a by 2 units right we get b, hence answer is yes
'''
def checkIfBinaryRotation(x, y):
    x = x | x << 32
    i = 0
    while i < 32:
        if x & 0xFFFFFFFF == y:
            return True
        x = x >> 1
        i += 1
    return False
    
b = 1
a = 8

print(checkIfBinaryRotation(a, b))

