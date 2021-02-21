# Dhaka city is getting crowded and noisy day by day. Certain roads always remain blocked in congestion. In order to convince people avoid shortest routes, and hence the crowded roads, to reach destination, the city authority has made a new plan. Each junction of the city is marked with a positive integer (<=20) denoting the busyness of the junction. Whenever someone goes from one junction (the source junction) to another (the destination junction), the city authority gets the amount (busyness of destination - busyness of source)^3 (that means the cube of the difference) from the traveler. The authority has appointed you to find out the minimum total amount that can be earned when someone intelligent goes from a certain junction (the zero point) to several others.

# Input
# Input starts with an integer T (<=50), denoting the number of test cases.

# Each case contains a blank line and an integer n (1<=n<=200) denoting the number of junctions. The next line contains n integers denoting the busyness of the junctions from 1 to n respectively. The next line contains an integer m, the number of roads in the city. Each of the next m lines (one for each road) contains two junction-numbers (source, destination) that the corresponding road connects (all roads are unidirectional). The next line contains the integer q, the number of queries. The next q lines each contain a destination junction-number. There can be at most one direct road from a junction to another junction.

# Output
# For each case, print the case number in a single line. Then print q lines, one for each query, each containing the minimum total earning when one travels from junction 1 (the zero point) to the given junction. However, for the queries that gives total earning less than 3, or if the destination is not reachable from the zero point, then print a ?

# Example
# input
# 2

# 5
# 6 7 8 9 10
# 6
# 1 2
# 2 3
# 3 4
# 1 5
# 5 4
# 4 5
# 2
# 4
# 5

# 2
# 10 10
# 1
# 1 2
# 1
# 2
# output
# Case 1:
# 3
# 4
# Case 2:
# ?

INF = 10**9

class Edge:
  def __init__(self, source, target, weight):
    self.source = source
    self.target = target
    self.weight = weight
  def __str__(self):
    return str(self.source) + " " + str(self.target) + " " + str(self.weight)

def BellmanFord(graph, s, n):
  dist = [INF for i in range(n)]
  path = [-1 for i in range(n)]
  dist[s] = 0
  for i in range(1, n):
    for j in range(len(graph)):
      u = graph[j].source
      v = graph[j].target
      w = graph[j].weight
      if (dist[u] != INF) and (dist[u] + w < dist[v]):
        dist[v] = dist[u] + w
        path[v] = u
  # we must run (n-1)*m times more so when it discovers negative weighted cycle, it will update dist[v] to -INF, m times can't detect it
  # we can run it or use BFS to find those nodes affected by NWC
  for i in range(1, n):
    for j in range(len(graph)):
      u = graph[j].source
      v = graph[j].target
      w = graph[j].weight
      if (dist[u] != INF) and (dist[u] + w < dist[v]):
        dist[v] = -INF
  return dist

T = int(input())
for i in range(T):
  input()
  n = int(input())
  graph = []
  arr = list(map(int, input().split()))
  m = int(input())
  for j in range(m):
    u, v = map(int, input().split())
    w = (arr[v-1]-arr[u-1])**3
    graph.append(Edge(u-1, v-1, w))
  q = int(input())
  dist = BellmanFord(graph, 0, n)
  print("Case " + str(i+1) + ":")
  for k in range(q):
    t = int(input())
    if dist[t-1] >= 3 and dist[t-1] != INF:
      print(dist[t-1])
    else:
      print("?")