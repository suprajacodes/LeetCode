'''
Example 1:

Input: s = "abccccdd"
Output: 7
Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.
Example 2:

Input: s = "a"
Output: 1
Explanation: The longest palindrome that can be built is "a", whose length is 1.
'''


class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = Counter(s)
        res = 0
        flag_odd = 0
        for i in count.values():
            if i % 2 == 0:
                res += i
            else:
                res = res + i - 1
                flag_odd = 1

        if flag_odd == 1:
            res += 1
        return res



