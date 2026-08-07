# You are given the head of a linked list of length n. Unlike a singly linked list, each node contains an additional pointer random, which may point to any node in the list, or null.

# Create a deep copy of the list.

# The deep copy should consist of exactly n new nodes, each including:

# The original value val of the copied node
# A next pointer to the new node corresponding to the next pointer of the original node
# A random pointer to the new node corresponding to the random pointer of the original node
# Note: None of the pointers in the new list should point to nodes in the original list.

# Return the head of the copied linked list.

# In the examples, the linked list is represented as a list of n nodes. Each node is represented as a pair of [val, random_index] where random_index is the index of the node (0-indexed) that the random pointer points to, or null if it does not point to any node.

# Constraints:

# 0 <= n <= 100
# -100 <= Node.val <= 100
# Node values are not guaranteed to be unique.
# random is null or is pointing to some node in the linked list.

from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: "Node" = None, random: "Node" = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        # BP: A -> A' -> B -> B' -> C -> C', Time = O(n), Space = O(1)

        # Time = O(n), Space = O(n)
        if not head:
            return None

        list_map = dict()
        dummy = Node(0)
        new = dummy
        old = head

        while old:
            new.next = Node(x=old.val)
            new = new.next
            list_map[old] = new
            old = old.next

        return self._list_mapping(head, dummy.next, list_map)

    def _list_mapping(self, head: Node, new: Node, list_map: dict) -> Node:
        curr = new
        while head:
            curr.random = list_map.get(head.random)
            curr = curr.next
            head = head.next
        return new
