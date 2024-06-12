class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count=Counter(nums)
        index = 0
        for i in range (0,2+1):
            for _ in range (count[i]):
                nums[index]=i
                index += 1