class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        rd = 0
        for i in range (1, len(nums)):
            if (nums[rd]!=nums[i]):
                rd+=1
                nums[rd]=nums[i]
        return rd+1