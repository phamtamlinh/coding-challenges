# Sandro is a well organised person. Every day he makes a list of things which need to be done and enumerates them from 1 to n. However, some things need to be done before others. In this task you have to find out whether Sandro can solve all his duties and if so, print the correct order.

# Dữ liệu nhập
# In the first line you are given an integer n and m (1 <= n <= 10000, 1 <= m <= 1000000). On the next m lines there are two distinct integers x and y, (1 <= x, y <= n) describing that job x needs to be done before job y.

# Dữ liệu xuất
# Print Sandro fails. if Sandro cannot complete all his duties on the list. If there is a solution print the correct ordering, the jobs to be done separated by a whitespace. If there are multiple solutions print the one, whose first number is smallest, if there are still multiple solutions, print the one whose second number is smallest, and so on.

# Ví dụ
# inputcopy
# 8 9
# 1 4
# 1 2
# 4 2
# 4 3
# 3 2
# 5 2
# 3 5
# 8 2
# 8 6
# outputcopy
# 1 4 3 5 7 8 2 6 
# inputcopy
# 2 2
# 1 2
# 2 1
# outputcopy
# Sandro fails.

# use heapq so smallest job will be added to top
import heapq
def topologicalSort(graph, result):
  indegree = [0] * V
  zero_indegree = []
  for u in range(V):
    for v in graph[u]:
      indegree[v] += 1
  for i in range(V):
    if indegree[i] == 0:
      # zero_indegree.put(i)
      heapq.heappush(zero_indegree, i)
  while len(zero_indegree):
    # u = zero_indegree.get()
    u = heapq.heappop(zero_indegree)
    result.append(u)
    for v in graph[u]:
      indegree[v] -= 1
      if indegree[v] == 0:
        # zero_indegree.put(v)
        heapq.heappush(zero_indegree, v)
  for i in range(V):
    if indegree[i] != 0:
      return False
  return True

V, E = map(int, input().split())
graph = [[] for i in range(V)]
result = []
for i in range(E):
  u, v = map(int, input().split())
  graph[u-1].append(v-1)
if (topologicalSort(graph, result)):
  for i in range(V):
    print(result[i]+1, end=" ")
else:
  print('Sandro fails.')
