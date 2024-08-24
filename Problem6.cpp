// 392. Is Subsequence.

// Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

// A subsequence of a string is a sequence of characters that can be obtained by deleting some (or none) of the characters from the original string, while maintaining the relative order of the remaining characters. For example, "ace" is a subsequence of "abcde" while "aec" is not. ***

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = j = 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1

        return i == len(s)






// Function Declaration: def isSubsequence(self, s: str, t: str) -> bool:
// This line defines a method named isSubsequence inside a class (Solution). Here's a breakdown of each part:

// def: This keyword is used to define a function or method in Python.

// isSubsequence: This is the name of the method. It's a descriptive name indicating that the method checks if one string (s) is a subsequence of another string (t).

// self: This is a reference to the instance of the class. When defining methods in a class, self is the first parameter and represents the instance of the class. It allows the method to access the attributes and other methods of the class.

// s: str and t: str: These are the parameters of the method. The part after the colon (: str) is a type hint, indicating that both s and t are expected to be strings (str). These type hints don't enforce the data type but provide clarity on what type of arguments the method expects.

// -> bool: This is also a type hint, indicating the return type of the method. In this case, it suggests that the method will return a boolean value (True or False).

// Summary:
// This method, isSubsequence, is designed to take two string arguments, s and t, and return a boolean (True or False). The self parameter allows the method to be part of a class, and the type hints (: str and -> bool) clarify the expected input and output types.







// Last Line: return i == len(s)
// This line is critical as it determines the output of the function. Here's what it does:

// i == len(s):

// i: This is the index that was incremented each time a character in s matched a character in t during the loop.
// len(s): This is the length of the string s.
// i == len(s): This checks if the index i has reached the length of the string s, which would mean that every character in s has been matched sequentially within t.
// return:

// The return statement sends the result of the comparison (i == len(s)) back as the output of the function.
// If i == len(s) evaluates to True, it means all characters of s have been found in the correct order within t, so the function returns True.
// If i == len(s) evaluates to False, it means not all characters of s were found in sequence in t, so the function returns False.
// Summary:
// The last line of the function determines whether the string s is a subsequence of the string t. If the index i has moved through all characters in s (i.e., i == len(s)), the function returns True. Otherwise, it returns False.






