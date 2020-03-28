function solution(N, A) {
    let result = Array(N).fill(0)
    let max = 0
    let setMax = 0
    for (let X of A) {
        if (X <= N && result[X-1] < setMax) {
            result[X-1] = setMax
        }
        if (X <= N) {
            result[X-1]++
            max = (result[X-1] > max) ? result[X-1] : max
        } else if (X == N+1) {
            setMax = max
        }
    }
    for (let i in result) {
        if (result[i] < setMax) {
            result[i] = setMax
        }
    }
    return result
}
