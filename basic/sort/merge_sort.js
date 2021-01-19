function mergeSort(arr) {
  if (arr.length>1) {
    let mid = Math.floor(arr.length/2)
    let leftArr = arr.slice(0, mid)
    let rightArr = arr.slice(mid)
    mergeSort(leftArr)
    mergeSort(rightArr)
    let i = j = k = 0
    while(i < leftArr.length && j < rightArr.length) {
      if(leftArr[i] < rightArr[j]) {
        // arr[i] = leftArr[i]
        arr[k] = leftArr[i]
        k++
        i++
      } else {
        arr[k] = rightArr[j]
        k++
        j++
      }
    }
    while (j < rightArr.length) {
      arr[k] = rightArr[j]
      j++
      k++
    }
    while (i < leftArr.length) {
      arr[k] = leftArr[i]
      i++
      k++
    }
  }
}

let arr = [38, 43, 27, 3, 9, 82, 10]
mergeSort(arr)
console.log(arr)