def solution(A):
  maxi = max(A)
  if maxi < 1:
    return 1
  if len(A) > maxi:
    leng = len(A)
  else:
    leng = maxi
  
  arr = [0]*leng
  for i in range(len(A)):
    if A[i] > 0:
      arr[A[i]-1] += 1
  for i in range(leng):
    if arr[i] < 1:
      return i+1
  return maxi+1