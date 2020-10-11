/***
You are given two non-empty arrays A and B consisting of N integers. These arrays represent N planks. More precisely, A[K] is the start and B[K] the end of the K−th plank.

Next, you are given a non-empty array C consisting of M integers. This array represents M nails. More precisely, C[I] is the position where you can hammer in the I−th nail.

We say that a plank (A[K], B[K]) is nailed if there exists a nail C[I] such that A[K] ≤ C[I] ≤ B[K].

The goal is to find the minimum number of nails that must be used until all the planks are nailed. In other words, you should find a value J such that all planks will be nailed after using only the first J nails. More precisely, for every plank (A[K], B[K]) such that 0 ≤ K < N, there should exist a nail C[I] such that I < J and A[K] ≤ C[I] ≤ B[K].

For example, given arrays A, B such that:

    A[0] = 1    B[0] = 4
    A[1] = 4    B[1] = 5
    A[2] = 5    B[2] = 9
    A[3] = 8    B[3] = 10
four planks are represented: [1, 4], [4, 5], [5, 9] and [8, 10].

Given array C such that:

    C[0] = 4
    C[1] = 6
    C[2] = 7
    C[3] = 10
    C[4] = 2
if we use the following nails:

0, then planks [1, 4] and [4, 5] will both be nailed.
0, 1, then planks [1, 4], [4, 5] and [5, 9] will be nailed.
0, 1, 2, then planks [1, 4], [4, 5] and [5, 9] will be nailed.
0, 1, 2, 3, then all the planks will be nailed.
Thus, four is the minimum number of nails that, used sequentially, allow all the planks to be nailed.

Write a function:

function solution(A, B, C);

that, given two non-empty arrays A and B consisting of N integers and a non-empty array C consisting of M integers, returns the minimum number of nails that, used sequentially, allow all the planks to be nailed.

If it is not possible to nail all the planks, the function should return −1.

For example, given arrays A, B, C such that:

    A[0] = 1    B[0] = 4
    A[1] = 4    B[1] = 5
    A[2] = 5    B[2] = 9
    A[3] = 8    B[3] = 10

    C[0] = 4
    C[1] = 6
    C[2] = 7
    C[3] = 10
    C[4] = 2
the function should return 4, as explained above.

Write an efficient algorithm for the following assumptions:

* N and M are integers within the range [1..30,000];
* each element of arrays A, B, C is an integer within the range [1..2*M];
* A[K] ≤ B[K].
*/

function solution(A, B, C) {
  let begin = 1;
  let end = C.length;
  let result = -1;

  while(begin <= end) {
    mid = Math.floor((begin + end) / 2);
    console.log(`mid ${mid}`);
    let min = check(A, B, C, mid);
    console.log(`min ${min}`)
    if (min) {
      end = mid - 1;
      result = min;
    } else {
      begin = mid + 1;
    }
  }
  return result;
}

function check(A, B, C, end) {
  let pointer = 0;
  let nail = 0;
  let min, max;
  for(let i = 0; i < end; i++) {
    if(min != undefined || C[i] < min) {
      min = C[i];
    }
    if (max != undefined || C[i] > max) {
      max = C[i]
    }
    console.log(`min ${min} - max ${max}`);
    for (pointer; pointer < A.length; pointer++) {
      console.log(`A ${A[pointer]} - B ${B[pointer]} - C ${C[i]}`)
      if (A[pointer] <= C[i] && B[pointer] >= C[i]) {
        console.log(`index ${pointer}`);
        nail++;
      } else {
        break;
      }
    }
  }

  if (nail == A.length) {
    return end;
  } else {
    return 0;
  }
}

let A = [ 28, 18, 43, 15, 26, 18, 21, 49, 6, 23, 12, 18, 50, 17, 31, 21, 37, 23, 9, 22, 21, 40, 29, 10, 34, 15, 26, 11, 21, 40, 26, 38, 38, 30, 33, 20, 31, 39, 5, 47, 19, 7, 8, 18, 4, 20, 21, 33, 24, 47, 33, 17, 44, 35, 49, 37, 49, 11, 14, 49, 2, 47, 6, 7, 8, 46, 48, 44, 37, 38, 16, 1, 32, 45, 48, 26, 1, 9, 23, 12, 2, 10, 25, 7, 6, 9, 2, 40, 44, 11, 32, 44, 13, 17, 45, 39, 32, 40, 29, 16 ];
let B = [ 55, 32, 44, 48, 36, 31, 41, 81, 56, 46, 62, 68, 62, 20, 39, 63, 67, 69, 58, 55, 48, 43, 30, 51, 68, 53, 54, 45, 53, 85, 31, 63, 53, 72, 77, 32, 35, 51, 21, 86, 39, 45, 23, 44, 13, 52, 47, 76, 72, 73, 36, 64, 92, 59, 73, 84, 61, 24, 49, 83, 36, 89, 72, 28, 19, 56, 66, 66, 74, 69, 42, 20, 63, 64, 88, 58, 36, 28, 49, 48, 50, 36, 41, 42, 12, 26, 3, 68, 56, 30, 72, 76, 14, 39, 45, 80, 57, 83, 42, 57 ];
let C = [ 55, 35, 85, 29, 52, 35, 42, 98, 11, 45, 23, 35, 100, 33, 61, 42, 74, 45, 18, 44, 41, 80, 57, 20, 68, 30, 52, 22, 42, 79, 52, 76, 76, 59, 65, 40, 62, 78, 10, 94, 37, 14, 16, 35, 7, 40, 42, 66, 47, 94, 66, 33, 88, 70, 97, 74, 97, 21, 28, 98, 3, 93, 92, 14, 16, 92, 96, 87, 73, 76, 31, 1, 63, 89, 95, 52, 1, 18, 45, 24, 3, 20, 50, 13, 12, 17, 4, 79, 87, 21, 64, 88, 25, 34, 89, 77, 63, 80, 58, 32, 69, 79, 6, 33, 30, 89, 29, 68, 44, 38, 50, 90, 66, 39, 16, 35, 48, 65, 100, 33, 95, 92, 45, 23, 24, 93, 18, 65, 66, 17, 4, 64, 6, 55, 98, 47, 32, 11, 31, 33, 12, 71, 61, 72, 11, 26, 93, 1, 37, 82, 23, 23, 64, 26, 34, 40, 30, 66, 74, 77, 99, 8, 26, 99, 80, 77, 23, 13, 28, 90, 76, 37, 66, 74, 29, 11, 82, 71, 81, 75, 37, 66, 37, 91, 13, 70, 35, 91, 81, 18, 2, 24, 97, 77, 71, 21, 22, 45, 54, 62, 6, 85, 25, 72, 32, 30, 88, 22, 51, 88, 83, 72, 25, 63, 48, 31, 78, 68, 90, 43, 15, 28, 74, 71, 65, 40, 58, 7, 10, 81, 12, 63, 30, 18, 79, 89, 32, 16, 47, 12, 97, 3, 51, 17, 1, 100, 69, 71, 77, 79, 61, 67, 32, 11, 73, 74, 74, 65, 9, 65, 9, 88, 1, 27, 54, 87, 66, 14, 73, 21, 34, 37, 80, 21, 33, 29, 25, 22, 39, 18, 26, 12, 59, 70, 24, 45, 61, 98, 97, 12, 95, 81, 23, 20, 51, 29, 32, 41, 55, 55 ];

console.log(solution(A, B, C));