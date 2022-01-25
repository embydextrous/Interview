from stack import Stack

def nextGreaterElement(a):
    n = len(a)
    if n == 0:
        return []
    if n == 1:
        return [-1]
    result = [-1] * n
    s = Stack()
    s.push(0)
    for i in range(1, n):
        x = a[i]
        while not s.isEmpty() and x > a[s.peek()]:
            result[s.pop()] = x
        s.push(i)
    return result

a = [3, 8, 1, 10, 12, 11, 7, 5, 4, 9, 0]
result = nextGreaterElement(a)
print(result)

    
    