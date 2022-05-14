'''
A stack permutation is a permutation of objects in the given input queue which is done by
transferring elements from input queue to the output queue with the help of a stack and 
the built-in push and pop functions

The well defined rules are: 
    Only dequeue from the input queue.
    Use inbuilt push, pop functions in the single stack.
    Stack and input queue must be empty at the end.
    Only enqueue to the output queue.

There are a huge number of permutations possible using a stack for a single input queue. 
Given two arrays, both of unique elements. One represents the input queue and the other represents the output queue. Our task is to check if the given output is possible through stack permutation.
Examples: 
 
# 
# 1 2
# 1 2

Input : First array: 1, 2, 3  
        Second array: 3, 1, 2
Output : Yes
Procedure:
push 1 from input to stack
push 2 from input to stack
pop 2 from stack to output
pop 1 from stack to output
push 3 from input to stack
pop 3 from stack to output


Input : First array: 1, 2, 3  
        Second array: 3, 1, 2
Output : Not Possible  
'''

from collections import deque


def checkIfStackPermutation(inp, out):
    s = []
    while True:
        if len(s) == 0 and len(inp) > 0:
            s.append(inp.popleft())
        elif s[-1] == out[0]:
            out.popleft()
            s.pop()
            if len(inp) == 0 and len(out) == 0:
                return True
        else:
            if len(inp) == 0:
                return False
            else:
                s.append(inp.popleft())

inp = [1, 2, 3, 4, 5, 6, 7, 8, 9]
out = [4, 2, 3, 1, 5, 6, 7, 8, 9]

print(checkIfStackPermutation(deque(inp), deque(out)))