class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums) / 2
        d = {}
        for i in nums:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        m = (max(d.items(), key=lambda x: x[1]))
        if int(m[1]) > n:
            return m[0]



