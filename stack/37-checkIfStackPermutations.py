def checkIfStackPermutation(inp, out):
    s = []
    while len(out) > 0:
        while len(inp) > 0:
            q = inp.pop(0)
            if q == out[0]:
                out.pop(0)
            else:
                s.append(q)
                break
        if len(out) == 0:
            return True
        while len(inp) > 0 and inp[0] != out[0]:
            s.append(inp.pop(0))
        s.append(inp.pop(0))
        while len(s) > 0:
            if out[0] != s[-1]:
                return False
            else:
                s.pop()
                out.pop(0)
    return len(s) == 0

inp = [1, 2, 3, 4, 5]
out = [3, 1, 2, 5, 4]

print(checkIfStackPermutation(inp, out))