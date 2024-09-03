class Solution(object):
    def countElements(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
     
        seen = set()
        seen2 = set(arr)
        duplicate =  0
        
        
        for x in arr :
            if x in seen and x+1 in seen2 :
                duplicate +=1 
            else:
                if x+1 in seen2 :
                      seen.add(x)
        
        return len(seen) + duplicate
    

   #Time complexity: O(n)
   #Space complexity: O(n)

   #Better Optimized Solution :
class Solution(object):
        def countElements(self, arr):
            """
            :type arr: List[int]
            :rtype: int
            """
            seen = set(arr)
            return sum(1 for x in arr if x + 1 in seen)
