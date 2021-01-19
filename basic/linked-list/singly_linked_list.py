class SinglyLinkedListNode:
  def __init__(self, data):
    self.data = data
    self.next = None

class SinglyLinkedList:
  def __init__(self):
    self.head = None
    self.tail = None
  
  def insertNode(self, data):
    node = SinglyLinkedListNode(data)
    if self.head is None:
      self.head = node
    else:
      self.tail.next = node
    
    self.tail = node
  
  def printList(self, node):
    result = ''
    while(node):
      result += str(node.data) + ' '
      node = node.next
    print(result)
  
  def reverse(self):
    current = self.head
    prev, next = None, None
    while current:
      next = current.next
      current.next = prev
      prev = current
      current = next
    self.head = prev

arr = [1, 2, 32, 4]
llist = SinglyLinkedList()
for a in arr:
  llist.insertNode(a)

llist.reverse()
llist.printList(llist.head)
