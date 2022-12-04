import random

class Solution:
    
    def __init__(self, nums: list[int]):
        self.reset = lambda: nums
        self.shuffle = lambda: random.sample(nums, len(nums))


class Solution:
    
    def __init__(self, nums: list[int]):
        self.nums = nums[:]
        self.copy = nums[:]
        

    def reset(self) -> list[int]:
        self.nums = self.copy[:]
        return self.nums        

    def shuffle(self) -> list[int]:
        n = len(self.nums)
        for i in range(n):
            j = random.randint(i, n - 1)
            self.nums[i], self.nums[j] = self.nums[j], self.nums[i]
        return self.nums


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()