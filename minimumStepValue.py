class Solution(object):
    def minStartValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        

        prefix = [nums[0]]
        for i in range(1,len(nums)):
            prefix.append(nums[i]+ prefix[-1])
        
        lowestAggregate = min(prefix)
        if (lowestAggregate <= 0 ) :  minStartVal = 1 - lowestAggregate
        else:  minStartVal = 1
       
        
        return  minStartVal