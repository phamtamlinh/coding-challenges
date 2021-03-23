# Given a knapsack with maximum capacity W, and a set S consisting of n items
# Each item i has some weight wi and benefit value bi (all wi, bi and W are integer values)
# Problem: How to pack the knapsack to achieve maximum total value of packed items?

# Example:
# values = [60, 100, 120]
# weights = [10, 20, 30]
# W = 50

# weight = 10, value = 60
# weight = 20, value = 100
# weight = 30, value = 120
# weight = (20+10), value = (100+60)
# weight = (30+10), value = (120+60)
# weight = (30+20), value = (120+100) -> solution

# http://cse.unl.edu/~goddard/Courses/CSCE310J/Lectures/Lecture8-DynamicProgramming.pdf
# https://www.geeksforgeeks.org/0-1-knapsack-problem-dp-10/

def knapSack(W, wt, val, n):
  K = [[0 for _ in range(W+1)] for _ in range(n+1)]
  for i in range(n+1):
    for w in range(W+1):
      if i == 0 or w == 0:
        K[i][w] = 0
      elif wt[i-1] <= w:
        K[i][w] = max(K[i-1][w], val[i-1] + K[i-1][w-wt[i-1]])
      else:
        K[i][w] = K[i-1][w]
  return K[n][W]

val = [60, 100, 120]
wt = [10, 20, 30]
W = 50
n = len(val)
print(knapSack(W, wt, val, n))