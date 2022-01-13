class TwoStacks:
    def __init__(self, size):
        self.arr = [None] * size
        self.size = size
        self.topLeft = -1
        self.topRight = size

    def push1(self, data):
        if self.topLeft < self.topRight - 1:
            self.topLeft += 1
            self.arr[self.topLeft] = data
        else:
            print("Stack Overflow")
            exit(1)

    def push2(self, data):
        if self.topLeft < self.topRight - 1:
            self.topRight -= 1
            self.arr[self.topRight] = data
        else:
            print("Stack Overflow")
            exit(1)

    def pop1(self):
        if self.topLeft >= 0:
            result = self.arr[self.topLeft]
            self.arr[self.topLeft] = None
            self.topLeft -= 1
            return result
        else:
            print("Stack Underflow")
            exit(1)

    def pop2(self):
        if self.topRight < self.size:
            result = self.arr[self.topRight]
            self.arr[self.topRight] = None
            self.topRight += 1
            return result
        else:
            print("Stack Underflow")
            exit(1)

ts = TwoStacks(5)
ts.push1(5)
ts.push2(10)
ts.push2(15)
ts.push1(11)
ts.push2(7)
 
print("Popped element from stack1 is " + str(ts.pop1()))
ts.push2(40)
print("Popped element from stack2 is " + str(ts.pop2()))
ts.push1(8)
ts.push1(16)