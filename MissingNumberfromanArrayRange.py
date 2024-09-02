class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        newSet = set(nums)
        for i in range(len(nums) + 1):
            if not i in newSet:
                return i 
            


            ### This was O(n) time complexity and O(n) space complexity
            ### The time complexity was O(n) because we had to iterate through the entire list
            ### The space complexity was O(n) because we had to create a new set from the list

            ### But if we needed to do this in O(n) time complexity and O(1) space complexity, we could use the formula for the sum of the first n numbers
            ### The formula is n * (n + 1) / 2
            ### We could subtract the sum of the list from the sum of the first n numbers to get the missing number
            class Solution(object):
                def missingNumber(self, nums):
                    n = len(nums)
                    total_sum = n * (n + 1) // 2  # Sum of first n natural numbers
                    actual_sum = sum(nums)
                    return total_sum - actual_sum
