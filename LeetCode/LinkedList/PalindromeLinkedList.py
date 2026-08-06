# Palindrome Linked List

# You are given the head of a singly linked list, return true if it is a palindrome or false otherwise.

# A palindrome is a sequence that reads the same forward and backward.

# Constraints:

# 1 <= Length of the list <= 100,000.
# 0 <= Node.val <= 9

from typing import Optional
import Util


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head and not head.next:
            return True
        left, right = self._split(head)
        reversed_right = self._reverse(right)
        return self._compare(left, reversed_right)

    def _split(self, head: ListNode) -> tuple[ListNode, ListNode]:
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        left = head
        right = slow.next
        slow.next = None
        return left, right

    def _reverse(self, head: ListNode) -> ListNode:
        curr, prev = head, None
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev

    def _compare(self, left: ListNode, right: ListNode) -> bool:
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True


if __name__ == "__main__":
    sol = Solution()

    # print(sol.isPalindrome(Util.build_list([1])))
    # print("--------------------------------")
    print(sol.isPalindrome(Util.build_list([2, 2])))
    print("--------------------------------")
    print(sol.isPalindrome(Util.build_list([1, 2, 3, 2, 1])))
    print("--------------------------------")
    print(sol.isPalindrome(Util.build_list([2, 1])))
