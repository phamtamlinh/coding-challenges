# Singham and his friends are fond of pizza. But this time they short of money. So they decided to help each other. They all decided to bring pizza in pairs. Our task is to find the total number of pairs possible which can buy pizza, given the cost of pizza. As pizza boy dont have any cash for change, if the pair adds upto more money than required, than also they are unable to buy the pizza. Each friend is guaranteed to have distinct amount of money. As it is Singham's world, money can also be negative ;).

# Input
# The first line consist of t (1<=t<=100) test cases. In the following 2*t lines, for each test case first there is n and m, where n (1 <= n <= 100000) is number of Singham's friend and m is the price of pizza. The next line consist of n integers, seperated by space, which is the money each friend have.

# The value of m and money is within the limits of int in C, C++.

# Output
# A single integer representing the number of pairs which can eat pizza.

# Example
# input
# 2
# 4 12
# 9 -3 4 3
# 5 -9
# -7 3 -2 8 7
# output
# 1
# 1

def bsFirst(a, left, right, x):
  if left <= right:
    mid = (left + right) // 2
    if (mid == left or x > a[mid-1]) and a[mid] == x:
      return mid
    elif x > a[mid]:
      return bsFirst(a, mid+1, right, x)
    else:
      return bsFirst(a, left, mid-1, x)
  return -1

def bsLast(a, left, right, x):
  if left <= right:
    mid = (left + right) // 2
    if (mid == right or x < a[mid+1]) and a[mid] == x:
      return mid
    elif x < a[mid]:
      return bsLast(a, left, mid-1, x)
    else:
      return bsLast(a, mid+1, right, x)
  return -1

t = int(input())
for i in range(t):
  n, m = map(int, input().split())
  arr = list(map(int, input().split()))
  arr.sort()
  left, right = 0, len(arr)-1
  count = 0
  while left < right:
    if arr[left] + arr[right] == m:
      count += 1
      left += 1
      right -= 1
    elif arr[left] + arr[right] < m:
      x = m - arr[left]
      newLeft = bsFirst(arr, left, right, x)
      if newLeft > -1:
        left = newLeft
        right -= 1
        count += 1
      else:
        left += 1
    else:
      x = m - arr[right]
      newRight = bsLast(arr, left, right, x)
      if newRight > -1:
        right = newRight
        left += 1
        count += 1
      else:
        right -= 1
  print(count)
