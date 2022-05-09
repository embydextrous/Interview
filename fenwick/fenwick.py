class FenwickTree:
    def __init__(self, a):
        self.n = len(a)
        self.tree = [0 for i in range(self.n+1)]
        for i in range(self.n):
            self.update(i, a[i])

    def update(self, i, x):
        idx = i + 1
        while idx <= self.n:
            self.tree[idx] += x
            idx += idx & (-idx)

    # Returns sum from 0 to i
    def getSumFromStart(self, i):
        sum = 0
        while i != 0:
            sum += self.tree[i]
            i -= i & -i
        return sum

    # O(logn)
    def getSum(self, start, end):
        return self.getSumFromStart(end + 1) - self.getSumFromStart(start + 1)

    def __repr__(self):
        return f"{self.tree}"

'''
a = [2, 1, 1, 3, 2, 3, 4, 5, 6, 7, 8, 9]
bit = FenwickTree(a)
print(bit)
#bit.update(5, 12)
print(bit)
print(bit.getSumFromStart(6))
print(bit.getSum(3, 8))
'''