class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        '''
        Time Complexity: O(n)
        Space Complexity : O(n)
        '''
        def recursive (l,r):
            if l<r:
                s[l], s[r] = s[r], s[l]
                recursive(l+1, r-1)
        recursive(0,len(s)-1)