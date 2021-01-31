# The government of Spoj_land has selected number of locations in the city for road construction and numbered those locations as 0, 1, 2, 3, ..., 500.

# Now, they want to construct roads between various pairs of location (say A and B) and have fixed the cost for travelling between those pair of locations from either end as W unit.

# Now, Rohit being a curious boy wants to find the minimum cost for travelling from location U (source) to Q number of other locations (destination).

# Input
# First line contains N, the number of roads that government constructed.

# Next N line contains three integers A, B and W. A and B represent the locations between which the road was constructed and W is the fixed cost for travelling from A to B or from B to A.

# Next line contains an integer U from where Rohit wants to travel to other locations.

# Next line contains Q, the number of queries (finding cost) that he wants to perform.

# Next Q lines contain an integer V (destination) for which minimum cost is to be found from U.

# Constraints
# 1 <= N <= 500
# 0 <= A, B <= 500
# 1 <= W <= 100
# 0 <= U, V <= 500
# 1 <= Q <= 500

# Output
# Print the required answer in each line.

# If he can't travel from location U to V by any means then, print 'NO PATH' without quotes.

# Example
# Input
# 7
# 0 1 4
# 0 3 8
# 1 4 1
# 1 2 2
# 4 2 3
# 2 5 3
# 3 4 2
# 0
# 4
# 1
# 4
# 5
# 7
# Output
# 4
# 5
# 9
# NO PATH
# Explain
# Query #1
# 0->1: cost = 4

# Query #2
# 0->4 = 0->1->4 cost = 4 + 1 = 5

# Query #3
# 0->5 = 0->1->2->5 cost = 4 + 2 + 3 = 9

# Query #4
# 0->7 . No path exists between 0 and 7

import queue

INF = int(1e9)

class Node:
  def __init__(self, id, dist):
    self.dist = dist
    self.id = id
  def __lt__(self, other):
    return self.dist <= other.dist
  
def Dijkstra(s, N, graph):
  dist = [INF for i in range(501)]
  path = [-1 for i in range(501)]
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

def test():
  N = int(input())
  graph = [[] for i in range(501)]
  for i in range(N):
    d = list(map(int, input().split()))
    graph[d[0]].append(Node(d[1], d[2]))
    graph[d[1]].append(Node(d[0], d[2]))
  
  U = int(input())
  Q = int(input())
  dist = Dijkstra(U, N, graph)
  for i in range(Q):
    V = int(input())
    if dist[V] < INF:
      print(dist[V])
    else:
      print("NO PATH")
test()