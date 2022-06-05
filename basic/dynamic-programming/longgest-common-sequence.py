# Agnes, a student of computer science, is very keen on cross¬country running, and she participates in races organised every Saturday in a big park. Each of the participants obtains a route card, which specifies a sequence of checkpoints, which they need to visit in the given order. Agness is a very atractive girl, and a number of male runners have asked her for a date. She would like to choose one of them during the race. Thus she invited all her admirers to the park on Saturday and let the race decide. The winner would be the one, who scores the maximum number of points. Agnes came up with the following rules:

# a runner scores one point if he meets Agnes at the checkpoint,
# if a runner scored a point at the checkpoint, then he cannot get another point unless he and Agnes move to the next checkpoints specified in their cards.
# route specified by the card may cross the same checkpoint more than once,
# each competitor must strictly follow race instructions written on his card.
# Between two consecutive meetings, the girl and the competitors may visit any number of checkpoints. The boys will be really doing their best, so you may assume, that each of them will be able to visit any number of checkpoints whilst Agnes runs between two consecutive ones on her route.

# You should write a program which for each data set from a sequence of several data sets:

# reads in the contents of Agnes' race card and contents of race cards presented to Tom,
# computes the greatest number of times Tom is able to meet Agnes during the race,
# writes it to output.
# Dữ liệu nhập
# There is one integer dd in the first line of the input file, 1≤d≤10. This is the number of data sets. The data sets follow. Each data set consists of a number of lines, with the first one specifying the route in Agnes' race card. Consecutive lines contain routes on cards presented to Tom. At least one route is presented to Tom. The route is given as a sequence of integers from interval [1, 1000] separated by single spaces. Number 0 stands for the end of the route, though when it is placed at the beginning of the line it means the end of data set. There are at least two and at most 2000 checkpoints in a race card.

# Dữ liệu xuất
# The ith line of the output file should contain one integer. That integer should equal the greatest number of times Tom is able to meet with Agnes for race cards given in the ith data set.

# Ví dụ
# inputcopy
# 3
# 1 2 3 4 5 6 7 8 9 0
# 1 3 8 2 0
# 2 5 7 8 9 0
# 1 1 1 1 1 1 2 3 0
# 1 3 1 3 5 7 8 9 3 4 0
# 1 2 35 0
# 0
# 1 3 5 7 0
# 3 7 5 1 0
# 0
# 1 2 1 1 0
# 1 1 1 0
# 0
# outputcopy
# 6
# 2
# 3

MAXM = 1000
MAXN = 1000
dp = [[-1] * (MAXN + 1) for _ in range(MAXM+1)]
def LCS(s1, s2, m, n):
  for i in range(m+1):
    for j in range(n+1):
      if i == 0 or j == 0:
        dp[i][j] = 0
      elif s1[i-1] == s2[j-1]:
        dp[i][j] = dp[i-1][j-1] + 1
      else:
        dp[i][j] = max(dp[i-1][j], dp[i][j-1])
  return dp[m][n]
        
d = int(input())
for _ in range(d):
  A = list(map(int, input().split()))
  A = A[:-1]
  result = 0
  while True:
    B = list(map(int, input().split()))
    if B[0] == 0:
      break
    B = B[:-1]
    result = max(LCS(A, B, len(A), len(B)), result)
  print(result)