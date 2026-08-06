# Contains Duplicate

# Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

# Constraints:

# 0 <= nums.length <= 10^5
# -10^9 <= nums[i] <= 10^9

from typing import List


class Solution:

    def hasDuplicate(self, nums: List[int]) -> bool:
        # O(n) for set(nums)
        # return (len(nums) - len(set(nums))) != 0

        # -
        # still O(n), but increasing the best case performance
        seen = set()
        for x in nums:
            if x in seen:
                return True
            seen.add(x)
        return False
