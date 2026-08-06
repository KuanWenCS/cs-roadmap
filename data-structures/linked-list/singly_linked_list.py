# Design Singly Linked List

# Design a Singly Linked List class.

# Your LinkedList class should support the following operations:

# LinkedList() will initialize an empty linked list.
# int get(int i) will return the value of the ith node (0-indexed). If the index is out of bounds, return -1.
# void insertHead(int val) will insert a node with val at the head of the list.
# void insertTail(int val) will insert a node with val at the tail of the list.
# bool remove(int i) will remove the ith node (0-indexed). If the index is out of bounds, return false, otherwise return true.
# int[] getValues() return an array of all the values in the linked list, ordered from head to tail.

# Note:

# The index int i provided to get(int i) and remove(int i) is guaranteed to be greater than or equal to 0.

from typing import List


class Node:

    def __init__(self, val: int):
        self.val = val
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        if self.head is None:
            return -1
        curr = self.head
        while index > 0:
            if curr.next is None:
                return -1
            curr = curr.next
            index -= 1
        return curr.val

    def insertHead(self, val: int) -> None:
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node

    def insertTail(self, val: int) -> None:
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
        else:
            curr = self.head
            while curr.next is not None:
                curr = curr.next
            curr.next = new_node

    def remove(self, index: int) -> bool:
        if self.head is None:
            return False
        if index == 0:
            self.head = self.head.next
            return True

        curr = self.head
        steps = index
        while steps > 0:
            if curr.next is None:
                return False
            prev = curr
            curr = curr.next
            steps -= 1
        prev.next = curr.next
        return True

    def getValues(self) -> List[int]:
        new_int_list = []
        curr = self.head
        while curr is not None:
            new_int_list.append(curr.val)
            curr = curr.next
        return new_int_list
