# Some natural number was written on the board. Its sum of digits was not less than k. But you were distracted a bit, and someone changed this number to nn, replacing some digits with others. It's known that the length of the number didn't change.

# You have to find the minimum number of digits in which these two numbers can differ.

# Dữ liệu nhập
# The first line contains integer k (1 <= k <= 10^9).

# The second line contains integer n (1 <= n <= 10^100000)

# There are no leading zeros in n. It's guaranteed that this situation is possible.

# Dữ liệu xuất
# Print the minimum number of digits in which the initial number and n can differ.

# Ví dụ
# inputcopy
# 3
# 11
# outputcopy
# 1
# inputcopy
# 3
# 99
# outputcopy
# 0
# Giải thích ví dụ
# In the first example, the initial number could be 12.

# In the second example the sum of the digits of nn is not less than k. The initial number could be equal to n.

k = int(input())
n = int(input())
digits = list(map(int, str(n)))
digits.sort()
sum_digit = sum(digits)
digit_change = 0
i = 0

while sum_digit < k and i < len(digits):
  change = 9 - digits[i]
  sum_digit += change
  digit_change += 1
  i += 1

print(digit_change)
