# OR in Matrix
# Let's define logical OR as an operation on two logical values (i. e. values that belong to the set {0, 1}) that is equal to 1 if either or both of the logical values is set to 1, otherwise it is 0. We can define logical OR of three or more logical values in the same manner:

# a1 OR a2 OR ... OR ak where ai is 0 or 1, it is 1 if ai = 1, otherwise it is equal to 0.

# Nam has a matrix A consisting of m rows and nn columns. The rows are numbered from 1 to m, columns are numbered from 1 to n. Element at row i (1≤i≤m) and column j (1≤j≤n) is denoted as Aij. All elements of A are either 0 or 1. From matrix A, Nam creates another matrix B of the same size using formula:

# Bij = Ai1 OR Ai2 OR ... OR A1j OR ... OR Amj

# Bij is OR of all elements in row i and column j of matrix A)

# Nam gives you matrix B and challenges you to guess matrix A. Although Nam is smart, he could probably make a mistake while calculating matrix B, since size of A can be large.

# Dữ liệu nhập
# The first line contains two integer m and n (1≤m,n≤100), number of rows and number of columns of matrices respectively.

# The next mm lines each contain nn integers separated by spaces describing rows of matrix B (each element of B is either 0 or 1).

# Dữ liệu xuất
# In the first line, print "NO" if Nam has made a mistake when calculating B, otherwise print "YES". If the first line is "YES", then also print mm rows consisting of nn integers representing matrix A that can produce given matrix B. If there are several solutions print any one.

# Ví dụ
# inputcopy
# 2 3
# 0 1 0
# 1 1 1
# outputcopy
# YES
# 0 0 0
# 0 1 0
# inputcopy
# 2 2
# 1 0
# 0 0
# outputcopy
# NO

m, n = map(int, input().split())
B = [[] for _ in range(m)]
A = [[1 for _ in range(n)] for _ in range(m)]
for _ in range(m):
  B[_] = list(map(int, input().split()))
for i in range(m):
  for j in range(n):
    if B[i][j] == 0:
      for k in range(n):
        A[i][k] = 0
      for k in range(m):
        A[k][j] = 0
result = 'YES'
for i in range(m):
  for j in range(n):
    if B[i][j] == 1:
      flag = False
      for k in range(n):
        if A[i][k] == 1:
          flag = True
      for k in range(m):
        if A[k][j] == 1:
          flag = True
      if flag == False:
        result = 'NO'
        break
print(result)
if result == 'YES':
  for i in range(m):
    for j in range(n):
    	print(A[i][j], end=' ')
    print()
