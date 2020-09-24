class Node:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

def buildTree(inOrder, preOrder): # FC CF

  if (len(inOrder) == 0):
    return None

  root = preOrder[0] # C
  node = Node(root)

  if (len(inOrder) == 1):
    return node

  rootIndex = inOrder.index(root) # 1
  preLeftSubTree = preOrder[1:rootIndex+1] # F
  preRightSubTree = preOrder[rootIndex+1:] # []

  inLeftSubTree = inOrder[:rootIndex] # F
  inRightSubTree = inOrder[rootIndex+1:] # []

  node = Node(root)
  node.left = buildTree(inLeftSubTree, preLeftSubTree)
  node.right = buildTree(inRightSubTree, preRightSubTree)

  return node

def printInorder(node): 
  if node is None: 
    return 
  # first recur on left child 
  printInorder(node.left) 
  # then print the data of node 
  print(node.data, end=" ")
  # now recur on right child 
  printInorder(node.right) 

def printPostorder(node):
  if node is None:
    return
  # first recur on left
  printPostorder(node.left)
  # then recur on right
  printPostorder(node.right)
  #then print node
  print(node.data, end=" ")

inOrder = ['D', 'B', 'E', 'A', 'F', 'C'] 
preOrder = ['A', 'B', 'D', 'E', 'C', 'F'] 
root = buildTree(inOrder, preOrder)
printPostorder(root)

