// You’re given the pointer to the head node of a linked list, an integer to add to the list and the position at which the integer must be inserted.Create a new node with the given integer, insert this node at the desired position and return the head node.

// A position of 0 indicates head, a position of 1 indicates one node away from the head and so on.The head pointer given may be null meaning that the initial list is empty.

// As an example, if your list starts as and you want to insert a node at position  with , your new list should be

// Function Description Complete the function insertNodeAtPosition in the editor below.It must return a reference to the head node of your finished list.

// insertNodeAtPosition has the following parameters:

// head: a SinglyLinkedListNode pointer to the head of the list
// data: an integer value to insert as data in your new node
// position: an integer position to insert the new node, zero based indexing
// Input Format

// The first line contains an integer, the number of elements in the linked list.
// Each of the next  lines contains an integer SinglyLinkedListNode[i].data.
// The next line contains an integer  denoting the data of the node that is to be inserted.
// The last line contains an integer.

const { SinglyLinkedList, SinglyLinkedListNode, printSinglyLinkedList } = require('../basic/singly_linked_list');

function insertNodeAtPosition(head, data, position) {
  const newNode = new SinglyLinkedListNode(data);
  if (position == 0) {
    newNode.next = head;
    return newNode;
  }
  let currentNode = head;
  for (let i = 1; i < position; i++) {
    currentNode = currentNode.next;
  }
  const nextNode = currentNode.next;
  currentNode.next = newNode;
  newNode.next = nextNode;
  return head;
}

let arr = [16, 17, 13];
const llist = new SinglyLinkedList();
arr.forEach(a => llist.insertNode(a));
const newLList = insertNodeAtPosition(llist.head, 1, 2);
printSinglyLinkedList(newLList);