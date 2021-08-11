class Stack:
    def __init__(self, max):
        self.max = max
        self.arr = [None for i in range(self.max)]
        self.top = 0

    def push(self, ele):
        if self.top == self.max:
            print("\nStack is full\n")
            return
        self.arr[self.top] = ele
        self.top += 1

    def pop(self):
        if self.top == 0:
            print("\nStack is empty\n")
            return
        ele = self.arr[self.top-1]
        self.arr[self.top-1] = None
        self.top -=1
        return ele

