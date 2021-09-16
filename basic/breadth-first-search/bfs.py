#!/bin/python3

import math
import os
import random
import re
import sys
from queue import Queue

#
# Complete the 'bfs' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#  3. 2D_INTEGER_ARRAY edges
#  4. INTEGER s
#

def calPath(path, s, f):
    dist = 0
    if path[f] == -1:
        return -1
    while True:
        dist = dist + 1
        f = path[f]
        if f == s:
            break
    return dist * 6

def bfs(n, m, edges, s):
    visited = [False for i in range(n+1)]
    graph = [[] for i in range(n+1)]
    path = [-1 for i in range(n+1)]
    result = []
    for edge in edges:
        graph[edge[0]].append(edge[1])
    
    q = Queue()
    visited[s] = True
    q.put(s)
    while not q.empty():
        u = q.get()
        for v in graph[u]:
            if not visited[v]:
                visited[v] = True
                q.put(v)
                path[v] = u
    for j in range(1, n+1):
        if j != s:
            dist = calPath(path, s, j)
            result.append(dist)
    return result
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        edges = []

        for _ in range(m):
            edges.append(list(map(int, input().rstrip().split())))

        s = int(input().strip())

        result = bfs(n, m, edges, s)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
