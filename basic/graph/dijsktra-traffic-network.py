# The city traffic network consists of N nodes numbered from 1 to N and M one-way roads connecting pairs of nodes. In order to reduce the length of the shortest path between two different critical nodes S and T, a list of K two-way roads are proposed as candidates to be constructed. Your task is to write a program to choose one two-way road from the proposed list in order to minimize the resulting shortest path between S and T.

# Input
# The input file consists of several data sets. The first line of the input file contains the number of data sets which is a positive integer and is not bigger than 2020. The following lines describe the data sets.

# For each data set, the first line contains five positive integers N (N<=10000), M (M<=100000), K(K<300), S (1<= S<=N), T (1<=T<=N) separated by space. The i-th line of the following M lines contains three integers d, c, l separated by space, representing the length l i-th (0 <= l <= 1000) of the i-th one-way road connecting node d to c. The j-th line of the next K lines contains three positive integers u, v and q (q <= 1000) separated by space, representing the j-th proposed two-way road of length q connecting node u to v.

# Output
# For each data set, write on one line the smallest possible length of the shortest path after building the chosen one two-way road from the proposed list. In case, there does not exist a path from S to T, write -1.

# Example
# input
# 1
# 4 5 3 1 4
# 1 2 13
# 2 3 19
# 3 1 25
# 3 4 17
# 4 1 18
# 1 3 23
# 2 3 5
# 2 4 25
# out
# 35

import queue

INF = 10**9

class Node:
  def __init__(self, id, dist):
    self.id = id
    self.dist = dist
  def __lt__(self, other):
    return self.dist <= other.dist

def Dijkstra(graph, s):
  N = len(graph)
  dist = [INF for i in range(N)]
  path = [-1 for i in range(N)]
  pq = queue.PriorityQueue()
  pq.put(Node(s, 0))
  dist[s] = 0
  while not pq.empty():
    top = pq.get()
    u = top.id
    w = top.dist
    if dist[u] != w:
      continue
    for neighbor in graph[u]:
      if w + neighbor.dist < dist[neighbor.id]:
        dist[neighbor.id] = w + neighbor.dist
        pq.put(Node(neighbor.id, dist[neighbor.id]))
        path[neighbor.id] = u
  return dist

t = int(input())
for i in range(t):
  N, M, K, S, T = map(int, input().split())
  graph = [[] for j in range(N)]
  reverse_graph = [[] for j in range(N)]
  for j in range(M):
    d, c, l = map(int, input().split())
    graph[d-1].append(Node(c-1, l))
    reverse_graph[c-1].append(Node(d-1, l))
  distS = Dijkstra(graph, S-1)
  distT = Dijkstra(reverse_graph, T-1)
  minDist = distS[T-1]
  for j in range(K):
    u, v, q = map(int, input().split())
    minDist = min(minDist, distS[u-1] + q + distT[v-1], distS[v-1] + q + distT[u-1])
  if minDist == INF:
    print(-1)
  else:
    print(minDist)