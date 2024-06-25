'''
Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
'''


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ''
        strs = sorted(strs)
        print(strs)
        first = strs[0]
        last = strs[-1]
        for i in range(len(first)):
            if first[i] != last[i]:
                return res
            res += first[i]
        return res
