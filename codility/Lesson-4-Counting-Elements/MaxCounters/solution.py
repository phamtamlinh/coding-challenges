def solution(N, A):
    result = [0]*N
    max = 0
    setMax = 0
    for i in range(len(A)):
        if A[i] <= N and result[A[i]-1] < setMax:
            result[A[i]-1] = setMax
        if A[i] <= N:
            result[A[i]-1] += 1
            if result[A[i]-1] > max: max = result[A[i]-1]
        elif A[i] == N+1:
            setMax = max
    for i in range(N):
        if result[i] < setMax:
            result[i] = setMax

    return result
