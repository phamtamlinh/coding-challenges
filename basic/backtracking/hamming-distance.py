# The Hamming distance between two strings of bits (binary integers) is the number of corresponding bit positions that differ. This can be found by using XOR on corresponding bits or equivalently, by adding corresponding bits (base 2) without a carry. For example, in the two bit strings that follow

# A	0	1	0	0	1	0	1	0	0	0
# B	1	1	0	1	0	1	0	1	0	0
# A XOR B	1	0	0	1	1	1	1	1	0	0
# The Hamming distance (H) between these 1010-bit strings is 6, the number of 1's in the XOR string.

# Dữ liệu nhập
# Input consists of several datasets.

# The first line of the input contains the number of datasets, and it's followed by a blank line.

# Each dataset contains NN, the length of the bit strings and HH, the Hamming distance, on the same line. There is a blank line between test cases.

# Dữ liệu xuất
# For each dataset print a list of all possible bit strings of length NN that are Hamming distance HH from the bit string containing all 0's (origin). That is, all bit strings of length NN with exactly HH 1's printed in ascending lexicographical order.

# The number of such bit strings is equal to the combinatorial symbol C(N, H)C(N,H). This is the number of possible combinations of N - HN−H zeros and HH ones. It is equal to
# N!/((N-H)!H!)

# This number can be very large. The program should work for 1 <= H <= N <= 16.

# Print a blank line between datasets.

# Ví dụ
# inputcopy
# 1

# 4 2
# outputcopy
# 0011
# 0101
# 0110
# 1001
# 1010
# 1100

def shouldSwap(s, start, end):
  for i in range(start, end):
    if s[i] ==  s[end]:
      return False
  return True

def distinctPermutations(s, l, r):
  if l >= r:
    print(''.join(s))
    return
  for i in range(l, r):
    check = shouldSwap(s, l, i)
    if check == True:
      s[l], s[i] = s[i], s[l]
      distinctPermutations(s, l+1, r)
      s[l], s[i] = s[i], s[l]

T = int(input())
input()
for _ in range(T):
  N, H = map(int, input().split())
  s = ['0']*(N-H) + ['1']*H
  distinctPermutations(s, 0, len(s))
  if _ < T-1:
    print()