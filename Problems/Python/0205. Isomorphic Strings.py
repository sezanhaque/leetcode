class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        return len(set(s)) == len(set(zip(s, t))) == len(set(t))


print(Solution.isIsomorphic(0, "egg", "add"))
print(Solution.isIsomorphic(0, "foo", "bar"))
