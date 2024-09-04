class Solution(object):
    def intersection(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        arrayOfSet = [set(row) for row in nums]
        setIntersect = set.intersection(*arrayOfSet)
        result = sorted(list(setIntersect))
       

        return result
    


#Things I learned :

# - **Purpose of `set.intersection()`**:
#   - `set.intersection()` is a method used to find the common elements (intersection) between multiple sets.

# - **Parameters**:
#   - It accepts an arbitrary number of set arguments and returns a new set containing only the elements that are present in all of the provided sets.

# - **Usage in Code**:
#   - You can use `set.intersection(*iterable)` to find the intersection of sets in an iterable (e.g., a list of sets). The `*` operator unpacks the iterable into individual set arguments.

# - **Example Usage**:
#   ```python
#   arrayOfSet = [set(row) for row in nums]
#   setIntersect = set.intersection(*arrayOfSet)
#   ```
#   - Here, `arrayOfSet` is a list of sets, and `set.intersection(*arrayOfSet)` finds the common elements across all sets.

# - **Built-in `set` Type**:
#   - The `set` class in Python is built-in, so you don’t need to define or import it. You can directly create sets using `set()` and use its methods like `intersection()`.

# - **No Need to Define `set`**:
#   - You don’t need to define `set` in your code for `set.intersection()` to work. It refers to the built-in Python `set` type.

# - **Potential Conflicts**:
#   - Be careful not to override the `set` name with another variable in your code, as that would cause conflicts with the built-in `set` type.

# - **Complexity**:
#   - The complexity of `set.intersection()` depends on the number of sets and the size of the sets involved, typically linear with respect to the smallest set.

# This summary captures the main points discussed about `set.intersection()` and its use in Python.