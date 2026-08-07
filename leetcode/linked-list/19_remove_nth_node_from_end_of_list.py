# Given the head of a linked list and an integer n, remove the nth node from the end of the list and return its head.

# Constraints:

# The number of nodes in the list is sz.
# 1 <= sz <= 30
# 0 <= Node.val <= 100
# 1 <= n <= sz

from typing import Optional
import util


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # BP, Floyd's Cycle Detection
        # (100% n times) Time = O(n), Space = O(1)
        dummy = ListNode(0, head)
        slow, fast = dummy, dummy
        for _ in range(n + 1):
            fast = fast.next

        while fast:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next
        return dummy.next

        # (constant factor is bigger) Time = O(n), Space = O(1)
        # if not head:
        #     return head
        # reverse_head = self._reverse(head)
        # return self._restore_skip_nth(reverse_head, n - 1)

    # def _restore_skip_nth(self, head: ListNode, n: int) -> ListNode:
    #     curr, prev = head, None
    #     while curr:
    #         if n == 0:
    #             curr = curr.next
    #         else:
    #             next_node = curr.next
    #             curr.next = prev
    #             prev = curr
    #             curr = next_node
    #         n -= 1
    #     return prev

    # def _reverse(self, head: ListNode) -> ListNode:
    #     curr, prev = head, None
    #     while curr:
    #         next_node = curr.next
    #         curr.next = prev
    #         prev = curr
    #         curr = next_node
    #     return prev


if __name__ == "__main__":
    sol = Solution()

    util.print_list_node(sol.removeNthFromEnd(util.build_list([5]), 1))
    print("--------------------------------")
    util.print_list_node(sol.removeNthFromEnd(util.build_list([1, 2]), 1))
    print("--------------------------------")
    util.print_list_node(sol.removeNthFromEnd(util.build_list([1, 2]), 2))
    print("--------------------------------")
    util.print_list_node(sol.removeNthFromEnd(util.build_list([1, 2, 3, 4]), 2))
