class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        maxleft, maxright = height[l], height[r]
        rain_water = 0
        while l < r:
            if maxleft <= maxright:
                rain_water = abs(rain_water + maxleft - height[l])
                l += 1
                maxleft = max(maxleft, height[l])
                print(rain_water)
            else:
                rain_water = abs(rain_water + maxright - height[r])
                r -= 1
                maxright = max(maxright, height[r])
                print(rain_water)

        return rain_water





