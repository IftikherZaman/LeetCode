
// Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

 

// Example 1:

// Input: nums = [-4,-1,0,3,10]
// Output: [0,1,9,16,100]
// Explanation: After squaring, the array becomes [16,1,0,9,100].
// After sorting, it becomes [0,1,9,16,100].
// Example 2:

// Input: nums = [-7,-3,2,3,11]
// Output: [4,9,9,49,121]
 

// Constraints:

// 1 <= nums.length <= 104
// -104 <= nums[i] <= 104
// nums is sorted in non-decreasing order.
 

// Follow up: Squaring each element and sorting the new array is very trivial, could you find an O(n) solution using a different approach?




class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
      
        n = len(nums)
        result = [0] * n  # Initialize the result array with zeros
        left, right = 0, n - 1  # Two pointers at the start and end
        position = n - 1  # Start filling the result array from the end

        while left <= right:
            left_square = nums[left] ** 2
            right_square = nums[right] ** 2

            if left_square > right_square:
                result[position] = left_square
                left += 1
            else:
                result[position] = right_square
                right -= 1

            position -= 1  # Move to the next position in the result array

        return result



        //Alternative solution
        class Solution(object):
    def sortedSquares(self, A):
        return sorted(x * x for x in A)

//Things learned :


// Your implementation of the sortedSquares method is a concise and effective way to solve the problem of squaring each number in a list and then sorting the result. Let's break down what this code does:

// Code:
// python
// Copy code
// class Solution(object):
//     def sortedSquares(self, A):
//         return sorted(x * x for x in A)
// Explanation:
// x * x for x in A:

// This is a generator expression. It iterates over each element x in the list A, computes x * x (which is the square of x), and yields the squared value.
// For example, if A = [-4, -1, 0, 3, 10], the generator expression will produce the values 16, 1, 0, 9, 100.
// sorted(...):

// The sorted() function takes an iterable (in this case, the generator expression) and returns a new list containing all the items in ascending order.
// After squaring each element, sorted() will sort these squared values.
// Return Statement:

// The return statement outputs the sorted list of squared values.
// Example Walkthrough:
// For the input A = [-4, -1, 0, 3, 10]:

// The generator expression x * x for x in A computes the squares: [16, 1, 0, 9, 100].
// The sorted() function then sorts this list to produce [0, 1, 9, 16, 100].
// Summary:
// Your implementation is correct and efficient in terms of simplicity and readability. It leverages Python’s built-in sorted() function and a generator expression to achieve the desired result with minimal code. The time complexity is O(n log n) due to the sorting step, where n is the number of elements in the input list A.

###
The `sorted()` function in Python is a built-in function used to sort any iterable (like a list, tuple, or string) and return a new sorted list. It is versatile and can be customized using optional parameters.

### Syntax:

```python
sorted(iterable, key=None, reverse=False)
```

### Parameters:

1. **`iterable`**:
   - The iterable (e.g., list, tuple, string) that you want to sort.
   - Required parameter.

2. **`key`**:
   - A function to be called on each element prior to making comparisons. The `key` function allows you to specify a custom sorting criterion.
   - Default is `None`, which means the elements are compared directly.
   - Example: `key=len` to sort by the length of the elements.

3. **`reverse`**:
   - A boolean value. If `True`, the list is sorted in descending order. If `False` (default), it is sorted in ascending order.
   - Example: `reverse=True` for descending order.

### Return Value:

- Returns a new list that contains all items from the iterable, sorted according to the specified criteria.

### Examples:

1. **Sorting a List of Numbers**:

```python
numbers = [4, 1, 7, 3, 9]
sorted_numbers = sorted(numbers)
print(sorted_numbers)  # Output: [1, 3, 4, 7, 9]
```

2. **Sorting in Descending Order**:

```python
numbers = [4, 1, 7, 3, 9]
sorted_numbers_desc = sorted(numbers, reverse=True)
print(sorted_numbers_desc)  # Output: [9, 7, 4, 3, 1]
```

3. **Sorting a List of Strings**:

```python
words = ["banana", "apple", "cherry"]
sorted_words = sorted(words)
print(sorted_words)  # Output: ['apple', 'banana', 'cherry']
```

4. **Sorting by Length of Strings**:

```python
words = ["banana", "apple", "cherry"]
sorted_words_by_length = sorted(words, key=len)
print(sorted_words_by_length)  # Output: ['apple', 'banana', 'cherry']
```

5. **Sorting a List of Tuples**:

```python
pairs = [(2, 'two'), (1, 'one'), (3, 'three')]
sorted_pairs = sorted(pairs, key=lambda x: x[1])
print(sorted_pairs)  # Output: [(1, 'one'), (3, 'three'), (2, 'two')]
```

### Key Points:

- **Non-Destructive**: `sorted()` returns a new list and does not modify the original iterable.
- **Stability**: Python’s sort is stable, meaning that if two elements have the same key, their original order is preserved in the sorted list.

### Summary:

The `sorted()` function is a powerful tool for ordering items in an iterable in Python. With its customizable `key` and `reverse` parameters, it provides flexible sorting options to suit various needs.
