def solution(A, B, K):
  (first, last) = (0, 0)
  if A % K == 0:
    first = int(A / K - 1)
  else:
    first = int(A/K)

  last = int(B/K)
  return last - first