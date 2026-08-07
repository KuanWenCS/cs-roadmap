# You are given an integer array piles where piles[i] is the number of bananas in the ith p. You are also given an integer h, which represents the number of hours you have to eat all the bananas.

# You may decide your bananas-per-hour eating rate of k. Each hour, you may choose a p of bananas and eats k bananas from that p. If the p has less than k bananas, you may finish eating the p but you can not eat from another p in the same hour.

# Return the minimum integer k such that you can eat all the bananas within h hours.

# Constraints:

# 1 <= piles.length <= 1,000
# piles.length <= h <= 1,000,000
# 1 <= piles[i] <= 1,000,000,000

from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        while l < r:
            mid = (l + r) // 2
            if self.cntHours(piles, k=mid) <= h:
                r = mid
            else:
                l = mid + 1
        return l

    def cntHours(self, piles: List[int], k: int) -> int:
        h = 0
        for p in piles:
            # shortcut
            h += (p + k - 1) // k

            # if p <= k:
            #     h += 1
            # else:
            #     if p % k == 0:
            #         h += p // k
            #     else:
            #         h += (p // k) + 1
        return h


if __name__ == "__main__":
    sol = Solution()

    print("\noutput: ", sol.minEatingSpeed([1, 4, 3, 2], 9), "\n")
    print("\noutput: ", sol.minEatingSpeed([25, 10, 23, 4], 4), "\n")
    print("\noutput: ", sol.minEatingSpeed([3, 6, 7, 11], 8), "\n")
    print("\noutput: ", sol.minEatingSpeed([30, 11, 23, 4, 20], 6), "\n")


# brute force sol. (exceed time limit)
# class Solution:
#     def minEatingSpeed(self, piles: List[int], h: int) -> int:
#         max_k = self.findMaxK(piles, h)
#         # print("max_k: ", max_k, "\n")
#         for k in range(1, max_k + 1):
#             hours = self.hourCalc(piles, h, k)
#             # print("k: ", k)
#             # print("hours: ", hours, "\n")
#             if hours <= h:
#                 return k

#     def findMaxK(self, piles: List[int], h: int) -> int:
#         max_k = 0
#         for p in piles:
#             if p > max_k:
#                 max_k = p
#         return max_k

#     def hourCalc(self, piles: List[int], h: int, k: int) -> int:
#         # print("piles: ", piles, ",h: ", h, ",k: ", k)
#         h = 0
#         for p in piles:
#             # print("p: ", p)
#             # print("h: ", h)
#             temp = h
#             if p <= k:
#                 h += 1
#             else:
#                 if p % k == 0:
#                     h += p // k
#                 else:
#                     h += (p // k) + 1
#             # print("calc h: ", h - temp)
#         return h
