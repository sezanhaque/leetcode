from typing import List


class Solution:
    """
    Let the heaviest person go with the lightest person
    """
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        left, right = 0, len(people) - 1
        people.sort(reverse=True)

        while left <= right:
            if people[left] + people[right] <= limit:
                right -= 1
            left += 1

        return left


obj = Solution()
print(obj.numRescueBoats(people=[1, 2], limit=3))
print(obj.numRescueBoats(people=[3, 2, 2, 1], limit=3))
print(obj.numRescueBoats(people=[3, 5, 3, 4], limit=5))
