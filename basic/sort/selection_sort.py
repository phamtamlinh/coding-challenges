def selection_sort(arr):
  for i in range(1, len(arr)):
    min_index = i
    for j in range(i+1, len(arr)):
      if arr[min_index] > arr[j]:
        min_index = j
    arr[i], arr[min_index] = arr[min_index], arr[i]


arr = [4, 3, 2, 10, 12, 1, 5, 6]
selection_sort(arr)
print(arr)
