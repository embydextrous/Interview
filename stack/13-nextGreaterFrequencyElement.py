from stack import Stack

def nextGreaterFrequencyElement(a):
    n = len(a)
    if n == 0:
        return []
    if n == 1:
        return -1
    result = [-1] * n
    f = {x : a.count(x) for x in a}
    s = Stack()
    s.push(0)
    for i in range(1, n):
        x = a[i]
        if f[x] > f[a[s.peek()]]:
            while not s.isEmpty() and f[x] > f[a[s.peek()]]:
                result[s.pop()] = x
        s.push(i)
    return result

a = [1, 1, 2, 3, 4, 2, 1]
result = nextGreaterFrequencyElement(a)
for key in a:
    print(str(key) + ": " + str(result[key]))