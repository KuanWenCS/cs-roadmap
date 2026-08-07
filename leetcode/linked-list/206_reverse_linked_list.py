# Reverse Linked List

# Given the beginning of a singly linked list head, reverse the list, and return the new beginning of the list.

# Constraints:

# 0 <= The length of the list <= 1000.
# -1000 <= Node.val <= 1000

from typing import Optional
import util


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # BP, Time = O(n), Space = O(1)
        prev = None
        curr = head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev

        # revursion sol., Not BP, Time = O(n), Space = O(n)
        # if head is None or head.next is None:
        #     return head
        # new_head = self.reverseList(head.next)
        # head.next.next = head
        # head.next = None
        # return new_head

        # brute force sol., Time = O(n), Space = O(n)
        # arr = []
        # while head:
        #     arr.append(head.val)
        #     head = head.next
        # arr.reverse()
        # dummy = ListNode()
        # curr = dummy
        # for num in arr:
        #     curr.next = ListNode(num)
        #     curr = curr.next
        # return dummy.next


if __name__ == "__main__":
    sol = Solution()

    util.print_list_node(sol.reverseList(util.build_list([])))
    util.print_list_node(sol.reverseList(util.build_list([0, 1, 2, 3])))
