# Given a string s, return true if it is a palindrome, otherwise return false.

# A palindrome is a string that reads the same forward and backward. It is also case-insensitive and ignores all non-alphanumeric characters.

# Note: Alphanumeric characters consist of letters (A-Z, a-z) and numbers (0-9).

# Constraints:

# 1 <= s.length <= 1000
# s is made up of only printable ASCII characters.


class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1

            while left < right and not s[right].isalnum():
                right -= 1

            if s[left].casefold() != s[right].casefold():
                return False

            left += 1
            right -= 1

        return True


if __name__ == "__main__":
    sol = Solution()

    tests = ["Was it a car or a cat I saw?", "tab a cat", "Never odd or even"]

    for t in tests:
        print(sol.isPalindrome(t))
