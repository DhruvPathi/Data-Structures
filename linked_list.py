class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insertAtBegining(self,data):
        node = Node(data, self.head)
        self.head = node

    def insertAtEnd(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None)

    def print(self):
        itr = self.head
        output = ""
        if itr is None:
            print("\nLinked List is empty\n")
            return
        while itr:
            output += str(itr.data) + "-->"
            itr = itr.next
        print(output)

    def getLength(self):
        count = 0
        itr = self.head
        while itr:
            itr = itr.next
            count += 1
        return count

    def removeAt(self, index):
        if index < 0 or index > self.getLength():
            print("\nInvalid Index \n")
            return
        
        if index == 0:
            self.head = self.head.next
            return

        itr = self.head
        for i in range(index-1):
            itr = itr.next
        itr.next = itr.next.next
    
    def insertAt(self,index, data):
        if index > self.getLength() or index < 0:
            print("\nInvalid Index\n")
            return

        if index == 0:
            self.insertAtBegining(data)
            return

        itr = self.head
        for i in range(index-1):
            itr = itr.next
        node = Node(data, itr.next)
        itr.next = node

    def insertAfterValue(self, data, value):
        if self.head is None:
            return

        itr = self.head
        while itr:
            if itr.data == value:
                node = Node(data, itr.next)
                itr.next = node
                return
            itr = itr.next

        print("\nValue Not Found\n")
        return

    def removeByValue(self, value):
        if self.head is None:
            return

        if self.head.data == value:
            self.head = self.head.next
            return

        itr = self.head
        while itr:
            if itr.next.data == value:
                itr.next = itr.next.next
                return
            itr = itr.next
            
        print("\nValue Not Found\n")
        return

ll = LinkedList()

ll.insertAtEnd(73)
ll.insertAtEnd(49)
ll.insertAtEnd(58)
ll.insertAtEnd(78)
ll.insertAtEnd(83)
ll.insertAtEnd(72)
ll.insertAtEnd(94)
ll.removeByValue(73)
ll.print()
