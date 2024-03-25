class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        tortise, hare = 0, 0
        while True:
            hare = nums[nums[hare]]
            tortise = nums[tortise]
            if hare == tortise:
                break

        tortise2 = 0
        while True:
            tortise = nums[tortise]
            tortise2 = nums[tortise2]
            if tortise == tortise2:
                return tortise2

