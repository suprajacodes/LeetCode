'''
Example 1:

Input: s = "aba"
Output: true
Example 2:

Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.
Example 3:

Input: s = "abc"
Output: false

'''

class Solution:
    def validPalindrome(self, s: str) -> bool:
        #Using Helper Function
        l,r = 0, len(s)-1
        while l < r:
            if s[l]!=s[r]:
                return self.helperMethods(s,l+1,r) or self.helperMethods(s,l, r-1)
            l,r = l+1, r-1
        return True

    def helperMethods(self,s,i,j):
        l,r = i,j
        while l < r:
            if s[l]!=s[r]:
                return False
            l,r = l+1, r-1
        return True





