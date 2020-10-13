class Node {
  constructor(data) {
    this.data = data;
    this.left = null;
    this.right = null;
  }
}

class BinarySearchTree {
  constructor() {
    this.root = null;
  }
  insert(data) {
    let newNode = new Node(data);
    if(this.root === null) {
      this.root = newNode;
    } else {
      this.insertNode(this.root, newNode);
    }
  }
  insertNode(node, newNode) {
    if(newNode.data < node.data) {
      if(!node.left) {
        node.left = newNode;
      } else {
        this.insertNode(node.left, newNode);
      }
    } else {
      if(!node.right) {
        node.right = newNode;
      } else {
        this.insertNode(node.right, newNode);
      }
    }
  }
}

function printInorder(node) {
  if(node) {
    printInorder(node.left)
    console.log(node.data)
    printInorder(node.right)
  }
}

arr = [50, 30, 20, 40, 70, 60, 80]
let binTree = new BinarySearchTree();
for (const a of arr) {
  binTree.insert(a); 
}
printInorder(binTree.root)