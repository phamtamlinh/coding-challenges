function solution(A) {
  A.sort((a, b) => a - b);
  let N = A.length;
  let prodNegA = A[0] * A[1] * A[N - 1];
  let prodPosA = A[N - 3] * A[N - 2] * A[N - 1];

  return (prodNegA > prodPosA) ? prodNegA : prodPosA;
}