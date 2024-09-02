class Solution(object):
    def checkIfPangram(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        alphaOnce = set ()
        
      
        
        for s in sentence :
            alphaOnce.add(s)
        
        
        
        if len(alphaOnce) < 26 :
            return False
        
        else : return True
            
        #alternate explanation
    #     class Solution(object):
    # def checkIfPangram(self, sentence):
    #     return len(set(sentence)) == 26


# import string
#The string.ascii_lowercase is a constant in Python's string module that contains all the lowercase letters of the English alphabet, from 'a' to 'z', in a single string.

print(string.ascii_lowercase)
