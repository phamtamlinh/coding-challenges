function solution(A) {
  let max = 0;
  for (let i = 0; i < A.length; i++) {
    max = (A[i] > max) ? A[i] : max;
  }
  if (max < 1) return 1;
  let len = (A.length > max) ? A.length : max;
  let arr = Array(len).fill(0);
  for (let i = 0; i < A.length; i++) {
    if(A[i] > 0) arr[A[i] - 1]++;
  }
  for (let i = 0; i < len; i++) {
    if (arr[i] < 1) return i + 1;
  }
  return max + 1;
}
