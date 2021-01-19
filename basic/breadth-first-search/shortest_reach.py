# Consider an undirected graph consisting of N nodes where each node is labeled from 1 to N and the edge between any two nodes is always of length 6. We define node S to be the starting position for a BFS.

# Given Q queries in the form of a graph and some starting node, S, perform each query by calculating the shortest distance from starting node S to all the other nodes in the graph. Then print a single line of N - 1 space-separated integers listing node S's shortest distance to each of the N - 1 other nodes (ordered sequentially by node number); if S is disconnected from a node, print -1 as the distance to that node.

# Input
# The first line contains an integer, Q, denoting the number of queries. The subsequent lines describe each query in the following format:

# The first line contains two space-separated integers describing the respective values of N (the number of nodes) and M (the number of edges) in the graph.
# Each line ii of the M subsequent lines contains two space-separated integers, u and v, describing an edge connecting node u to node v.
# The last line contains a single integer, S, denoting the index of the starting node.
# Constraints
# * 1 <= Q <= 10
# * 2 <= N <= 1000
# * 1 <= M <= N*(N-1)/2
# * 1 <= u,v,S <= N

# Output
# For each of the Q queries, print a single line of N - 1 space-separated integers denoting the shortest distances to each of the N - 1 other nodes from starting position S. These distances should be listed sequentially by node number (i.e., 1, 2, ...,N), but should not include node S. If some node is unreachable from S, print -1 as the distance to that node.

# Example
# Input
# 2
# 4 2
# 1 2
# 1 3
# 1
# 3 1
# 2 3
# 2
# Output
# 6 6 -1
# -1 6

from queue import Queue

def BFS(graph, visited, path, S):
  q = Queue()
  visited[S-1] = True
  q.put(S)
  while not q.empty():
    u = q.get()
    for v in graph[u-1]:
      if not visited[v-1]:
        visited[v-1] = True
        q.put(v)
        path[v-1] = u

# def printPath(path, s, f, m, l):
#   if s == f:
#     m.append(l)
#   else:
#     if path[f-1] == -1:
#       m.append(-1)
#     else:
#       l += 6
#       printPath(path, s, path[f-1], m, l)

def printPath(path, s, f):
  l = 0
  if path[f-1] == -1:
    return -1
  while True:
    l += 6
    f = path[f-1]
    if f == s:
      return l


def test():
  R = []
  N, M = map(int, input().split(" "))
  graph = [[] for j in range(N)]
  for i in range(M):
    u, v = map(int, input().split(" "))
    graph[u-1].append(v)
    graph[v-1].append(u)
  S = int(input())
  visited = [False for i in range(N)]
  path = [-1 for i in range(N)]

  BFS(graph, visited, path, S)
  for i in range(N):
    if S != i+1:
      m = printPath(path, S, i+1)
      R.append(m)
  return R


Q = int(input())
R = [[] for j in range(Q)]
for j in range(Q):
  R[j] = test()

for j in range(Q):
  print(*R[j], sep=" ")