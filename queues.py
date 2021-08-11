class Queue:
    def __init__(self, max):
        self.max = max
        self.arr = [None for i in range(self.max)]
        self.end = 0

    def enqueue(self, ele):
        if self.end == self.max:
            print("\nQueue is full\n")
            return
        self.arr[self.end] = ele
        self.end +=1
        return

    def dequeue(self):
        if self.end == 0:
            print("\nQueue is empty\n")
        for i in range(self.max-1):
            self.arr[i] = self.arr[i+1]
        self.arr[self.end-1] = None
        self.end -= 1


