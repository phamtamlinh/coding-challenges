"""
There are many algorithms to generate maze (Maze Generation Algorithm). After generating the maze we’ve to validate whether it’s a valid maze or not. A valid maze has exactly one entry point and exactly one exit point (exactly 22 openings in the edges) and there must be atleast one path from the entry point to exit point.

Given a maze, just find whether the maze is "valid" or "invalid".

Input
The first line consists of an integer T, the number of test cases. Then for each test case, the first line consists of two integers M and N, the number of rows and columns in the maze. Then contains the description of the matrix M of order MxN. M[i][j] = '#' represents a wall and M[i][j] = '.' represents a space.

Constraints:
* 1 <= T <= 10000
* 1 <= M <= 20
* 1 <= N <= 20

Output
For each test case find whether the maze is "valid" or "invalid".

INPUT

6
4 4
####
#...
#.##
#.##
5 5
#.###
#..##
##..#
#.#.#
###.#
1 1
.
5 1
#
#
.
.
#
2 2
#.
.#
3 4
#..#
#.##
#.##

OUTPUT

valid
valid
invalid
valid
invalid
invalid
"""

from queue import Queue

def parseMap(M, W, H):
  MAX = W * H
  graph = [[] for i in range(MAX)]
  start, end, count = -1, -1, 0
  for i in range(H):
    for j in range(W):
      index = j + W*i
      if M[i][j] == '.':
        if i == 0 or i == H-1 or j == 0 or j == W-1:
          count += 1
          if start < 0:
            start = index
          elif end < 0:
            end = index
        if i > 1 and M[i-1][j] == '.':
          nIndex = j + (i-1)*W
          graph[index].append(nIndex)
          graph[nIndex].append(index)
        if j < W-1 and M[i][j+1] == '.':
          nIndex = j+1 + i*W
          graph[index].append(nIndex)
          graph[nIndex].append(index)
        if j > 0 and M[i][j-1] == '.':
          nIndex = j-1 + i*W
          graph[index].append(nIndex)
          graph[nIndex].append(index)
        if i < H-1 and M[i+1][j] == '.':
          nIndex = j + (i+1)*W
          graph[index].append(nIndex)
          graph[nIndex].append(index)
  if count != 2:
    return graph, -1, -1
  return graph, start, end

def BFS(graph, S):
  path = [-1 for i in range(len(graph))]
  visited = [False for i in range(len(graph))]
  q = Queue()
  visited[S] = True
  q.put(S)
  while not q.empty():
    u = q.get()
    for v in graph[u]:
      if not visited[v]:
        visited[v] = True
        q.put(v)
        path[v] = u
  return path, visited

def checkPath(path, start, end):
  if path[end] == -1:
    return "invalid"
  while True:
    end = path[end]
    if end == start:
      return "valid"

T = int(input())
result = []
for i in range(T):
  M, N = map(int, input().split(" "))
  MAP = [list(input()) for i in range(M)]
  graph, start, end = parseMap(MAP, N, M)
  if start < 0 or end < 0:
    result.append("invalid")
    continue
  path, visited = BFS(graph, start)
  r = checkPath(path, start, end)
  result.append(r)

for r in result:
  print(r)