class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words, dict = s.split(), {}

        # for pattern = "abba", s = "dog cat cat fish"
        if len(pattern) != len(words):
            return False

        # for pattern="aaaa", s="dog cat cat dog"
        if len(set(pattern)) != len(set(words)):
            return False

        # store every pattern as a key
        # and word as a value in dictionary
        for idx, val in enumerate(pattern):
            if val not in dict:
                dict[val] = words[idx]
            elif dict[val] != words[idx]:
                return False

        return True


print(Solution.wordPattern(0, pattern="abba", s="dog cat cat dog"))
print(Solution.wordPattern(0, pattern="abba", s="dog cat cat fish"))
print(Solution.wordPattern(0, pattern="aaaa", s="dog cat cat dog"))
