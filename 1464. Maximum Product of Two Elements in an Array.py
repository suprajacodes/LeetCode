class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        c = ((nums[0] - 1) * (nums[1] - 1))
        return c
