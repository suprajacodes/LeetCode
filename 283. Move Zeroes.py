class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        c=nums.count(0)
        nums[:] = list(filter(lambda x : x!=0 , nums))+[0]*c
        return nums