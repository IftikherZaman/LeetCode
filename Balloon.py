from collections import defaultdict
class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        alphaMap = defaultdict(int)
        for c in text :
            alphaMap[c] += 1
        
        return min ([alphaMap['b'], alphaMap['a'], alphaMap['l']//2 , alphaMap['o']/2, alphaMap['n']]
    )


        
        #Things I learned :
        # If told to find the maximum number of the word and find the minimum frquency of the charcters you need for the word. Let's say Balloon , if you have 1 b , 2a , 4l, 4o, 2n, - Your maximum number will always be 1 as b is only 1
        #If key for a hash is a string using ''. 