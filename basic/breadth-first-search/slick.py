# A maritime accident has caused oil to spill onto the seas of Felipistonia, which is a major natural disaster. The Felipistonia's government wants to clean up this mess before more damage occurs. To do this, they first have to know how serious was the accident and the amount of oil that has been spilled into the sea. The only instrument the Felipistonia's government has to get information of the magnitude of this disaster, is the use of satellite images. With these images they can estimate how much money they have to spend to clean this mess. For this, the number of slicks in the seas and the size of each slick must be know. A slick is a patch of oil floating on water. Unfortunately, the Felipistonia's people are not very bright, so they have hired you to help them process the image.

# The image can be transformed to 0's and 1's with 1 is spilled oil area and 0 is not. Given the binary matrix, your job is to count the number of slicks in the ocean and their corresponding size. Two adjacent pixels in the image are considered to be in the same slick if they are in the same row or the same column.

# Input
# The input contains several test cases, each one corresponding to a different satellite image. The first line of each case contains two integers that indicate the number of rows (N) and columns (M) in the image (1 <= N,M <= 250). Then N lines follows with M integers each, containing the information of the image.

# The end of input is indicated by a test case with N = M = 0. This case should not be processed.

# Output
# For each image, output the number of slicks in the sea. Additionally, output the size of each slick in ascending order and the number of slicks of that size.

# Example
# input
# 10 10
# 1 1 1 1 1 1 1 1 1 1
# 1 1 1 1 0 0 0 0 0 0
# 1 1 1 0 0 0 0 1 1 1
# 1 1 0 0 1 0 0 1 1 1
# 1 0 1 0 0 1 1 0 0 0
# 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0
# 1 1 1 1 1 1 1 1 1 1
# 0 0 0 0 0 0 0 0 0 0
# 1 1 1 1 1 1 1 1 1 1
# 0 0
# output
# 7
# 1 2
# 2 1
# 6 1
# 10 2
# 20 1

from queue import Queue

def parseMap(M, W, H):
  MAX = W * H
  graph = [[] for i in range(MAX)]
  nodes = [False for i in range(MAX)]
  for i in range(H):
    for j in range(W):
      if M[i][j] == '1':
        index = j + W*i
        nodes[index] = True
        if i > 0 and M[i-1][j] == '1':
          nIndex = j + (i-1)*W
          graph[index].append(nIndex)
        if j < W-1 and M[i][j+1] == '1':
          nIndex = j+1 + i*W
          graph[index].append(nIndex)
        if j > 0 and M[i][j-1] == '1':
          nIndex = j-1 + i*W
          graph[index].append(nIndex)
        if i < H-1 and M[i+1][j] == '1':
          nIndex = j + (i+1)*W
          graph[index].append(nIndex)
  return graph, nodes

def BFS(graph, S, nodes):
  q = Queue()
  nodes[S] = False
  q.put(S)
  count = 1

  while not q.empty():
    u = q.get()
    for v in graph[u]:
      if nodes[v]:
        nodes[v] = False
        q.put(v)
        count += 1

  return count

def test(N, M):
  m = [input().split() for i in range(N)]
  result = []
  r = []
  graph, nodes = parseMap(m, M, N)
  i = 0
  while i < N*M:
    if nodes[i]:
      count = BFS(graph, i, nodes)
      result.append(count)
    i += 1
  r.append(len(result))
  c = {}
  for i in range(0, len(result)):
    if result[i] not in c:
      c[result[i]] = 1
    else:
      c[result[i]] += 1
  d = sorted(c.items(),key = lambda i: i[0])
  for k in d:
    r.append(str(k[0]) + " " + str(k[1]))

  return r

result = []
while True:
  N, M = map(int, input().split(" "))
  if (N > 0 and M > 0):
    r = test(N, M)
    result.append(r)
  else:
    break

for r in result:
  for j in r:
    print(j)