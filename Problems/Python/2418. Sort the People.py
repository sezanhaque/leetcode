from typing import List


class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        res = []

        for height, name in zip(heights, names):
            res.append([height, name])

        res.sort(reverse=True)

        return [name for height, name in res]

    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        return [name for height, name in sorted([[height, name] for height, name in zip(heights, names)], reverse=True)]


obj = Solution()
print(obj.sortPeople(names=["Mary", "John", "Emma"], heights=[180, 165, 170]))
print(obj.sortPeople(names=["Alice", "Bob", "Bob"], heights=[155, 185, 150]))
