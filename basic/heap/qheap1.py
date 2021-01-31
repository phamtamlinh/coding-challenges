# This question is designed to help you get a better understanding of basic heap operations. You will be given queries of 3 types:

# "1 v" - Add an element to the heap.
# "2 v" - Delete the element from the heap.
# "3" - Print the minimum of all the elements in the heap.
# NOTE: It is guaranteed that the element to be deleted will be there in the heap. Also, at any instant, only distinct elements will be in the heap.

# Input
# The first line contains the number of queries, Q (1 <= Q <= 10^5).

# Each of the next Q lines contains a single query of any one of the 3 above mentioned types (-10^9 <= v <= 10^9)

# Output
# For each query of type 3, print the minimum value on a single line.

# Example
# input
# 5
# 1 4
# 1 9
# 3
# 2 4
# 3
# output
# 4
# 9
# Explain
# After the first 2 queries, the heap contains 4, 9. Printing the minimum gives 4 as the output. Then, the 4th query deletes 4 from the heap, and the 5th query gives 9 as the output.

import sys
sys.setrecursionlimit(10**6)

pq = []
pqRemove  = []

def deleteElement(h, i):
  length = len(h)
  if length == 0:
    return
  h[i] = h[length-1]
  h.pop()
  minHeapify(h, i)

def addElement(h, e):
  h.append(e)
  i = len(h) - 1
  while i != 0 and h[(i-1)//2] > h[i]:
    h[i], h[(i-1)//2] = h[(i-1)//2], h[i]
    i = (i-1)//2

def minHeapify(h, i):
  smallest = i
  left = 2*i+1
  right = 2*i+2
  if left < len(h) and h[left] < h[smallest]:
    smallest = left
  if right < len(h) and h[right] < h[smallest]:
    smallest = right
  if smallest != i:
    h[i], h[smallest] = h[smallest], h[i]
    minHeapify(h, smallest)

Q = int(input())
for i in range(Q):
  a = list(map(int, input().split()))
  if a[0] == 1:
    addElement(pq, a[1])
  elif a[0] == 2:
    addElement(pqRemove, a[1])
  elif a[0] == 3:
    while len(pqRemove) and pq[0] == pqRemove[0]:
      deleteElement(pq, 0)
      deleteElement(pqRemove, 0)
    print(pq[0])