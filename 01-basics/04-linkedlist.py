class Node:
  def __init__(self, data):
    self.next = None
    self.data = data

class LinkedList:
  def __init__(self):
    self.head = None
    self.tail = None
  
  def push(self, data):
    node = Node(data)
    
    if self.head is None :
      self.head = self.tail = node
    
    else:
      self.tail.next = node
      self.tail = node
  
  def pop(self):
    cur = self.head
    prev = cur
    
    if cur is None:
      return

    if cur.next is None:
      tmp = cur.data
      self.head = self.tail = None
      return tmp
      
    while cur.next:
      prev = cur
      cur = cur.next

    prev.next = None
    self.tail = prev
    tmp = cur.data
    
    del cur
    return tmp
  
  def unshift(self, data):
    node = Node(data)
    
    if self.head is None :
      self.head = self.tail = node
    
    else:
      node.next = self.head
      self.head = node
  
  def shift(self):
    if self.head is None:
      return

    tmp = self.head.data
    
    if self.head.next is None:
      self.head = self.tail = None
    
    self.head = self.head.next
    
    return tmp
    
  def print(self):
    cur = self.head
    
    while cur :
      print(cur.data)
      cur = cur.next


lst = LinkedList()

lst.push(10)
lst.push(11)
lst.push(12)
lst.shift()
lst.unshift(-5)
lst.print()