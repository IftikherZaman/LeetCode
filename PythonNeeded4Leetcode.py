# Python things to learn for LeetCode
n="abc"
print('n=', n) # Print 

n,m = 0,"abc"
n,m,z = 0.125, "abc" , False



#Can't do n++ ;
n +=1 
n= n+1 

#None is null
n = 4
n = None 

#If statements don't need brackets

n = 1
if n > 2 :
        n -= 1 # Use indentation to show what belongs in the if statement

elif n ==2 : 
        n*=2

        #Brackets are needed for Multi-Line Conditions

        # and = && (Logic and)
        # or = ||   (logic Or)

# While loops are similar

# For Loops
for i in range(5) :
        print (i)
# i here gets incremented automatically 0 to 4

for i in range (2,6) :
        # 2 to 5
        for i in range (5, 1, -1) :
        # -1  means decrementing by 1
        # -2 means decrementing by 2

# Division in Python is decimal by default

         x = (5/2)

 # if you want integer division you  have to use double //
         x = (5//2)

         ## Round downs always ( by 2 above )
         ## default so negative will round too
        x = (-3//2) # It will be -2 as it round downs to smaller number ( -2 is smaller than -1)

 
    # To make thing work like C++ , -3 / 2 could have rounded to 1 is to use int()
        x = int(-3//2)


          # In order to proper mod like C++, import math do math.fmod()
import math
x = math.fmod(-10, 3)

# More Math Helpers : 
# math.floor(number) gives explicitly rounds down
# math.ceil(number) explicitly rounds up
# math.sqrt()
#math.pow(base, power)
#Max int 
float("inf")
#Min int
float("-inf")

#Python numbers are infinite so they never overflow


## Arrays (Called Lists in Python)
arr = [1,2,3]
print(arr)


# Can be used as a stack as arrays in Python are dynamic
arr.append(4) # pushed         0(1)
arr.pop(4)   # popped          0(1)


arr.insert(1, 7) # Insert Value 7 on Index 1 || But insering sth in middle of an array is O(n)

# But index and change the value of an array
arr[0] = 2 #                O(1)


# Initialize arr of size n with default value of 1
# n = 5 
# arr = [1] * n

# Size of an array can be found by  len(arr)


arr[-1] # Last value of the array
arr[-2] # Second last value of the array

# Sublist (aka slicing an array)
arr[1:3]  # Value of arr[1], arr[2]

# Unpacking
a, b, c = [1, 2, 3] 
# Here a = 1, b = 2, c = 3

#Looping through arrays
for i in range (len(arr)) :
       x = arr[i]

       #Without index
       for n in arr :
             print (n)
       ## When you write for n in arr:, Python is doing something very specific:
       ##Iterating over the List: The for loop iterates over the list arr.
       ##Assigning Each Element to the Variable n: During each iteration of the loop, the next element of the list arr is assigned to the variable n.

       #With index and valuee

       for i, n in enumerate(arr) :
              print (i,n)

              #How It Works
              #The enumerate(arr) function generates pairs of (index, element) for each item in the list.
              #During each iteration, i is assigned the index, and n is assigned the value of the current element from arr.
              #The print(i, n) statement prints the index and value.



       # Looping through Multiple arrays simultaneously
       # with unpacking
       nums1 = [1, 3, 5]
       nums2 = [2,4,6]
       for n1, n2 in zip(nums1, nums2) :
              print(n1, n2)

              """
             

### Explanation

1. **Initialization**:
   - `nums1 = [1, 3, 5]`: This is the first list.
   - `nums2 = [2, 4, 6]`: This is the second list.

2. **For Loop with `zip`**:
   - `for n1, n2 in zip(nums1, nums2):`:
     - The `zip` function is used to pair up elements from `nums1` and `nums2` into tuples.
     - Each tuple contains one element from each list.
     - `n1` and `n2` are used to unpack these tuples into individual variables.

3. **Loop Body**:
   - `print(n1, n2)`: This line prints the values of `n1` and `n2`.

### How It Works

- The `zip(nums1, nums2)` function combines the two lists element-wise into pairs (tuples).
- During each iteration, `n1` is assigned the first element of the tuple (from `nums1`), and `n2` is assigned the second element of the tuple (from `nums2`).
- The `print(n1, n2)` statement prints the paired values.

### Step-by-Step Execution

Let's go through the loop step by step for the lists `nums1 = [1, 3, 5]` and `nums2 = [2, 4, 6]`.

1. **First Iteration**:
   - The first pair from `zip(nums1, nums2)` is `(1, 2)`.
   - `n1` is assigned the value `1` (from `nums1`).
   - `n2` is assigned the value `2` (from `nums2`).
   - `print(n1, n2)` prints `1 2`.

2. **Second Iteration**:
   - The second pair from `zip(nums1, nums2)` is `(3, 4)`.
   - `n1` is assigned the value `3` (from `nums1`).
   - `n2` is assigned the value `4` (from `nums2`).
   - `print(n1, n2)` prints `3 4`.

3. **Third Iteration**:
   - The third pair from `zip(nums1, nums2)` is `(5, 6)`.
   - `n1` is assigned the value `5` (from `nums1`).
   - `n2` is assigned the value `6` (from `nums2`).
   - `print(n1, n2)` prints `5 6`.

After the third iteration, there are no more elements in `nums1` and `nums2`, so the loop ends.

### Complete Example

Here is the complete code with example lists:

```python
nums1 = [1, 3, 5]
nums2 = [2, 4, 6]

for n1, n2 in zip(nums1, nums2):
    print(n1, n2)
```

When you run this code, it will output:

```
1 2
3 4
5 6
```

### Summary

- The `zip` function allows you to combine multiple lists element-wise into tuples.
- `for n1, n2 in zip(nums1, nums2):` means "for each pair of elements (one from `nums1` and one from `nums2`), assign the first element to `n1` and the second element to `n2`, and execute the following block of code."
- This approach is useful when you need to process multiple lists in parallel.

If you have any more questions or need further clarification, feel free to ask!
              """



# Reversing an arr
arr.reverse() # reverses the array
arr.sort()    # sorts the array (ascending by default) or alphabetical order if it's a string
arr.sort(reverse=True) # sorts in Descending order

# Custom sort ( by length of string )
arr.sort (key=lambda x:len(x))

"""
key=lambda x: len(x) means that each element x in the list will be passed to the lambda function, which returns the length of x.
"""

# List Comprehension 
arr = [i for i in range(5)]
"""
Structure Breakdown
List Comprehension: This is a concise way to create lists in Python. It allows you to generate a new list by applying an expression to each item in an existing iterable (like a range, list, etc.).

for i in range(5): This part is a for loop inside the list comprehension. It iterates over the numbers generated by range(5).

i: This is the expression applied to each item in the iterable. In this case, it simply takes the value of i from the for loop.
"""

#2-D Lists
# List Comprehension to make a 4x4 array

arr = [[0]*4 for i in range(4)]    # [0]*4 - This is a 1-D array that gets iterated to every row through " for i in range(4)"

# Strings are similar to arrays
s = "abc"
s[0:2] # Can be sliced similarly

# They are immutaable meaning they can't be modified by index. The characters of a string cant be reasigned
# We can update the string

s += "def"  # This actually means creating a new string "abcdef" - hence a O(n)
# String can be coverted into integer and vice versa :
x = int("Rat") 
x  = str(123)
# To find Ascii Value
x = ord("a")

# Combine a list of strings (with an empty string delimitor)
strings = ["ab", "cd", "ef"]
print(" " .join(strings))

"""
Explanation
List of Strings: strings = ["ab", "cd", "ef"]

This is a list containing three string elements: "ab", "cd", and "ef".
join Method: " ".join(strings)

The join method is a string method that takes an iterable (like a list) and concatenates its elements into a single string, with each element separated by the string used to call join.
Delimiter: " "

The delimiter is the string that separates each element in the resulting string. In this case, the delimiter is a single space " ".
How It Works
The join method iterates over each element in the strings list.
It concatenates each element, inserting the delimiter (a space " ") between each pair of elements.
Step-by-Step Execution
Initial List:

strings = ["ab", "cd", "ef"]
Using join with a Space Delimiter:

The join method concatenates the elements with a space as the delimiter.
It effectively performs the following concatenation:
"ab" + " " + "cd" + " " + "ef"
Resulting String:

The result is the single string: "ab cd ef"
"""



###Queues 
# Queues in Python are double ended queue by default
from collections import deque # importing deque to clear up queue
queue = deque()
queue.append(1) # right push
queue.append(2)

# One of the benefit of the queue over array stack is We can pop from the left at O(1)
queue.popleft()
queue.appendleft()
queue.pop # right pop

# At Queue, you can push and pop on both sides of the container













    








