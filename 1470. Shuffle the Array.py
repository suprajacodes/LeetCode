class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        nums1 = nums[:n]
        # print(nums1)
        nums2 = nums[n:]
        # print(nums2)
        res = []
        for i in range(n):
            res.append(nums1[i])
            res.append(nums2[i])
        return res
