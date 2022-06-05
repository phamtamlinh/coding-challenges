# A fraction m/n is basic if 0≤m<n and it is irreducible if gcd(m, n) = 1. Given a positive integer n, in this problem you are required to find out the number of irreducible basic fractions with denominator n.

# For example, the set of all basic fractions with denominator 12, before reduction to lowest terms, is

# 0/12, 1/12, 2/12, ..., 11/12

# Reduction yields

# 0/1, 1/12, 1/6, ..., 11/12

# Hence there are only the following 44 irreducible basic fractions with denominator 12

# 1/12, 5/12, 7/12, 11/12

# Dữ liệu nhập
# Each line of the input contains a positive integer nn (n < 1000000000) and the input terminates with a value 00 for n (do not process this terminating value).

# Dữ liệu xuất
# For each n in the input print a line containing the number of irreducible basic fractions with denominator n.

# Ví dụ
# inputcopy
# 12
# 123456
# 7654321
# 0
# outputcopy
# 4
# 41088
# 7251444

# basically find total of relatively prime numbers

def phi(n):
  result = n
  for i in range(2, int(n**0.5) + 1):
    if n % i == 0:
      while n % i == 0:
        n //= i
      result = result // i * (i-1)
  if n > 1:
    result = result // n * (n-1)
  return result

while True:
  n = int(input())
  if n == 0:
    break
  print(phi(n))