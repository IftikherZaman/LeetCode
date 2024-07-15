/* 
Given an integer n, return a string array answer (1-indexed) where:

answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
answer[i] == "Fizz" if i is divisible by 3.
answer[i] == "Buzz" if i is divisible by 5.
answer[i] == i (as a string) if none of the above conditions are true.
 

Example 1:

Input: n = 3
Output: ["1","2","Fizz"]
Example 2:

Input: n = 5
Output: ["1","2","Fizz","4","Buzz"]
Example 3:

Input: n = 15
Output: ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]
 

Constraints:

1 <= n <= 104
*/

class Solution {
public:
    vector<string> fizzBuzz(int n) {
        vector <string> answer (n) ;
        int i ;
        for (i = 0; i < n  ; i++) {

             if ((i+1)%5 == 0 && (i+1)%3 ==0 ) {
            answer[i] = "FizzBuzz" ;
        }
        else if ((i+1)%3 == 0) {
            answer[i] = "Fizz" ;
        }
        else if ((i+1)%5 == 0) {
             answer[i] = "Buzz" ;
        }
        else {
             answer[i] = to_string(i + 1) ;
        }

        }
        return answer ;
       
    }
};

//Things I learned //
/*
 1) Converting Integers to Strings:

answer[i - 1] = std::to_string(i);

2) No push_back Needed:
You directly assign the string to the element of the vector since each position in the vector is already reserved by initializing the vector with size n.