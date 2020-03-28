def solution(A):
  arr = (len(A)+1)*[0]
  for i in range(len(A)):
    arr[i+1] = A[i] + arr[i]

  (P, minAve) = (0, max(A))
  for i in range(len(A)-1):
    ave2 = (arr[i+2]-arr[i])/2
    ave3 = minAve
    if i < len(A)-2:
        ave3 = (arr[i+3]-arr[i])/3

    if minAve > ave2:
      minAve = ave2
      P = i
    if minAve > ave3:
      minAve = ave3
      P = i
  return P
