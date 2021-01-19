class MinHeap {
  constructor() {
    this.heap = [];
  }
  getMin() {
    return this.heap[0];
  }
  insert(node) {
    this.heap.push(node);
    
    if (this.heap.length > 0) {
      let currentIndex = this.heap.length - 1;
      while(currentIndex > 0 && this.heap[Math.floor(currentIndex/2)] > this.heap[currentIndex]) {
        let parentIndex = Math.floor(currentIndex/2);
        [this.heap[parentIndex], this.heap[currentIndex]] = [this.heap[currentIndex], this.heap[parentIndex]];
        currentIndex = parentIndex;
      }
    }
  }
}