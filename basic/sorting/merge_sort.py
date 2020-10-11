def merge_sort(arr):
  if len(arr) > 1:
    mid = len(arr)//2
    L = arr[:mid]
    R = arr[mid:]
    merge_sort(L)
    merge_sort(R)

    i = j = k = 0
    while i < len(L) and j < len(R):
      if L[i] < R[j]:
        arr[k] = L[i]
        i += 1
      else:
        arr[k] = R[j]
        j += 1
      k += 1
      print(arr)
    
    while i < len(L):
      arr[k] = L[i]
      k += 1
      i += 1
    while j < len(R):
      arr[k] = R[j]
      k += 1
      j += 1

arr = [38, 27, 82, 3, 9, 43, 10]
merge_sort(arr)
print(arr)
