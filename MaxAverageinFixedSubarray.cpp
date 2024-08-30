class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """

        total = sum(nums[:k])
        max_average = total / float(k)

        for i in range(k, len(nums)):
            total = total - nums[i - k] + nums[i]
            new_average = total / float(k)
            max_average = max(max_average, new_average)

        return max_average



        //Things Learned : 
//         5 / 2  # In Python 2, this would return 2
// 5 / 2.0  # This would return 2.5 in both Python 2 and 3
//Always convert integer into float for Pythob 2.0