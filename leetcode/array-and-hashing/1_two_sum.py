# Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.

# You may assume that every input has exactly one pair of indices i and j that satisfy the condition.

# Return the answer with the smaller index first.

# Constraints:

# 2 <= nums.length <= 1000
# -10,000,000 <= nums[i] <= 10,000,000
# -10,000,000 <= target <= 10,000,000
# Only one valid answer exists.

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Time = O(n), Space = O(n)
        seen_dict = {}
        for idx, val in enumerate(nums):
            complement = target - val
            if complement in seen_dict:
                return [seen_dict[complement], idx]
            seen_dict[val] = idx

        # 1+2+...+(n-1) = (n-1)n/2 = O(n^2)
        # 第二層迴圈本質上是為了尋找對應的數，因此應該以更有效率的資料結構來索引
        # 像現在這樣用slicing的方法會有額外成本，初學者常容易忽略
        # for first_index, first_value in enumerate(nums):
        #     for second_index, second_value in enumerate(nums[first_index + 1:]):
        #         if first_value + second_value == target:
        #             return [first_index, first_index + 1 + second_index]


if __name__ == "__main__":
    sol = Solution()

    tests = [
        ([2, 7, 11, 15], 9),
        ([3, 2, 4], 6),
        ([3, 3], 6),
        ([1, 5, 3, 7], 8),
    ]

    for nums, target in tests:
        print(sol.twoSum(nums, target))
