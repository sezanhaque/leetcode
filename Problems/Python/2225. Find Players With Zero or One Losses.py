from collections import Counter
from itertools import chain
from sortedcontainers import SortedDict


class Solution:
    def findWinners(self, matches: list[list[int]]) -> list[list[int]]:
        count = Counter()

        for winner, loser in matches:
            count[winner] += 0
            count[loser] += 1

        # filter winners & losers
        winners = (player for player, _ in count.items() if count[player] == 0)
        losers = (player for player, _ in count.items() if count[player] == 1)

        return [winners, losers]

    def findWinners(self, matches: list[list[int]]) -> list[list[int]]:
        # keeping track of all players
        ans = SortedDict()

        for winner, loser in matches:
            # add player
            if winner not in ans:
                ans[winner] = 0

            # increase loss count
            ans[loser] = ans[loser] + 1 if loser in ans else 1

        # filter winners & losers
        winners = (player for player, _ in ans.items() if ans[player] == 0)
        losers = (player for player, _ in ans.items() if ans[player] == 1)

        return [winners, losers]

    def findWinners(self, matches: list[list[int]]) -> list[list[int]]:
        n = max(chain(*matches)) + 1
        players = [0] * n
        for winner, loser in matches:
            if players[winner] >= 0:
                players[winner] = 1  # (1)
            if players[loser] < 0:
                players[loser] -= 1  # (2)
            if players[loser] >= 0:
                players[loser] = -1  # (3)

        # Collect players' id.
        lostZero, lostOne = [], []
        for i in range(n):
            if players[i] == 1:
                lostZero.append(i)
            elif players[i] == -1:
                lostOne.append(i)

        # They are already sorted
        return [lostZero, lostOne]

    def findWinners(self, matches: list[list[int]]) -> list[list[int]]:
        # My solution, Faster than 98.33%

        winners, losers = Counter(match[0] for match in matches), Counter(
            match[1] for match in matches
        )

        return (
            sorted(player for player in winners if player not in losers),
            sorted(loser for loser in losers if losers[loser] == 1),
        )


print(
    Solution.findWinners(
        0,
        [
            [1, 3],
            [2, 3],
            [3, 6],
            [5, 6],
            [5, 7],
            [4, 5],
            [4, 8],
            [4, 9],
            [10, 4],
            [10, 9],
        ],
    )
)
