class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        l=[]
        c=[]
        for i in range (len(candies)):
            c.append(candies[i]+extraCandies)
            print(c[i])
            if c[i] >= max(candies):
                l.append(True)
            else:
                l.append(False)
        return l
