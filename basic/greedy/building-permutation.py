# Building Permutation
# Permutation pp is an ordered set of integers p1, p2, ..., pn, consisting of n distinct positive integers, each of them doesn't exceed n. We'll denote the ith element of permutation p as pi. We'll call number n the size or the length of permutation p1, p2, ..., pn.

# You have a sequence of integers a1, a2, ..., an. In one move, you are allowed to decrease or increase any number by one. Count the minimum number of moves needed to build a permutation from this sequence.

# Dữ liệu nhập
# The first line contains integer n (1 <= n <= 3*10^5) — the size of the sought permutation.

# The second line contains n integers a1, a2, ..., an (-10^9 <= ai <= 10^9).

# Dữ liệu xuất
# Print a single number — the minimum number of moves.

# Ví dụ
# inputcopy
# 2
# 3 0
# outputcopy
# 2
# inputcopy
# 3
# -1 -1 2
# outputcopy
# 6
# Giải thích ví dụ
# In the first sample you should decrease the first number by one and then increase the second number by one. The resulting permutation is (2, 1).

# In the second sample you need 6 moves to build permutation (1, 3, 2).

n = int(input())
a = list(map(int, input().split()))
change = 0

a.sort()
i = 1
for num in a:
  change = change + abs(num-i)
  i += 1
print(change)
