# Drazil has many friends. Some of them are happy and some of them are unhappy. Drazil wants to make all his friends become happy. So he invented the following plan.

# There are n boys and m girls among his friends. Let's number them from 0 to n - 1 and 0 to m - 1 separately. In ith day, Drazil invites (i%n)th boy and (i%m)th girl to have dinner together (as Drazil is programmer, ii starts from 0). If one of those two people is happy, the other one will also become happy. Otherwise, those two people remain in their states. Once a person becomes happy (or if he/she was happy originally), he stays happy forever.

# Drazil wants to know whether he can use this plan to make all his friends become happy at some moment.

# Dữ liệu nhập
# The first line contains two integer n and m (1≤n,m≤100).

# The second line contains an integer b (0≤b≤n), denoting the number of happy boys among friends of Drazil, and then follow b distinct integers x1, x2,..., xb (0 <= xi < n), denoting the list of indices of happy boys.

# The third line contains an integer g (0≤g≤m), denoting the number of happy girls among friends of Drazil, and then follow gg distinct integers y1, y2,..., yb (0≤yj<m), denoting the list of indices of happy girls.

# It is guaranteed that there is at least one person that is unhappy among his friends.

# Dữ liệu xuất
# If Drazil can make all his friends become happy by this plan, print Yes. Otherwise, print No.

# Ví dụ
# inputcopy
# 2 3
# 0
# 1 0
# outputcopy
# Yes
# inputcopy
# 2 4
# 1 0
# 1 2
# outputcopy
# No
# inputcopy
# 2 3
# 1 0
# 1 1
# outputcopy
# Yes

n, m = map(int, input().split())
b, *boys = map(int, input().split())
g, *girls = map(int, input().split())

def gcd(n, m):
  while m != 0:
    r = n%m
    n = m
    m = r
  return n

happy_boys = [False] * n
happy_girls = [False] * m

for person in boys:
  happy_boys[person] = True
  
for person in girls:
  happy_girls[person] = True

total_unhappy = m+n-b-g
lcm = int(m*n/gcd(m,n))

for i in range(2*lcm):
  if happy_boys[i%n] + happy_girls[i%m] == 1:
    happy_boys[i%n] = True
    happy_girls[i%m] = True
    total_unhappy -= 1

if total_unhappy == 0:
  print("Yes")
else:
  print("No")