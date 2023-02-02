from typing import List


class Solution:
    """
    Sort the list according to age and score
    So, we will get a list of players sorted by age and score.

    Now, we need to check if current player score is greater than previous players.
    We will track a list for total score as "DP" from 1st to current player.

    Always get max between the current score with res.
    """

    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        scores = sorted(((ages[idx], scores[idx]) for idx in range(len(scores))), key=lambda x: (x[0], x[1]))
        DP = [scores[i][1] for i in range(len(scores))]
        res = DP[0]

        for idx in range(len(scores)):
            currScore = scores[idx][1]
            for j in range(idx):
                # if every score of the list is
                # less than or equal to currScore
                if scores[j][1] <= currScore:
                    DP[idx] = max(DP[idx], currScore + DP[j])
                res = max(res, DP[idx])

        return res

    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        max_scores = [0] * (max(ages) + 1)

        for score, age in sorted(zip(scores, ages)):
            print(score, age, max_scores)
            # max_scores[:age + 1] limits the players considered without conflict - lower score and equal or lower ages
            max_scores[age] = score + max(max_scores[:age + 1])
            print("max_scores:", max_scores)

        return max(max_scores)


obj = Solution()
print(obj.bestTeamScore(scores=[4, 5, 6, 5], ages=[2, 1, 2, 1]))
# print(obj.bestTeamScore(scores=[1], ages=[4]))
