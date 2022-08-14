case = 1
end_of_case = 0
A = []

def LIS(a):
  length = 0
  dp = [1]* (len(a)+1)
  for i in range(1, len(a)):
    for j in range(i):
      if a[i] > a[j] and dp[i] < dp[j] + 1:
        dp[i] = dp[j] + 1
  for i in range(len(a)):
    if length < dp[i]:
      length = dp[i]
  return length
while True:
  h = int(input())
  if end_of_case == -1 and h == -1:
    break
  if end_of_case != -1 and h == -1:
    end_of_case = -1
    result = LIS(A)
    if case > 1:
      print()
    print("Test #" + str(case) + ":")
    print("  maximum possible interceptions: " + str(result))
    A = []
    case += 1
  elif h != -1:
    end_of_case = h
    A.append(h)