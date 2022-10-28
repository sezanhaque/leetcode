class Solution:
    def sortByBits(self, arr: list[int]) -> list[int]:
        return sorted(arr, key=lambda x: [bin(x).count("1"), x])

    def sortByBits(self, arr: list[int]) -> list[int]:
        """
        Bit Manipulation
        """
        return sorted(arr, key = lambda x: (sum((x >> _) & 1 for _ in range(32)), x))

print(Solution.sortByBits(0, [0, 1, 2, 3, 4, 5, 6, 7, 8]))
# print(Solution.sortByBits(0, [1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]))

print(
    Solution.sortByBits(
        0,
        [
            1111,
            7644,
            1107,
            6978,
            8742,
            1,
            7403,
            7694,
            9193,
            4401,
            377,
            8641,
            5311,
            624,
            3554,
            6631,
        ],
    )
)
