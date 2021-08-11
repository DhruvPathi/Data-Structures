class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insertNode(self, data):
        if data == self.data:
            return
        
        if data < self.data:
            if self.left:
                self.left.insertNode(data)
                return
            else:
                self.left = Node(data)
                return
        if data > self.data:
            if self.right:
                self.right.insertNode(data)
                return
            else:
                self.right = Node(data)
    '''
    def delete(self, val):
        if val < self.data:
            self.left = self.left.delete(val)
        elif val > self.data:
            self.right = self.right.delete(val)
        else:
            if self.right is None and self.left is None:
                return None
            if self.right is None:
                return self.left
            if self.left is None:
                return self.right

            min = self.right.findMin()
            self.data = min
            self.right = self.right.delete(min)
        return self
    '''




    def inOrderTraversal(self):
        elements = []
        if self.left:
            elements += self.left.inOrderTraversal()

        elements.append(self.data)
        
        if self.right:
            elements += self.right.inOrderTraversal()

        return elements
    
    def search(self, ele):
        if self.data == ele:
            return True
        
        if self.data > ele:
            if self.left:
                return self.left.search(ele)
    
            else:
                return False
            
        if self.data < ele:
            if self.right:
                return self.right.search(ele)
                
            else:
                return False
    
    def findMax(self):
        if self.right == None:
            return self.data
        return self.right.findMax()

    def findMin(self):
        if self.left == None:
            return self.data
        return self.left.findMin()
    
    def delete(self, val):
        if val < self.data:
            self.left = self.left.delete(val)
        elif val > self.data:
            self.right = self.right.delete(val)
        else:
            if self.right is None and self.left is None:
                return None
            if self.right is None:
                return self.left
            if self.left is None:
                return self.right
            max = self.left.findMax()
            self.data = max
            self.left = self.left.delete(max)
        return self


def buildTree(elements):
    root = Node(elements[0])
    for i in range(1,len(elements)):
        root.insertNode(elements[i])
    return root


root = buildTree([10,5,20,2,7,15,25])
print(root.inOrderTraversal())
root.delete(11)
print(root.inOrderTraversal()) 