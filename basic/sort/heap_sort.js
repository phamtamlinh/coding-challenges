function heapify(arr, n, i) {
  let l = 2*i+1
  let r = 2*i+2
  let largest = i
  if(l < n && arr[i] < arr[l]) {
    largest = l
  }
  if(r < n && arr[largest] < arr[r]) {
    largest = r
  }
  if(largest != i) {
    // swap
    [arr[largest], arr[i]] = [arr[i], arr[largest]]
    heapify(arr, n, largest)
  }
}

function heapSort(arr) {
  let n = arr.length
  for (let i = Math.ceil(n / 2) - 1; i >= 0; i--) {
    heapify(arr, n, i)
  }
  for(let i = n-1; i>=0; i--) {
    [arr[0], arr[i]] = [arr[i], arr[0]]
    heapify(arr, i, 0)
  }
}

let arr = [38, 27, 43, 3, 9, 82, 10]
heapSort(arr)
console.log(arr)