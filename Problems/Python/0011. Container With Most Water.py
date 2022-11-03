class Solution:
    def maxArea(self, height: list[int]) -> int:
        water = 0
        left, right = 0, len(height) - 1

        while left < right:
            water = max(water, (right - left) * min(height[left], height[right]))
            minHeight = min(height[left], height[right])

            if height[left] < height[right]:
                left += 1

                while height[left] < minHeight:
                    left += 1
            else:
                right -= 1

                while height[right] < minHeight:
                    right -= 1

        return water


print(Solution.maxArea(0, [1, 8, 6, 2, 5, 4, 8, 3, 7]))
