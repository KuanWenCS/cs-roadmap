# You are given a string s consisting of the following characters: '(', ')', '{', '}', '[' and ']'.

# The input string s is valid if and only if:

# Every open bracket is closed by the same type of close bracket.
# Open brackets are closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
# Return true if s is a valid string, and false otherwise.

# Constraints:

# 1 <= s.length <= 1000


class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2:
            return False

        pairs = {
            "(": ")",
            "[": "]",
            "{": "}",
        }

        stack = []
        for ch in s:
            if ch in pairs:
                stack.append(pairs[ch])
            elif stack and stack[-1] == ch:
                stack.pop()
            else:
                return False

        return not stack

        # almost BP, Time = O(n), Space = O(n), not enough pythonic
        # len_s = len(s)
        # if len_s == 1 or len_s % 2 != 0:
        #     return False

        # arr = []
        # for i, v in enumerate(s):
        #     if v == "(" or v == "[" or v == "{":
        #         match v:
        #             case "(":
        #                 arr.append(")")
        #             case "[":
        #                 arr.append("]")
        #             case "{":
        #                 arr.append("}")
        #     elif arr and v == arr[-1]:
        #         arr.pop()
        #     else:
        #         return False
        # return len(arr) == 0


if __name__ == "__main__":
    sol = Solution()

    tests = ["[]", "([{}])", "[(])", "()[]{}", "]]"]

    for t in tests:
        print(sol.isValid(t), "\n")
