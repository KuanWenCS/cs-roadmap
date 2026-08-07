# Reorder Linked List

# You are given the head of a singly linked-list.

# The positions of a linked list of length = 7 for example, can intially be represented as:

# [0, 1, 2, 3, 4, 5, 6]

# Reorder the nodes of the linked list to be in the following order:

# [0, 6, 1, 5, 2, 4, 3]

# Notice that in the general case for a list of length = n the nodes are reordered to be in the following order:

# [0, n-1, 1, n-2, 2, n-3, ...]

# You may not modify the values in the list's nodes, but instead you must reorder the nodes themselves.

# Constraints:

# 1 <= Length of the list <= 1000.
# 1 <= Node.val <= 1000

from typing import List, Optional
import util


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next or not head.next.next:
            return
        left, right = self._split(head)
        right = self._reverse(right)
        self._merge(left, right)

    def _split(self, head: ListNode) -> tuple[ListNode, ListNode]:
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        first = head
        second = slow.next
        slow.next = None
        return first, second

    def _reverse(self, head: ListNode) -> ListNode:
        curr, prev = head, None
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev

    def _merge(self, first: ListNode, second: ListNode) -> None:
        while first and second:
            next_first = first.next
            next_second = second.next
            first.next = second
            second.next = next_first
            first = next_first
            second = next_second


if __name__ == "__main__":
    sol = Solution()

    util.print_list_node(sol.reorderList(util.build_list([])))
    print("--------------------------------")
    util.print_list_node(sol.split(util.build_list([1, 2, 3, 4])))
    print("--------------------------------")
    util.print_list_node(sol.split(util.build_list([1, 2, 3, 4, 5])))
