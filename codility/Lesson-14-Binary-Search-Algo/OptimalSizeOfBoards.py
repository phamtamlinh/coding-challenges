# You are given n binary values x0, x1, . . . , xn−1, such that xi ∈ {0, 1}. This array represents holes in a roof(1 is a hole). You are also given k boards of the same size. The goal is to choose the optimal(minimal) size of the boards that allows all the holes to be covered by boards.
import math
def boards(A, k):
  n = len(A)
  beg = 1
  end = n
  result = -1
  while (beg <= end):
    mid = math.floor((beg + end) / 2)
    print(f"beg {beg} - end {end} - mid {mid}")
    if (check(A, mid) <= k):
      end = mid-1
      result = mid
    else:
      beg = mid+1
  return result

def check(A, k):
  n = len(A)
  boards = 0
  last = -1
  for i in range(n):
    if A[i] == 1 and last < i:
      print(f"i {i} - A[i] {A[i]} - last {last}")
      boards += 1
      last = i + k - 1
  print(f"boards {boards}")
  return boards

A = [0,1,0,1,1,0,1,1,1]
print (boards(A, 4))