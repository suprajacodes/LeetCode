class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i] < 0:
                nums[i] = 0

        for i in range(len(nums)):
            absol = abs(nums[i])
            if absol > 0 and absol <= len(nums):
                if nums[absol - 1] > 0:
                    nums[absol - 1] *= -1
                elif nums[absol - 1] == 0:
                    nums[absol - 1] = -1 * (len(nums) + 1)

        for i in range(1, len(nums) + 1):
            if nums[i - 1] >= 0:
                return i
        return len(nums) + 1