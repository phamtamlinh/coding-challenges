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
    if self.head == None:
      self.head = node
    else:
      self.tail.next = node

    self.tail = node
  def printList(self):
    node = self.head
    result = ''
    while(node):
      result += str(node.data) + ' '
      node = node.next
    print(result)
  def reverse(self):
    currNode = self.head
    nextNode, prevNode = None, None
    while(currNode):
      nextNode = currNode.next
      currNode.next = prevNode
      prevNode = currNode
      currNode = nextNode
    self.head = prevNode

arr = [1, 2, 32, 4]
llist = SinglyLinkedList()
for a in arr:
  llist.insertNode(a)
llist.reverse()
llist.printList()
