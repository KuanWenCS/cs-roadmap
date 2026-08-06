# Valid Anagram

# Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

# An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

# Constraints:

# 1 <= s.length, t.length <= 5 * 10^4
# s and t consist of lowercase English letters.


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # maintaining freq dict for two str
        # Time = O(n), Space = O(n)
        if len(s) != len(t):
            return False

        cnt_freq = {}
        for c_s, c_t in zip(s, t):
            if c_s not in cnt_freq:
                cnt_freq[c_s] = 1
            else:
                cnt_freq[c_s] += 1

            if c_t not in cnt_freq:
                cnt_freq[c_t] = -1
            else:
                cnt_freq[c_t] -= 1

        for i in cnt_freq:
            if cnt_freq[i] != 0:
                return False
        return True

        # brute force solution O(n)
        # if len(s) != len(t):
        #     return False
        # return sorted(s) == sorted(t)
