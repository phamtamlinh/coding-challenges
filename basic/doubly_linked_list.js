const DoublyLinkedListNode = class {
  constructor(nodeData) {
    this.data = nodeData;
    this.next = null;
    this.back = null;
  }
}

const DoublyLinkedList = class {
  constuctor() {
    this.head = null;
    this.tail = null;
  }

  insertNode(nodeData) {
    const node = new DoublyLinkedListNode(nodeData);
    if (this.head == null) {
      this.head = node;
    } else {
      this.tail.next = node;
      node.back = this.tail;
    }
    this.tail = node;
  }
}

const arr = [5, 2, 6, 3, 6, 7];

const llist = new DoublyLinkedList();

arr.forEach(a => llist.insertNode(a));

const head = llist.head;
let secondNode = head.next;

console.log(secondNode);