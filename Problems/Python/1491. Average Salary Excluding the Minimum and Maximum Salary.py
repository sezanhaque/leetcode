class Solution:
    def average(self, salary: list[int]) -> float:
        salary.sort()
        return sum(salary[1:-1]) / (len(salary) - 2)

    def average(self, salary: list[int]) -> float:
        return (sum(salary) - min(salary) - max(salary)) / (len(salary) - 2)


print(Solution.average(0, [4000, 3000, 1000, 2000]))
