# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return true if you can finish all courses. Otherwise, return false.

 

# Example 1:

# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: true
# Explanation: There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0. So it is possible.
# Example 2:

# Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
# Output: false
# Explanation: There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
 

# Constraints:

# 1 <= numCourses <= 2000
# 0 <= prerequisites.length <= 5000
# prerequisites[i].length == 2
# 0 <= ai, bi < numCourses
# All the pairs prerequisites[i] are unique.

def dfs(u, graph, visited, result, is_cycled):
    visited[u] = 1
    # print('u', u)
    # print(visited)
    for v in graph[u]:
        if visited[v] == 0:
            is_cycled = dfs(v, graph, visited, result, is_cycled)
        elif visited[v] == 1:
            is_cycled = True
    result.append(u)
    visited[u] = 2
    # print(visited)
    return is_cycled

def topologicalSort(graph, result):
    visited = [0] * len(graph)
    is_cycled = False
    for i in range(len(graph)):
        if visited[i] == 0:
            is_cycled = dfs(i, graph, visited, result, is_cycled)
    # print(graph)
    # print(result)
    # print(visited)
    # print(is_cycled)
    return is_cycled

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        result = []
        for i in range(len(prerequisites)):
            [u, v] = prerequisites[i]
            graph[v].append(u)
        return not topologicalSort(graph, result)