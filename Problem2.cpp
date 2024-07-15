/* 
2. Richest Customer Wealth

You are given an m x n integer grid accounts where accounts[i][j] is the amount of money the i​​​​​​​​​​​th​​​​ customer has in the j​​​​​​​​​​​th​​​​ bank. Return the wealth that the richest customer has.

A customer's wealth is the amount of money they have in all their bank accounts. The richest customer is the customer that has the maximum wealth.

 

Example 1:

Input: accounts = [[1,2,3],[3,2,1]]
Output: 6
Explanation:
1st customer has wealth = 1 + 2 + 3 = 6
2nd customer has wealth = 3 + 2 + 1 = 6
Both customers are considered the richest with a wealth of 6 each, so return 6.
Example 2:

Input: accounts = [[1,5],[7,3],[3,5]]
Output: 10
Explanation: 
1st customer has wealth = 6
2nd customer has wealth = 10 
3rd customer has wealth = 8
The 2nd customer is the richest with a wealth of 10.
Example 3:

Input: accounts = [[2,8,7],[7,1,3],[1,9,5]]
Output: 17
 

Constraints:

m == accounts.length
n == accounts[i].length
1 <= m, n <= 50
1 <= accounts[i][j] <= 100 */

class Solution {
public:
    int maximumWealth(vector<vector<int>>& accounts) {
        int max = 0 ;
        
        // for (int i= 0; i < accounts[0].size(); i++ ) {
        //          max  += accounts[0][i] ;
        // }
        for(int i = 0; i < accounts.size(); i++) {
               int wealth = 0;
            for(int j= 0 ; j < accounts[i].size(); j++) {
                     wealth += accounts[i][j] ;
            }
            if(wealth > max) {
                max = wealth ;
            }
        }
        return max ;
    }
};


//Things learned :
/* To calculate the size of rows and columns in a 2D array (or more precisely, a vector of vectors) in C++, you can use the `.size()` method provided by the `std::vector` class.





### Explanation

1. **Calculate Number of Rows**:
    ```cpp
    int numRows = matrix.size();
    ```
    The `size()` method of the outer vector (which represents the number of rows) is used to get the number of rows in the matrix.

2. **Calculate Number of Columns**:
    ```cpp
    if (numRows > 0) {
        int numCols = matrix[0].size();
    }
    ```
    To get the number of columns, we use the `size()` method of the inner vector. It is important to check if `numRows > 0` to avoid accessing an element in an empty matrix.

### Handling Empty or Irregular Matrices

- **Empty Matrix**: If the matrix has no rows, `matrix.size()` will return 0.
- **Irregular Matrix**: If the rows have different lengths, the number of columns may vary. In such cases, you might need to check each row individually.

Here is an example to handle irregular matrices:

```cpp
#include <vector>
#include <iostream>

int main() {
    // Example irregular 2D vector
    std::vector<std::vector<int>> matrix = {
        {1, 2, 3},
        {4, 5},
        {6, 7, 8, 9}
    };

    // Calculate the number of rows
    int numRows = matrix.size();
    std::cout << "Number of rows: " << numRows << std::endl;

    // Calculate the number of columns for each row
    for (int i = 0; i < numRows; ++i) {
        int numCols = matrix[i].size();
        std::cout << "Number of columns in row " << i << ": " << numCols << std::endl;
    }

    return 0;
}
```

This code calculates the number of columns for each row, which can vary if the matrix is irregular.*/