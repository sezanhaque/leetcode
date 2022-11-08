class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        # Hard
        if k > 1:
            return "".join(sorted(s))
        return min(s[i:] + s[:i] for i in range(len(s)))

        # one liner
        # return "".join(sorted(s)) if k > 1 else min(s[i:] + s[:i] for i in range(len(s)))


print(Solution.orderlyQueue(0, s = "cba", k = 1))
print(Solution.orderlyQueue(0, s = "baaca", k = 3))