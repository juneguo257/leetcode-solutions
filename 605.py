class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        c = 0
        if (len(flowerbed) == 1):
            return (n == 0 or (n == 1 and flowerbed == [0]))
        
        for i in range(len(flowerbed)):
            if (i == 0):
                if flowerbed[i+1] == 0 and flowerbed[i] == 0:
                    flowerbed[i] = 1
                    c += 1
            elif (i == len(flowerbed)-1):
                if (flowerbed[i-1] == 0 and flowerbed[i] == 0):
                    flowerbed[i] = 1
                    c += 1
            else:
                if (flowerbed[i-1] == 0 and flowerbed[i+1] == 0 and flowerbed[i] == 0):
                    flowerbed[i] = 1
                    c += 1

        return n <= c