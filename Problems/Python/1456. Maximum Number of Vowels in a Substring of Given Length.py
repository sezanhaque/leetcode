class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        res = curr_count = 0

        for idx, value in enumerate(s):
            if idx >= k:
                if s[idx - k] in vowels:
                    curr_count -= 1
            if value in vowels:
                curr_count += 1
            res = max(res, curr_count)

        return res


obj = Solution()
print(obj.maxVowels(s="abciiidefaaa", k=3))
print(obj.maxVowels(s="aeiou", k=2))
print(obj.maxVowels(s="tryhard", k=4))  # 1
