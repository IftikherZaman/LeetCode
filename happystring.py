from collections import Counter
class Solution(object):
    def areOccurrencesEqual(self, s):
        """
        :type s: str
        :rtype: bool
        """
        count = Counter(s)
        countSet = set(count.values())
        if len(countSet) == 1 :
            return True
        else : return False



#Things I learned :
# 1. The Counter() function from the collections module is used to count the frequency of elements in an iterable.
# 2. The Counter() function returns a dictionary-like object that maps elements to their counts.
#3. When counter receives an array, you can treat it as an array with frequency of each index.
#4. When counter receives a string, you can treat it as a dictionary with frequency of each character.