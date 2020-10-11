def heapify(arr, n, i):
  largest = i
  left = 2*i + 1
  right = 2*i + 2

  if left < n and arr[left] > arr[largest]:
    largest = left
  if right < n and arr[right] > arr[largest]:
    largest = right
  
  if largest != i:
    arr[largest], arr[i] = arr[i], arr[largest]
    heapify(arr, n, largest)

def heap_sort(arr):
  n = len(arr)
  for i in range(n-1, -1, -1):
    heapify(arr, n, i)
  print(arr)
  
  for i in range(n-1, 0, -1):
    arr[0], arr[i] = arr[i], arr[0]
    heapify(arr, i, 0)

# Driver code to test above
arr = [38, 27, 43, 3, 9, 82, 10, 2, 1, 5, 6, 90, 42]
heap_sort(arr)
print(arr)
