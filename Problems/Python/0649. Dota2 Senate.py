from collections import deque


class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        senate = list(senate)
        D, R = deque(), deque()

        for idx, char in enumerate(senate):
            if char == "D":
                D.append(idx)
            else:
                R.append(idx)

        while D and R:
            d_turn = D.popleft()
            r_turn = R.popleft()

            if r_turn < d_turn:
                R.append(d_turn + len(senate))
            else:
                D.append(r_turn + len(senate))

        return "Radiant" if R else "Dire"


obj = Solution()
print(obj.predictPartyVictory("RD"))
print(obj.predictPartyVictory("RDD"))
