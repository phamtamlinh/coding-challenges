# We're going to make our own Contacts application! The application must perform two types of operations:

# add name, where namename is a string denoting a contact name. This must store namename as a new contact in the application.

# find partial, where partialpartial is a string denoting a partial name to search the application for. It must count the number of contacts starting with partialpartial and print the count on a new line.

# Given n sequential add and find operations, perform each operation in order.

# Input
# The first line contains a single integer, n, denoting the number of operations to perform.

# Each line i of the n subsequent lines contains an operation in one of the two forms defined above.

# Constraints
# 1 <= n <= 10^5
# 1 <= name <= 21
# 1 <= partial <= 21
# It is guaranteed that namename and partialpartial contain lowercase English letter only.
# The input doesn't have any duplicate namename for the addadd operator.
# Output
# For each find partial operation, print the number of contact names starting with partial on a new line.

# Example
# input
# 4
# add hack
# add hackerrank
# find hac
# find hak
# output
# 2
# 0

class Node:
  def __init__(self):
    self.count = 0
    self.child = dict()
    self.child.clear()
def addWord(root, s):
  for ch in s:
    if ch not in root.child:
      root.child[ch] = Node()
    root = root.child[ch]
    root.count += 1

def findPartial(root, s):
  for ch in s:
    if ch not in root.child:
      return 0
    root = root.child[ch]
  return root.count

n = int(input())
root = Node()
for i in range(n):
  command, word = input().split()
  if command == 'add':
    addWord(root, word)
  if command == 'find':
    count = findPartial(root, word)
    print(count)