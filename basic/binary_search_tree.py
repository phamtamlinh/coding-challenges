class Node:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

class BinarySearchTree:
  def __init__(self):
    self.root = None
  
  def insert(self, data):
    newNode = Node(data)
    if self.root is None:
      self.root = newNode
    else:
      self.insertNode(self.root, newNode)
  
  def insertNode(self, node, newNode):
    if newNode.data < node.data:
      if node.left is None:
        node.left = newNode
      else:
        self.insertNode(node.left, newNode)
    else:
      if node.right is None:
        node.right = newNode
      else:
        self.insertNode(node.right, newNode)
  
  def search(self, node, data):
    if node is None or node.data == data:
      return node

    if node.data < data:
      return self.search(node.right, data)
    else:
      return self.search(node.left, data)
  
  def searchAndReturnParentNode(self, node, data):
    parent = None
    while node and node.data != data:
      parent = node
      if data < node.data:
        node = node.left
      else:
        node = node.right
    return parent, node
  
  def getInorderSuccessor(self, node):
    if node.left and node.left.left is None:
      return node, node.left
    else:
      self.getInorderSuccessor(node.left)

  def delete(self, data):
    if self.root is None:
      return self.root
    
    parentNode, node = self.searchAndReturnParentNode(self.root, data)

    if node.left is None and node.right is None:
      if node != self.root:
        if parentNode.left == node:
          parentNode.left = None
        else:
          parentNode.right = None
      else:
        self.root = None
    elif node.left and node.right:
      parentNodeSuccessor, nodeSuccessor = self.getInorderSuccessor(node.right)
      node.data = nodeSuccessor.data
      parentNodeSuccessor.left = None
    else:
      child = None
      if node.left:
        child = node.left
      else:
        child = node.right
      if node != self.root:
        if parentNode.left == node:
          parentNode.left = child
        else:
          parentNode.right = child
      else:
        self.root = child

def printInorder(node):
  if node:
    printInorder(node.left)
    print(node.data)
    printInorder(node.right)


# arr = [1, 2, 3, 4, 5]
arr = [50, 30, 20, 40, 70, 60, 80]
binTree = BinarySearchTree()
for i in range(0, len(arr)):
  binTree.insert(arr[i])

# node = binTree.search(binTree.root, 70)
binTree.delete(20)
print("Inorder traversal of the modified tree")
printInorder(binTree.root)

binTree.delete(30)
print("Inorder traversal of the modified tree")
printInorder(binTree.root)

binTree.delete(50)
print("Inorder traversal of the modified tree")
printInorder(binTree.root)
