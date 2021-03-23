# Find the minimum spanning tree of the graph.

# Input
# On the first line there will be two integers N - the number of nodes and M - the number of edges. (1 <= N <= 10000), (1 <= M <= 100000)

# M lines follow with three integers i j k on each line representing an edge between node i and j with weight k. The IDs of the nodes are between 1 and n inclusive. The weight of each edge will be <= 1000000.

# Output
# Single number representing the total weight of the minimum spanning tree on this graph. There will be only one possible MST.

# Example
# input
# 4 5
# 1 2 10
# 2 3 15
# 1 3 5
# 4 2 2
# 4 3 40
# output
# 17

import queue
INF = 10**9

class Node:
  def __init__(self, id, dist):
    self.dist = dist
    self.id = id
  def __lt__(self, other):
    return self.dist <= other.dist

def prims(src):
  pq = queue.PriorityQueue()
  pq.put(Node(src, 0))
  dist[src] = 0
  while not pq.empty():
    top = pq.get()
    u = top.id
    uW = top.dist
    if dist[u] != uW:
      continue
    visited[u] = True
    for neighbor in graph[u]:
      v = neighbor.id
      w = neighbor.dist
      if visited[v] == False and w < dist[v]:
        dist[v] = w
        pq.put(Node(v, w))
        path[v] = u
  minWeight = 0
  for w in dist:
    minWeight += w
  return minWeight

N, M = map(int, input().split())
graph = [[] for i in range(N)]
dist = [INF for i in range(N)]
path = [-1 for i in range(N)]
visited = [False for i in range(N)]
for m in range(M):
  i, j, k = map(int, input().split())
  graph[i-1].append(Node(j-1, k))
  graph[j-1].append(Node(i-1, k))
mW = prims(0)
print(mW)