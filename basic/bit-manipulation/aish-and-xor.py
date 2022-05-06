# Aish is playing with XOR, given an array (containing only 00 and 11) as element of NN length.

# Given LL and RR, she wants to know the value of XOR of all elements from LL to RR (both inclusive) and number of unset bits (00's) in the given range of the array.

# Being new she finds it tough so she asked for help from Puper. Puper also finds it tough and confusing. So he asked for your help.

# Input Format
# The first line contains the number NN.

# The second line contains NN numbers containing 00 and 11 only.

# The third line contains number of query QQ.

# The next QQ lines contains LL and RR.

# Output Format
# For each query print the XOR value and number of unset bits in that range.

# Constraints
# 1 \le N \le 1000001≤N≤100000 (11-based indexing of elements)
# 1 \le Q \le N1≤Q≤N
# 1 \le L \le R \le 1000001≤L≤R≤100000
# 0 \le R - L \le 1000000≤R−L≤100000
# Sample test
# inputcopy
# 5
# 1 0 0 0 1
# 3
# 2 4
# 1 5
# 3 5
# outputcopy
# 0 3
# 0 3
# 1 2

N = int(input())
arr = list(map(int, input().split()))
Q = int(input())
count = [0] * (N+1)

for i in range(1, N+1):
  count[i] = count[i-1] + arr[i-1]

for i in range(1, Q+1):
  L, R = map(int, input().split())
  count1 = count[R] - count[L-1]
  print(count1 % 2, R-L+1-count1)