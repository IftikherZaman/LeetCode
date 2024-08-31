class Solution(object):
    def longestOnes(self, nums, k):
       
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        left = right = count = ans= 0
        
        for right in range (len(nums)):
            if (nums[right]== 0) :
                    count +=1 
                
            while(count>k) :
                  
                if (nums[left] == 0) : 
                    count-=1 
                    
                left+=1 
                    
                 
                
            ans = max(ans, right-left+1)
            
        return ans   
                
                  //Things Learned :
                  //4 spaces for indentation