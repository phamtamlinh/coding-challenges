import math

class MinHeap:
  def __init__(self):
    self.heap = []
  
  def getMin(self):
    return self.heap[0]
  
  def getHeap(self):
    return self.heap
  
  def insert(self, node):
    self.heap.append(node)

    if len(self.heap) > 0:
      currentIndex = len(self.heap) - 1
      while currentIndex > 0 and self.heap[math.floor(currentIndex/2)] > self.heap[currentIndex]:
        parentIndex = math.floor(currentIndex/2)
        self.heap[parentIndex], self.heap[currentIndex] = self.heap[currentIndex], self.heap[parentIndex]
        currentIndex = parentIndex

  def extractMin(self):
    length = len(self.heap)
    if length == 0:
      return None
    if length == 1:
      return self.heap[0]

    root = self.getMin()
    self.heap[0], self.heap[length-1] = self.heap[length-1], self.heap[0]
    self.heap.pop()
    self.heapify(0)
    return root
  
  def heapify(self, i):
    left = 2*i+1
    right = 2*i+2
    smallest = i
    length = len(self.heap)
    if left < length and self.heap[i] > self.heap[left]:
      smallest = left
    if right < length and self.heap[smallest] > self.heap[right]:
      smallest = right
    # print(self.heap)
    # print('i ' + str(i) + ' left ' + str(left) + ' right ' + str(right) + ' smallest ' + str(smallest))
    if smallest != i:
      self.heap[smallest], self.heap[i] = self.heap[i], self.heap[smallest]
      self.heapify(smallest)

minHeap = MinHeap()
# arr = [7, 10, 4, 3, 20, 15]
arr = [2, 5, 7, 8, 10, 9]
for a in arr:
  minHeap.insert(a)

print(minHeap.getHeap())
print(minHeap.extractMin())
print(minHeap.getHeap())
print(minHeap.extractMin())
print(minHeap.getHeap())
print(minHeap.extractMin())
print(minHeap.getHeap())