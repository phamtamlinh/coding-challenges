import math

class MaxHeap:
  def __init__(self):
    self.heap = []
  
  def getMax(self):
    return self.heap[0]
  
  def getHeap(self):
    return self.heap
  
  def insert(self, node):
    self.heap.append(node)

    if len(self.heap) > 0:
      currentIndex = len(self.heap) - 1
      while currentIndex > 0 and self.heap[math.floor(currentIndex/2)] < self.heap[currentIndex]:
        parentIndex = math.floor(currentIndex/2)
        self.heap[parentIndex], self.heap[currentIndex] = self.heap[currentIndex], self.heap[parentIndex]
        currentIndex = parentIndex

maxHeap = MaxHeap()
arr = [7, 10, 4, 3, 20, 15]
for a in arr:
  maxHeap.insert(a)

print(maxHeap.getHeap())
