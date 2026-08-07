# Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

# Constraints:

# The number of nodes in the list is in the range [0, 100].
# 0 <= Node.val <= 100

from typing import Optional
import util


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        dummy = ListNode()
        prev, first = dummy, head

        while first and first.next:
            second = first.next
            next_pair = second.next

            second.next = first
            first.next = next_pair
            prev.next = second

            prev = first
            first = first.next

        return dummy.next


if __name__ == "__main__":
    sol = Solution()

    util.print_list_node(sol.swapPairs(util.build_list([])))
    print("--------------------------------")
    util.print_list_node(sol.swapPairs(util.build_list([1])))
    print("--------------------------------")
    util.print_list_node(sol.swapPairs(util.build_list([1, 2, 3, 4])))
    print("--------------------------------")
    util.print_list_node(sol.swapPairs(util.build_list([1, 2, 3, 4, 5])))
