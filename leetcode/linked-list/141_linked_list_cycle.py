# Linked List Cycle Detection

# Given the beginning of a linked list head, return true if there is a cycle in the linked list. Otherwise, return false.

# There is a cycle in a linked list if at least one node in the list can be visited again by following the next pointer.

# Internally, index determines the index of the beginning of the cycle, if it exists. The tail node of the list will set it's next pointer to the index-th node. If index = -1, then the tail node points to null and no cycle exists.

# Note: index is not given to you as a parameter.

# Constraints:

# 0 <= Length of the list <= 1000.
# -1000 <= Node.val <= 1000
# index is -1 or a valid index in the linked list.


from typing import Optional
import util


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Floyd's Cycle Detection, Time = O(n), Space = O(1)
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

        # Time = O(n), Space = O(n)
        # curr = head
        # seen = set()
        # while curr:
        #     if curr in seen:
        #         return True
        #     seen.add(curr)
        #     curr = curr.next
        # return False


if __name__ == "__main__":
    sol = Solution()

    print(sol.hasCycle(util.build_list([])))
    print(sol.hasCycle(util.build_list([1])))
    print(sol.hasCycle(util.build_list([1, 2, 3, 4])))
    print(sol.hasCycle(util.build_cycle([3, 2, 0, -4], 1)))
