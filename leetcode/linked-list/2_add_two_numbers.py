# You are given two non-empty linked lists, l1 and l2, where each represents a non-negative integer.

# The digits are stored in reverse order, e.g. the number 321 is represented as 1 -> 2 -> 3 -> in the linked list.

# Each of the nodes contains a single digit. You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Return the sum of the two numbers as a linked list.

# Constraints:

# 1 <= l1.length, l2.length <= 100.
# 0 <= Node.val <= 9

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        # BP, Time and Space are both O(n)
        dummy = ListNode()
        curr = dummy
        carry = 0

        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            total = v1 + v2 + carry
            carry = total // 10

            curr.next = ListNode(total % 10)
            curr = curr.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy.next

        # not BP, Time and Space are the same, bad syntax implementation
        # carry, sum = 0, 0
        # dummy = ListNode()
        # curr = dummy

        # while l1 or l2:
        #     if l1 and l2:
        #         sum = l1.val + l2.val + carry
        #     elif l1:
        #         sum = l1.val + carry
        #     else:
        #         sum = l2.val + carry

        #     if sum > 9:
        #         carry = 1
        #         sum -= 10
        #     else:
        #         carry = 0

        #     curr.next = ListNode(sum)
        #     curr = curr.next

        #     l1 = l1.next if l1 else None
        #     l2 = l2.next if l2 else None

        # if carry:
        #     curr.next = ListNode(1)

        # return dummy.next
