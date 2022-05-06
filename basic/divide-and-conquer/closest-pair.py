# Given a set of points in a two dimensional space, you will have to find the distance between the closest two points.

# Dữ liệu nhập
# The input contains several testcases.

# Each testcase starts with an integer NN (0 \le N \le 100000≤N≤10000), which denotes the number of points in this test.

# The next NN line contains the coordinates of NN two-dimensional points. The first of the two numbers denotes the XX-coordinate and the latter denotes the YY-coordinate.

# The input is terminated by a test in which N = 0N=0. This test should not be processed.

# The value of the coordinates will be less than 4000040000 and non-negative.

# Dữ liệu xuất
# For each test produce a single line of output containing a floating point number (with four digits after the decimal point) denoting the distance between the closest two points. If there is no such two points whose distance is less than 1000010000, print the line INFINITY.

# Ví dụ
# inputcopy
# 3
# 0 0
# 10000 10000
# 20000 20000
# 5
# 0 2
# 6 67
# 43 71
# 39 107
# 189 140
# 0
# outputcopy
# INFINITY
# 36.2215

import math
INF = 1e9

class Point:
  def __init__(self, x=0, y=0):
    self.x = x
    self.y = y
def distance(p1, p2):
  x = p1.x - p2.x
  y = p1.y - p2.y
  return (x*x + y*y) ** 0.5

def stripCloset(point_set, left, right, mid, dist_min):
  point_mid = point_set[mid]
  split_points = []
  for i in range(left, right):
    if abs(point_set[i].x - point_set[mid].x <= dist_min):
      split_points.append(point_set[i])
  split_points.sort(key=lambda p: p.y)
  smallest = dist_min
  l = len(split_points)
  for i in range(0, l):
    for j in range(i+1, l):
      if not (split_points[j].y - split_points[i].y < smallest):
        break
      d = distance(split_points[i], split_points[j])
      smallest = min(smallest, d)
  return smallest
  
def bruteForce(point_set, left, right):
  min_dist = INF
  for i in range(left, right):
    for j in range(i+1, right):
      min_dist = min(min_dist, distance(point_set[i], point_set[j]))
  return min_dist

def minimalDistance(point_set, left, right):
  if right - left <= 3:
    return bruteForce(point_set, left, right)
  mid = (left + right)//2
  dist_left = minimalDistance(point_set, left, mid)
  dist_right = minimalDistance(point_set, mid+1, right)
  dist_min = min(dist_left, dist_right)
  return min(dist_min, stripCloset(point_set, left, right, mid, dist_min))

while True:
  N = int(input())
  if N == 0:
    break
  point_set = []
  for i in range(0, N):
    x, y = map(int, input().split())
    point_set.append(Point(x, y))

  point_set.sort(key=lambda point: point.x)
  ans = minimalDistance(point_set, 0, N)
  if ans >= 10000:
    print('INFINITY')
  else:
    print(format(ans, '.4f'))
