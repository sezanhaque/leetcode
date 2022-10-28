def matchPlayersAndTrainers(self, players: list[int], trainers: list[int]) -> int:
    players.sort()
    trainers.sort()
    dict = {}
    res, left = 0, 0
    for p in players:
        for idx in range(left, len(trainers)):
            if p <= trainers[idx] and idx not in dict:
                dict[idx] = trainers[idx]
                res += 1
                left += 1
                break
    return res


def matchPlayersAndTrainers(self, players: list[int], trainers: list[int]) -> int:
    players.sort()
    trainers.sort()
    res = 0
    cur = 0
    for p in players:
        while cur != len(trainers) and trainers[cur] < p:
            cur += 1
        if cur != len(trainers):
            res += 1
            cur += 1
    return res

def matchPlayersAndTrainers(self, players: list[int], trainers: list[int]) -> int:
        trainers.sort()
        ans, left = 0, 0 
        for p in sorted(players): 
            while left < len(trainers) and p > trainers[left]: left += 1
            if left < len(trainers): 
                ans += 1
                left += 1
        return ans 

# print(matchPlayersAndTrainers(0, [4, 7, 9], [8, 2, 5, 8]))
# print(matchPlayersAndTrainers(0, [1, 1, 1], [10]))
print(matchPlayersAndTrainers(0, [2, 1], [2, 2]))
