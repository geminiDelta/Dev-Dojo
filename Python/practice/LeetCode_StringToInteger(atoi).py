import re

class Solution:  # 1st attempt - SUCCESS

    INT_MAX = 2**31 - 1
    INT_MIN = -2**31

    def myAtoi(self, str: str) -> int:
        can_convert = re.search(r'^(\s*[+\-]?\d+)', str)

        if can_convert:
            num_regex = r'[+\-]?\d+'
            num = int(re.search(num_regex, str).group())
            if num > self.INT_MAX:
                return self.INT_MAX
            elif num < self.INT_MIN:
                return self.INT_MIN
            else:
                return num
        else:
            return 0


solution_obj = Solution()

test1 = "123"
test2 = "    456 foo"
test3 = "   bar 789"
test4 = "-91283472332"
print(solution_obj.myAtoi(test4))


# Another solution
# class Solution:
#     def myAtoi(self, s: str) -> int:
#         # Use regular experssion
#         import re
#         s = s.strip()
#         INT_MAX = pow(2,31)
#         temp = re.findall(r'^[+-]?\d+', s)
#         if not temp:
#                 return 0
#         else:
#             return max(-INT_MAX, int(temp[0])) if "-" in temp[0] else min(INT_MAX-1, int(temp[0]))
