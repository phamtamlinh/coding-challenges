/*
You are given integers K, M and a non-empty array A consisting of N integers. Every element of the array is not greater than M.

You should divide this array into K blocks of consecutive elements. The size of the block is any integer between 0 and N. Every element of the array should belong to some block.

The sum of the block from X to Y equals A[X] + A[X + 1] + ... + A[Y]. The sum of empty block equals 0.

The large sum is the maximal sum of any block.

For example, you are given integers K = 3, M = 5 and array A such that:

  A[0] = 2
  A[1] = 1
  A[2] = 5
  A[3] = 1
  A[4] = 2
  A[5] = 2
  A[6] = 2
The array can be divided, for example, into the following blocks:

[2, 1, 5, 1, 2, 2, 2], [], [] with a large sum of 15;
[2], [1, 5, 1, 2], [2, 2] with a large sum of 9;
[2, 1, 5], [], [1, 2, 2, 2] with a large sum of 8;
[2, 1], [5, 1], [2, 2, 2] with a large sum of 6.
The goal is to minimize the large sum. In the above example, 6 is the minimal large sum.

Write a function:

function solution(K, M, A);

that, given integers K, M and a non-empty array A consisting of N integers, returns the minimal large sum.

For example, given K = 3, M = 5 and array A such that:

  A[0] = 2
  A[1] = 1
  A[2] = 5
  A[3] = 1
  A[4] = 2
  A[5] = 2
  A[6] = 2
the function should return 6, as explained above.

Write an efficient algorithm for the following assumptions:

 * N and K are integers within the range [1..100,000];
 * M is an integer within the range [0..10,000];
 * each element of array A is an integer within the range [0..M].
*/

function solution(K, M, A) {
  let lower = Math.max(...A);
  let upper = A.reduce((a, b) => (a + b), 0);
  let mid = 0;
  let smallestSum = upper;
  if (K == 1) {
    return upper;
  }
  if (K >= A.length) {
    return lower;
  }
  while (lower <= upper) {
    mid = Math.floor((lower + upper) / 2);
    let [count, sum] = countBlock(A, mid);
    console.log(`upper ${upper} lower ${lower} mid ${mid} count ${count} sum ${sum}`)
    if (count > K) {
      lower = mid + 1;
    } else if (count <= K) {
      upper = mid - 1;
      smallestSum = sum;
    }
  }
  return smallestSum;
}

function countBlock(arr, maxSum) {
  let sum = arr[0];
  let count = 1;
  let calMaxSum = 0;
  for (let i = 1; i < arr.length; i++) {
    if (sum + arr[i] > maxSum) {
      count++;
      if (sum > calMaxSum) {
        calMaxSum = sum;
      }
      sum = arr[i];
    } else {
      sum += arr[i];
    }
  }
  if (sum > calMaxSum) {
    calMaxSum = sum;
  }
  return [count, calMaxSum];
}

let count = solution(5, 99, [0, 0, 0, 98, 0, 0, 99, 0, 0, 0, 0, 0])
console.log(count)