#create linked list
class Node:
  def __init__(self, val, nex = None, last = None):
    self.val = val
    self.next= nex
    self.last = last

class Linkedlist:
  def __init__(self, value = None):
      self.head = None
      self.tail = None
      # self.value = value
  def add(self, value):
    #create new node
    newNode = Node(value, nex = None)


