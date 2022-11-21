class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0

        seen = [1] * n
        seen[0] = seen[1] = 0
        idx = 2
        while idx < n:
            tmp = idx
            if seen[idx]:
                tmp += idx
                while tmp < n:
                    seen[tmp] = 0
                    tmp += idx
            idx += 1
        return sum(seen)

    def countPrimes(self, n: int) -> int:
        """
        Algorithm : Sieve of Eratosthenes (link: https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes)
        """
        seen, ans = [True] * n, 0
        for num in range(2, n):
            if not seen[num]:
                continue
            ans += 1
            seen[num * num : n : num] = [False] * ((n - 1) // num - num + 1)
        return ans


print(Solution.countPrimes(0, 10))
print(Solution.countPrimes(0, 0))
print(Solution.countPrimes(0, 1))
