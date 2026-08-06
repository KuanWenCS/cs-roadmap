# Merge Two Sorted Linked Lists

# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists into one sorted linked list and return the head of the new sorted linked list.

# The new list should be made up of nodes from list1 and list2.

# Constraints:

# 0 <= The length of the each list <= 100.
# -100 <= Node.val <= 100

from typing import Optional
import Util


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy
        while list1 and list2:
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        tail.next = list1 if list1 else list2
        # ＾shortcut
        # if list1:
        #     tail.next = list1
        # else:
        #     tail.next = list2

        return dummy.next

        # sol. of create new ListNode, Space = O(n+m)
        # dummy = ListNode()
        # tail = dummy
        # while list1 or list2:
        #     if list1 and list2:
        #         if list1.val <= list2.val:
        #             tail.next = list1
        #             # tail.next = ListNode(list1.val)
        #             list1 = list1.next
        #         else:
        #             tail.next = list2
        #             # tail.next = ListNode(list2.val)
        #             list2 = list2.next
        #     elif list1:
        #         tail.next = list1
        #         # tail.next = ListNode(list1.val)
        #         list1 = list1.next
        #     elif list2:
        #         tail.next = list2
        #         # tail.next = ListNode(list2.val)
        #         list2 = list2.next
        #     tail = tail.next
        # return dummy.next


if __name__ == "__main__":
    sol = Solution()

    Util.print_list_node(sol.mergeTwoLists(Util.build_list([]), Util.build_list([])))
    print()
    Util.print_list_node(
        sol.mergeTwoLists(Util.build_list([]), Util.build_list([1, 2]))
    )
    print()
    Util.print_list_node(
        sol.mergeTwoLists(Util.build_list([1, 2, 4]), Util.build_list([1, 3, 5]))
    )
