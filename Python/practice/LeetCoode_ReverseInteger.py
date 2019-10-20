# Given a 32-bit signed integer, reverse digits of an integer.
#
# Example 1:
#
# Input: 123
# Output: 321
#
# Example 2:
#
# Input: -123
# Output: -321
#
# Example 3:
#
# Input: 120
# Output: 21
#
# Note:
# Assume we are dealing with an environment which could only store integers within the 32-bit signed integer
# range: [−2^31,  2^31 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed
# integer overflows.

class Solution:
    def reverse(self, x: int) -> int:
        x_str = str(x)
        reverse_iter = reversed(x_str)
        reverse_str = ''
        for digit in reverse_iter:
            if digit == '-':
                reverse_str = '-' + reverse_str
                break
            else:
                reverse_str += digit
            pass
        reverse_int = int(reverse_str)
        if reverse_int < -2 ** 31 or reverse_int > 2 ** 31 - 1:
            return 0
        else:
            return int(reverse_str)

    # def reverse(self, x: int) -> int:
    #     rev = 0
    #     inv = -1 if x < 0 else 1
    #     while x != 0:
    #         pop = abs(x) % 10
    #         rev = rev * 10 + pop
    #         x = int(x / 10)
    #     rev *= inv
    #     if rev < -2 ** 31 or rev > 2 ** 31 - 1:
    #         return 0
    #     else:
    #         return rev


s = Solution()
test = -2 ** 31
print(test)
print(s.reverse(test))

# Status    Runtime Memory  Language
# Accepted	40 ms	14 MB	python3