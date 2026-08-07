# Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

# You should preserve the original relative order of the nodes in each of the two partitions.

# Constraints:

# The number of nodes in the list is in the range [0, 200].
# -100 <= Node.val <= 100
# -200 <= x <= 200

from typing import Optional
import util


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        beforeDummy, afterDummy = ListNode(), ListNode()
        before, after = beforeDummy, afterDummy
        curr = head

        while curr:
            nxt = curr.next
            if curr.val < x:
                before.next = curr
                before = curr
            else:
                after.next = curr
                after = curr

            curr = nxt

        after.next = None
        before.next = afterDummy.next

        return beforeDummy.next

        # not BP, Time = O(n), Space = O(1)
        # lessDummy, greaterDummy = ListNode(), ListNode()
        # curr, prev = lessDummy, greaterDummy
        # curr.next = head

        # while curr.next:
        #     node = curr.next
        #     if node.val >= x:
        #         curr.next = node.next
        #         prev.next = node
        #         prev = node
        #         prev.next = None
        #     else:
        #         curr = node

        # if greaterDummy.next:
        #     curr.next = greaterDummy.next

        # return lessDummy.next


if __name__ == "__main__":
    sol = Solution()

    # util.print_list_node(sol.partition(util.build_list([]), 0))
    # print("--------------------------------")
    # util.print_list_node(sol.partition(util.build_list([1]), 2))
    # print("--------------------------------")
    # util.print_list_node(sol.partition(util.build_list([2, 1]), 2))
    # print("--------------------------------")
    util.print_list_node(sol.partition(util.build_list([1, 4, 3, 2, 5, 2]), 3))
    print("--------------------------------")
    util.print_list_node(sol.partition(util.build_list([1, 4, 3, 2, 5, 6]), 3))
