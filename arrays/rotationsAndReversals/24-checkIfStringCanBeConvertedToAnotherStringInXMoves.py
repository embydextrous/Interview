'''
Given an integer X and two strings S1 and S2, the task is to check that string S1 can be 
converted to the string S2 by shifting characters circular clockwise atmost X times.
 
    Input: S1 = "abcd", S2 = "dddd", X = 3 
    Output: Yes 
    Explanation: 
    Given string S1 can be converted to string S2 as- 
    Character "a" - Shift 3 times - "d" 
    Character "b" - Shift 2 times - "d" 
    Character "c" - Shift 1 times - "d" 
    Character "d" - Shift 0 times - "d"
    Input: S1 = "you", S2 = "ara", X = 6 
    Output: Yes 
    Explanation: 
    Given string S1 can be converted to string S2 as - 
    Character "y" - Circular Shift 2 times - "a" 
    Character "o" - Shift 3 times - "r" 
    Character "u" - Circular Shift 6 times - "a" 
'''
D = 26

def check(s1, s2, x):
    for i in range(len(s1)):
        c1, c2 = s1[i], s2[i]
        d = min(abs(ord(c1) - ord(c2)), D - (abs(ord(c1) - ord(c2))))
        if d > x:
            return False
    return True

s1 = "abcd"
s2 = "dddd"
print(check(s1, s2, 4))