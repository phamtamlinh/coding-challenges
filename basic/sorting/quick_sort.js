function partition(arr, low, high) {
  let pivot = arr[high - 1]
  let i = j = low
  while (j < high) {
    // console.log(`i: ${i} j:${j}`)
    // console.log(arr)
    if(arr[j] <= pivot) {
      // console.log("swap");
      [arr[i], arr[j]] = [arr[j], arr[i]]
      i++
    }
    j++
  }
  return i--
}

function quickSort(arr, low, high) {
  if(low < high) {
    index = partition(arr, low, high)
    quickSort(arr, low, index-1)
    quickSort(arr, index+1, high)
  }
}

let arr = [38, 27, 43, 3, 9, 82, 10]
n = arr.length
quickSort(arr, 0, n)
console.log(arr)