from collections import defaultdict
from random import choice

class Solution:
    
    def __init__(self, nums: list[int]):
        self.index_dict = defaultdict(list)
        for i in range(len(nums)):
            self.index_dict[nums[i]].append(i)
        

    def pick(self, target: int) -> int:
        return choice(self.index_dict[target])


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)