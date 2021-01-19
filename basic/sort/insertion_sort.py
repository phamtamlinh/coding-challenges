def insertion_sort(arr):
  for i in range(1, len(arr)):
    j = i - 1
    k = i
    while arr[k] < arr[j] and j >= 0:
      arr[k], arr[j] = arr[j], arr[k]
      k = j
      j = j - 1

arr = [4, 3, 2, 10, 12, 1, 5, 6]
insertion_sort(arr)
print(arr)
