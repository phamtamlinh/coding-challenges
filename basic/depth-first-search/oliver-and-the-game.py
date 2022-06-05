# Oliver and Bob are best friends. They have spent their entire childhood in the beautiful city of Byteland. The people of Byteland live happily along with the King.

# The city has a unique architecture with total NN houses. The King's Mansion is a very big and beautiful bungalow having address = 1=1. Rest of the houses in Byteland have some unique address, (say AA), are connected by roads and there is always a unique path between any two houses in the city. Note that the King's Mansion is also included in these houses.

# Oliver and Bob have decided to play Hide and Seek taking the entire city as their arena. In the given scenario of the game, it's Oliver's turn to hide and Bob is supposed to find him.

# Oliver can hide in any of the houses in the city including the King's Mansion. As Bob is a very lazy person, for finding Oliver, he either goes towards the King's Mansion (he stops when he reaches there), or he moves away from the Mansion in any possible path till the last house on that path.

# Oliver runs and hides in some house (say XX) and Bob is starting the game from his house (say YY). If Bob reaches house XX, then he surely finds Oliver.

# Given QQ queries, you need to tell Bob if it is possible for him to find Oliver or not.

# The queries can be of the following two types:

# 0 \ X \ Y0 X Y : Bob moves towards the King's Mansion.
# 1 \ X \ Y1 X Y : Bob moves away from the King's Mansion

# Dữ liệu nhập
# The first line of the input contains a single integer NN, total number of houses in the city. Next N - 1N−1 lines contain two space separated integers AA and BB denoting a road between the houses at address AA and BB.
# Next line contains a single integer QQ denoting the number of queries.
# Following QQ lines contain three space separated integers representing each query as explained above.

# CONSTRAINS:

# 1 \le N \le 10^51≤N≤10
# ​5
# ​​ 
# 1 \le A,B \le N1≤A,B≤N
# 1 \le Q \le 5*10^51≤Q≤5∗10
# ​5
# ​​ 
# 1 \le X,Y \le N1≤X,Y≤N
# Dữ liệu xuất
# Print YES or NO for each query depending on the answer to that query.

# Ví dụ
# inputcopy
# 9
# 1 2
# 1 3
# 2 6
# 2 7
# 6 9
# 7 8
# 3 4
# 3 5
# 5
# 0 2 8
# 1 2 8
# 1 6 5
# 0 6 5
# 1 9 1
# outputcopy
# YES
# NO
# NO
# NO
# YES

import sys
sys.setrecursionlimit(100000000)

t = 0

def DFS(v):
  global t
  global graph
  global start_time
  global finish_time
  t += 1
  start_time[v] = t
  for u in graph[v]:
    if start_time[u] == 0:
      DFS(u)
  t += 1
  finish_time[v] = t

N = int(input())
graph = [[] for _ in range(N+1)]
for _ in range(N-1):
  u, v = map(int, input().split())
  graph[u].append(v)
  graph[v].append(u)
start_time = [0] * (N+1)
finish_time = [0] * (N+1)
DFS(1)
Q = int(input())
for _ in range(Q):
  move, X, Y = map(int, input().split())
  if move == 1:
    X, Y = Y, X
  if start_time[X] <= start_time[Y] and finish_time[X] >= finish_time[Y]:
    print('YES')
  else:
    print('NO')

