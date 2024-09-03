from collections import defaultdict

def find_longest_substring(s, k):
    counts = defaultdict(int)
    left = ans = 0
    for right in range(len(s)):
        counts[s[right]] += 1
        while len(counts) > k:
            counts[s[left]] -= 1
            if counts[s[left]] == 0:
                del counts[s[left]]
            left += 1
        
        ans = max(ans, right - left + 1)
    
    return ans


//Things I learned :
#1. This is a sliding window problem.
#2. Time Complexity of sliding window is O(n)
#3. Space Complexity of sliding window is O(n)
#4. The defaultdict(int) is used to initialize the dictionary with a default value of 0.

# The `defaultdict()` constructor accepts a single, optional parameter called the **default factory function**. Here’s a breakdown of its usage:

# ### **Parameters:**

# 1. **default_factory** (optional):
#    - This is a callable (like a function or a type) that produces the default value whenever a key is accessed that doesn't already exist in the dictionary.
#    - Common default factories include `int` (which returns `0`), `list` (which returns an empty list `[]`), `set` (which returns an empty set `set()`), `str` (which returns an empty string `''`), or a custom function.
#    - If `default_factory` is `None`, the `defaultdict` behaves just like a regular dictionary and will raise a `KeyError` for missing keys.

# 2. **Other Parameters (Positional or Keyword Arguments)**:
#    - After the `default_factory`, you can pass in positional or keyword arguments, just like with a regular dictionary, to populate the `defaultdict` with initial values.

# ### **Example Usages:**

# ```python
# from collections import defaultdict

# # Using int as the default factory (creates 0 for new keys)
# counts = defaultdict(int)
# print(counts['missing'])  # Output: 0

# # Using list as the default factory (creates an empty list for new keys)
# grouped_items = defaultdict(list)
# grouped_items['missing'].append(1)
# print(grouped_items['missing'])  # Output: [1]

# # Using a custom factory function
# def default_value():
#     return "default"

# custom_dict = defaultdict(default_value)
# print(custom_dict['missing'])  # Output: 'default'

# # Providing initial values
# default_dict_with_values = defaultdict(int, a=10, b=20)
# print(default_dict_with_values['a'])  # Output: 10
# print(default_dict_with_values['missing'])  # Output: 0
# ```

# ### **Summary:**
# - The key parameter is `default_factory`, which determines the default value for missing keys.
# - You can also pass in initial key-value pairs like a regular dictionary.