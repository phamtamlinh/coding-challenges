# Well, the annual technical symposium of Department of Computer Technology is around the corner. All that we need, to make it a grand success is Publicity among the peer groups (Of course the sponsors too). We decided to share the job between the student groups. As per the plan we decided to meet people in person and influence them to attend Prayatna. But to meet them we have to go to various student groups. To do so, we had to cut our classes. But being studious, the students refused to cut more classes. Instead of meeting every one in person we decided to meet few people such that the person to whom we pass the news will spread it to all his friends. And those friends will pass it to other friends and so on. Your task is to find the number of people to be met by the organizers to spread the news.

# Input
# First line of input is T - test cases. Followed by N, the number of peers in the testcase (0 to N-1). Followed by the number of friend description E. Following are E descriptions of type a b denoting a friends with b. If a is friends with b then b is friends with a.

# Constraints
# T <= 10
# 2 <= N <= 100000
# 0 <= E <= N/2

# Output
# Output contains T line, the number of people, the organizers have to meet in person for each test case.

# Example
# input
# 2
# 4
# 2
# 0 1
# 1 2
# 3
# 0
# output
# 2
# 3

def parseGraph(N, A):
  graph = [[] for i in range(N)]
  for i in range(len(A)):
    u, v = map(int, A[i].split())
    graph[u].append(v)
    graph[v].append(u)
  return graph

def DFS(graph, S, N, student):
  s = []
  s.append(S)
  student[S] = True

  while len(s) > 0:
    u = s.pop()
    for v in graph[u]:
      if not student[v]:
        s.append(v)
        student[v] = True

def test(N, A):
  graph = parseGraph(N, A)
  student = [False for i in range(N)]
  count = 0
  for i in range(N):
    if not student[i]:
      count += 1
      DFS(graph, i, N, student)
  return count
 
T = int(input())
result = []
for i in range(T):
  N = int(input())
  E = int(input())
  A = [input() for i in range(E)]
  r = test(N, A)
  result.append(r)
for r in result:
  print(r)