class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        l = len(flowerbed)
        co = 0
        c = 1
        flowerbed.insert(0, 0)
        flowerbed.append(0)
        print(flowerbed)
        while (c <= l):
            if flowerbed[c - 1] != 1 and flowerbed[c] != 1 and flowerbed[c + 1] != 1:
                flowerbed[c] = 1
                n -= 1
            c += 1
        return n <= 0




