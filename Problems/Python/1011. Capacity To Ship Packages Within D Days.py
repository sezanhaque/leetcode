class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        """
        Binary Search
        """
        low, high = max(weights), sum(weights)

        while low < high:
            mid = (low + high) >> 1

            weight_sum, day_count = 0, 1
            for weight in weights:
                if weight_sum + weight > mid:
                    weight_sum = 0
                    day_count += 1
                weight_sum += weight

            if day_count > days:
                low = mid + 1
            else:
                high = mid

        return low


print(Solution.shipWithinDays(0, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5))
# print(Solution.shipWithinDays(0, [3, 5, 4, 6, 2], 3))
