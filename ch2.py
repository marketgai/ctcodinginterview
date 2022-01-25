#create linked list
class Node:
    def __init__(self, value, next = None, last = None):
        self.value = value
        self.next= next
        self.last = last

class LinkedList:
    def __init__(self, value = None):
        self.head = Node(value)
        self.tail = Node(value)
    def printList(self):
        temp=self.head
        while (temp):
            print(temp.value)
            temp=temp.next
    def add(self, value):
        temp = self.head
        while temp.next != None:
            temp = temp.next
            #create new node
        newNode = Node(value, None, temp)
        temp.next = newNode
    def remove(self, value):
        temp = self.head
        while temp.value != value:
            temp = temp.next
        if temp.last != None:
            before = temp.last
        else:
            before = self.head
        if temp.next != None:
            after = temp.next
        else: 
            after = None
        before.next = after
        if after != None:
            after.last = before
    def removeDup(self):
        temp = self.head
        storage = set()
        while temp.next != None:
            if temp.value not in storage:
                storage.add(temp.value)
            else: 
                before = temp.last
                if temp.next != None:
                    after = temp.next
                    after.last = before
                else: 
                    after = None
                before.next = after
                print("removed", temp.value)
            temp = temp.next
        if temp.value in storage:
            before = temp.last
            before.next = None
    

    

newlist = LinkedList(0)
newlist.add(1)
newlist.add(2)
newlist.add(3)
newlist.add(4)
# newlist.printList()
newlist.remove(3)
# newlist.printList()
newlist.add(1)
newlist.add(2)
print("before")
newlist.printList()
newlist.removeDup()
print("final")
newlist.printList()


