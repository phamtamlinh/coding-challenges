function solution (A) {
  A.sort((a, b) => a - b);
  let result = (A.length) ? 1 : 0;
  for (let i = 1; i < A.length; i++ ) {
    if (A[i] != A[i-1]) result++;
  }
  return result;
}