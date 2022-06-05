# Bytelandian gold coins
# In Byteland they have a very strange monetary system. Each Bytelandian gold coin has an integer number written on it. A coin nn can be exchanged in a bank into three coins: n/2, n/3, n/4. But these numbers are all rounded down (the banks have to make a profit). You can also sell Bytelandian coins for American dollars. The exchange rate is 1:1. But you can not buy Bytelandian coins. You have one gold coin. What is the maximum amount of American dollars you can get for it?

# Dữ liệu nhập
# The input will contain several test cases (not more than 10). Each testcase is a single line with a number n, 0≤n≤1000000000. It is the number written on your coin.

# Dữ liệu xuất
# For each test case output a single line, containing the maximum amount of American dollars you can make.

# Ví dụ
# inputcopy
# 12
# 2
# outputcopy
# 13
# 2
# Giải thích ví dụ
# Case 1: You can change 12 into 6, 4, 3, and then change these into $6+$4+$3=$13.

# Case 2: If you try changing the coin 2 into 3 smaller coins, you will get 1,0 and 0, and later you can get no more than $1 out of them. It is better just to change the 2 coin directly into $2.

MAX = 10**7 + 1
dp = [-1] * MAX

def solve(n):
  if n < MAX and dp[n] != -1:
    return dp[n]
  if n < 3:
    return n
  result = max(solve(n//2) + solve(n//3) + solve(n//4), n)
  if n < MAX:
  	dp[n] = result
  return result

while True:
  n = 0
  try:
    n = int(input())
  except:
    break
  print(solve(n))