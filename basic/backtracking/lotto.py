# In the German Lotto you have to select 6 numbers from the set {1,2,...,49}. A popular strategy to play Lotto - although it doesn’t increase your chance of winning — is to select a subset S containing k (k > 6) of these 49 numbers, and then play several games with choosing numbers only from S.

# For example, for k = 8 and S={1,2,3,5,8,13,21,34} there are 28 possible games: [1,2,3,5,8,13], [1,2,3,5,8,21], [1,2,3,5,8,34], [1,2,3,5,13,21], ..., [3,5,8,13,21,34].

# Your job is to write a program that reads in the number kk and the set SS and then prints all possible games choosing numbers only from SS.

# Dữ liệu nhập
# Input will contain one or more test cases.

# Each test case consists of one line containing several integers separated from each other by spaces. The first integer on the line will be the number k (6 < k < 13). Then k integers, specifying the set S, will follow in ascending order.

# Input will be terminated by a value of zero (0) for k.

# Dữ liệu xuất
# For each test case, print all possible games, each game on one line.

# The numbers of each game have to be sorted in ascending order and separated from each other by exactly one space. The games themselves have to be sorted lexicographically, that means sorted by the lowest number first, then by the second lowest and so on, as demonstrated in the sample output below.

# The test cases have to be separated from each other by exactly one blank line. Do not put a blank line after the last test case.

# Ví dụ
# inputcopy
# 7 1 2 3 4 5 6 7
# 8 1 2 3 5 8 13 21 34
# 0
# outputcopy
# 1 2 3 4 5 6
# 1 2 3 4 5 7
# 1 2 3 4 6 7
# 1 2 3 5 6 7
# 1 2 4 5 6 7
# 1 3 4 5 6 7
# 2 3 4 5 6 7

# 1 2 3 5 8 13
# 1 2 3 5 8 21
# 1 2 3 5 8 34
# 1 2 3 5 13 21
# 1 2 3 5 13 34
# 1 2 3 5 21 34
# 1 2 3 8 13 21
# 1 2 3 8 13 34
# 1 2 3 8 21 34
# 1 2 3 13 21 34
# 1 2 5 8 13 21
# 1 2 5 8 13 34
# 1 2 5 8 21 34
# 1 2 5 13 21 34
# 1 2 8 13 21 34
# 1 3 5 8 13 21
# 1 3 5 8 13 34
# 1 3 5 8 21 34
# 1 3 5 13 21 34
# 1 3 8 13 21 34
# 1 5 8 13 21 34
# 2 3 5 8 13 21
# 2 3 5 8 13 34
# 2 3 5 8 21 34
# 2 3 5 13 21 34
# 2 3 8 13 21 34
# 2 5 8 13 21 34
# 3 5 8 13 21 34

def printAns(a):
  for i in range(len(a)):
    print(a[i], end=' ')

def combination(S, a, left, k, lotto_length):
  if k == 0:
    printAns(a)
    print()
    return
  for i in range(left, len(S)+1):
    a.append(S[i-1])
    combination(S, a, i+1, k-1, lotto_length)
    a.pop()
blank_line = False
while True:
  k, *S = list(map(int, input().split()))
  if k == 0:
    break
  if blank_line:
    print()
  a = []
  combination(S, a, 1, 6, 6)
  blank_line = True
