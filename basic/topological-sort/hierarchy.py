# A group of graduated students decided to establish a company; however, they don't agree on who is going to be who's boss.

# Generally, one of the students will be the main boss, and each of the other students will have exactly one boss (and that boss, if he is not the main boss, will have a boss of his own too). Every boss will have a strictly greater salary than all of his subordinates - therefore, there are no cycles. Therefore, the hierarchy of the company can be represented as a rooted tree.

# In order to agree on who is going to be who's boss, they've chosen KK most successful students, and each of them has given a statement: I want to be the superior of him, him, and him (they could be successful or unsuccessful). And what does it mean to be a superior? It means to be the boss, or to be one of the boss' superiors (therefore, a superior of a student is not necessary his direct boss).

# Help this immature company and create a hierarchy that will satisfy all of the successful students' wishes. A solution, not necessary unique, will exist in all of the test data.

# Dữ liệu nhập
# In the first line of input, read positive integers N (N≤100000), total number of students, and K (K < N), the number of successful students. All students are numbered 1..N, while the successful ones are numbered 1..K. Then follow K lines. In A^{th} of these lines, first read an integer W (the number of wishes of the student A, 1≤W≤10), and then W integers from the range [1, N] which denote students which student AA wants to be superior to.

# Dữ liệu xuất
# Output N integers. The A^{th} of these integers should be 0 if student A is the main boss, and else it should represent the boss of the student A.

# Ví dụ
# inputcopy
# 4 2
# 1 3
# 2 3 4
# outputcopy
# 4
# 0
# 1
# 2
# inputcopy
# 7 4
# 2 2 3
# 1 6
# 1 7
# 2 1 2
# outputcopy
# 4
# 7
# 1
# 5
# 0
# 2
# 3

def dfs(u, graph, visited, result):
  visited[u] = True
  for v in graph[u]:
    if not visited[v]:
      dfs(v, graph, visited, result)
  result.append(u)

def topologicalSort(graph, result):
  visited = [False] * (N+1)
  for i in range(1, N+1):
    if not visited[i]:
      dfs(i, graph, visited, result)

N, K = map(int, input().split())
graph = [[] for i in range(N+1)]
result = []
for i in range(1, K+1):
  W, *A = list(map(int, input().split()))
  for a in A:
    graph[i].append(a)

# print(graph)
topologicalSort(graph, result)
response = [0] * (N+1)
for i in range(0, N-1):
  response[result[i]] = result[i+1]
for i in range(1, N+1):
  print(response[i])