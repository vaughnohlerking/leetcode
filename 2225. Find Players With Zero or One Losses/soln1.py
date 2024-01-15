# Runtime
# 1450ms
# Beats 77.50% of users with Python3

# Memory
# 72.04MB
# Beats 35.64% of users with Python3

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        
        players = {}

        for match in matches:
            winner = match[0]
            loser = match[1]
            if winner not in players:
                players[winner] = 0
            if loser not in players:
                players[loser] = 1
            else:
                players[loser] = players.get(loser) + 1

        zeroes = []
        ones = []

        for player in players:
            if players[player] == 0:
                zeroes.append(player)
            elif players[player] == 1:
                ones.append(player)

        zeroes.sort()
        ones.sort()

        return [zeroes, ones]
