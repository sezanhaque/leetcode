class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        """
        We can put one flower in every three contiguous empty spots, after put that flower in the middle of three,
        the third one can be counted into the "next three spots". So we set the count variable to be 1.

        Since the head and the tail are special cases, we insert a empty spot at head and append a empty spot at the tail.

        We append 0 to the last index so that if the last 3 index are "1, 0, 0" then after adding 0 it will be "0, 0, 0"
        and we can insert 1 in the middle 0
        """
        flowerbed.append(0)
        count = 1
        for f in flowerbed:
            if f == 0:
                count += 1
            else:
                count = 0
            if count == 3:
                n -= 1
                count = 1
            if n == 0:
                return True
        return False

    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        # NeetCode solution

       f = [0] + flowerbed + [0]
       
       for i in range(1, len(f) - 1):  # skip first & last
           if f[i - 1] == 0 and f[i] == 0 and f[i + 1] == 0:
               f[i] = 1
               n -= 1
       return n <= 0

       empty = 0 if flowerbed[0] else 1
       
       for f in flowerbed:
           if f:
               n -= int((empty - 1) / 2)  # int division, round toward zero
               empty = 0
           else:
               empty += 1

       n -= (empty) // 2
       return n <= 0



print(Solution.canPlaceFlowers(0, [1, 0, 0, 0, 1], 1))
print(Solution.canPlaceFlowers(0, [1, 0, 0, 0, 1], 2))
print(Solution.canPlaceFlowers(0, [1, 0, 0, 0, 0, 1], 2))
print(Solution.canPlaceFlowers(0, [1, 0, 0, 0, 0, 0, 1], 2))
print(Solution.canPlaceFlowers(0, [0, 1, 0], 1))
print(Solution.canPlaceFlowers(0, [0, 0, 1, 0, 1], 1))
