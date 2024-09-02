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
    
#         //Things learned :
# To find the lowest value in an array (or list) in Python, you can use the built-in `min()` function. The `min()` function returns the smallest item in an iterable or the smallest of two or more arguments.

# ### Example:
# ```python
# nums = [3, 1, 4, 1, 5, 9, -2]
# lowest_value = min(nums)
# print(lowest_value)  # Output: -2
# ```

# ### How it Works:
# - **`min(nums)`**: This iterates through the entire list `nums` and finds the smallest element.

# ### Complexity:
# - The time complexity of `min()` is **O(n)**, where `n` is the number of elements in the list. It needs to check each element to determine the smallest one.

# This approach is simple and efficient for finding the lowest value in an array.