'''
Example 1:

Input: s = "hello"
Output: "holle"

Example 2:
Input: s = "leetcode"
Output: "leotcede"
'''
#Time Complexity - O(n)
#Space Complexity - O(1)
class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        vowels = 'aeiouAEIOU'
        l , r = 0, len(s)-1
        while l<r:
            if s[l] in vowels and s[r] in vowels:
                s[l],s[r] = s[r], s[l]
                l, r = l+1, r-1
            elif s[l] not in vowels:
                l+=1
            elif s[r] not in vowels:
                r-=1
        return ''.join(s)