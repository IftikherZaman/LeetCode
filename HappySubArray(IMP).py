# 1248. Count Number of Nice Subarrays
from collections import defaultdict
class Solution(object):
    def numberOfSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        ont = defaultdict(int)   
        ont[0] = 1
        niceSubArrays = 0
       
        left = 0
        count = 0

        for num in nums :
                count += num % 2 # Add one if odd
                ont [count] += 1
                niceSubArrays += ont[count-k]

        return  niceSubArrays


# Things I learned:
# The format to solve this type of problem is to create a map of prefix sum( here prefix sum of odd numbers) and then check back (prefix sum - k) to see if we have a subarray that satisfies the condition. If yes, then the frequency of that (prefix sum - k) is subarrays that satisfy the condition.Iterate this through every number.
#Also, set the initial prefix sum of 0 (hashmap[0] = 1) to 1 because it will help you account subarrays that start from the beginning of the array.
# Pseudo code:
# 1. Create a hashmap to store the prefix sum of odd numbers.
# 2. Set the initial prefix sum of 0 to 1.
# 3. Set the initial count of odd numbers to 0.
# 4. Set the initial count of nice subarrays to 0.
# 5. Iterate through the array.
# 6. Increment the count of odd numbers if the number is odd.
# 7. Increment the count of nice subarrays by the frequency of (prefix sum - k).
