class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Initialize a count array for numbers 0, 1, and 2
        count = [0] * 3
        # Step 1: Count the occurrences of each number
        for i in nums:
            count[i]+=1
        print(count)
        # Step 2: Clear the original nums list
        nums.clear()
        # Step 3: Reconstruct the nums list based on count_array
        for i, j in enumerate(count):
            nums.extend([i] * j)

