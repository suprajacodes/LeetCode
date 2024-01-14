class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        d=Counter(nums)
        c=0
        for x in d.values():
            count = (x*(x-1))//2
            c+=count
        return c
