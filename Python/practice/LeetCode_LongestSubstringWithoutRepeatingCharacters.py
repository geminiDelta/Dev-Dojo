class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        # 4th attempt - SUCCESS
        char_set = set()
        longest_length = 0

        for si in range(len(s)):  # si -> str index
            for c, sj in zip(s[si:], range(len(s[si:]))):
                if c not in char_set:
                    char_set.add(c)
                    if sj == len(s[si:]) - 1:
                        if len(char_set) > longest_length:
                            longest_length = len(char_set)
                else:
                    if len(char_set) > longest_length:
                        longest_length = len(char_set)
                    char_set.clear()
                    break  # 3rd attempt - FAILED - forgot break
        return longest_length


        # 2nd attempt - FAILED -
        # char_set = set()
        # substring_length = 0
        # longest_length = 0
        # for c in s:
        #     if c not in char_set:
        #         substring_length += 1
        #         char_set.add(c)
        #     else:
        #         if substring_length > longest_length:
        #             longest_length = substring_length
        #         substring_length = 1
        #         char_set = set([c])
        # if substring_length > longest_length:
        #     longest_length = substring_length
        # return longest_length

        # 1st attempt - FAILED - misunderstood prompt
        # char_set = set()
        # substring_length = 0
        # for c in s:
        #     if c not in char_set:
        #         substring_length += 1
        #         char_set.add(c)
        # return substring_length
