function solution(A) {
  let arr = Array(A.length+1).fill(0);
  for (let i = 0; i < A.length; i++) {
    arr[i+1] = A[i] + arr[i];
  }
  let P = 0;
  let min;
  for (let i = 0; i < A.length-1; i++) {
    let ave2 = (arr[i+2]-arr[i])/2;
    if (!min) {
      min = ave2;
    }
    let ave3 = min;
    if (i<A.length-2) {
      ave3 = (arr[i + 3] - arr[i]) / 3;
    }
    if( min > ave2 ) {
      min = ave2;
      P = i;
    }
    if (min > ave3) {
      min = ave3;
      P = i;
    }
  }
  return P;
}

