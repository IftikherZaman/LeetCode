class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        prefix = [nums[0]]
        for i in range (1, len(nums)):
            prefix.append(nums[i]+prefix[-1])
        
        return prefix


        //Things learned :
        //range(5) means it ends before 5