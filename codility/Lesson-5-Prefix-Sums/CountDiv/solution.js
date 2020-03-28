function solution(A, B, K) {
  let first, last;
  if (A % K === 0) {
    first = A / K - 1;
  } else {
    first = Math.floor(A / K);
  }
  last = Math.floor(B / K);
  return last - first;
}