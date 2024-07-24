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
#



    








