class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        l = []
        m = max(candies)
        for i in range(len(candies)):
            l.append(candies[i] + extraCandies >= m)
        return l
