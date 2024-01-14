class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        d={}
        c=0
        for i in range(len(nums)):
            if nums[i] in d:
                d[nums[i]] += 1
            else:
                d[nums[i]] = 1
        for x in d.values():
            count = (x*(x-1))//2
            c+=count
        return c
