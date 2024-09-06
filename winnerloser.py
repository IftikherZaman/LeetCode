
from collections import defaultdict

class Solution(object):
    def findWinners(self, matches):
        """
        :type matches: List[List[int]]
        :rtype: List[List[int]]
        """
        playerMap = defaultdict(lambda: [0, 0])
        
        for winner, loser in matches:
            playerMap[winner][0] += 1  # Increment wins
            playerMap[loser][1] += 1   # Increment losses
        
        win1array = []
        lose1array = []
        
        for player, record in playerMap.items():
            if record[1] == 0:  # No losses
                win1array.append(player)
            elif record[1] == 1:  # Exactly one loss
                lose1array.append(player)
        
        return [sorted(win1array), sorted(lose1array)]
    
    ## Alternate Solution :
    class Solution(object):
    def findWinners(self, matches):
        """
        :type matches: List[List[int]]
        :rtype: List[List[int]]
        """
        winners = set()
        losers = set()
        multi_losers = set()
        for winner, loser in matches:
            winners.add(winner)
            if loser in losers:
                multi_losers.add(loser)
            losers.add(loser)

        only_winners = winners - losers
        one_time_losers = losers - multi_losers

        return [sorted(list(only_winners)), sorted(list(one_time_losers))]
