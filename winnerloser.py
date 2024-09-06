
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
# ```python
# from collections import defaultdict
# ```
# This line imports the `defaultdict` class from the `collections` module. `defaultdict` is a subclass of dictionary that allows us to specify a default value for any new keys.

# ```python
# class Solution(object):
# ```
# This line defines a class named `Solution`.

# ```python
# def findWinners(self, matches):
# ```
# This line defines a method named `findWinners` within the `Solution` class. It takes `self` (the instance of the class) and `matches` as parameters.

# ```python
# """
# :type matches: List[List[int]]
# :rtype: List[List[int]]
# """
# ```
# This is a docstring that describes the input and output types of the method.

# ```python
# playerMap = defaultdict(lambda: [0, 0])
# ```
# This creates a `defaultdict` where any new key will have a default value of `[0, 0]`. The first 0 represents wins, the second represents losses.

# ```python
# for winner, loser in matches:
# ```
# This starts a loop that iterates over each match in the `matches` list. It unpacks each match into `winner` and `loser`.

# ```python
# playerMap[winner][0] += 1  # Increment wins
# playerMap[loser][1] += 1   # Increment losses
# ```
# These lines update the win/loss record for each player. The winner's win count is incremented, and the loser's loss count is incremented.

# ```python
# win1array = []
# lose1array = []
# ```
# These lines initialize two empty lists to store players who haven't lost any matches and players who have lost exactly one match, respectively.

# ```python
# for player, record in playerMap.items():
# ```
# This starts a loop that iterates over each player and their record in the `playerMap`.

# ```python
# if record[1] == 0:  # No losses
#     win1array.append(player)
# elif record[1] == 1:  # Exactly one loss
#     lose1array.append(player)
# ```
# These lines check each player's loss count. If it's 0, the player is added to `win1array`. If it's 1, the player is added to `lose1array`.

# ```python
# return [sorted(win1array), sorted(lose1array)]
# ```
# This line returns a list containing two sorted lists: `win1array` (players with no losses) and `lose1array` (players with exactly one loss).

# This solution efficiently processes the match data and categorizes players based on their win/loss records, returning the result in the required format.