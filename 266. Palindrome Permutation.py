'''
Example 1:

Input: s = "code"
Output: false
Example 2:

Input: s = "aab"
Output: true
Example 3:

Input: s = "carerac"
Output: true

'''


class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        count = Counter(s)
        res = 0
        for i in count.values():
            if i % 2 != 0:
                res += 1
        return res <= 1



