const SinglyLinkedListNode = class {
  constructor(nodeData) {
    this.data = nodeData;
    this.next = null;
  }
};

const SinglyLinkedList = class {
  construction() {
    this.head = null;
    this.tail = null;
  }

  insertNode(nodeData) {
    const node = new SinglyLinkedListNode (nodeData);

    if (this.head == null) {
      this.head = node;
    } else {
      this.tail.next = node;
    }
    this.tail = node
  }
};

const arr = [5,2,6,3,6,7];

const llist = new SinglyLinkedList();

arr.forEach(a => llist.insertNode(a));

console.log(llist);