# Python code to break out of multiple
# loops by using a flag variable
 
 
def elementInArray(arr, x):
    flag = False  # Defining the flag variable
 
    # Iterating through all
    # lists present in arr:
    for i in arr:
       
        # Iterating through all the elements
        # of each of the nested lists in arr:
        for j in i:
 
            # Checking if any element in the
            # nested list is equal to x
            # and assigning True value to
            # flag if the condition is met
            # else printing the element j:
            if j == x:
                flag = True
                print('Element found')
                break
            else:
                print(j)
                 
        # If the inner loop terminates due to
        # the break statement and flag is True
        # then the following if block will
        # be executed and the break statement in it
        # will also terminate the outer loop. Else,
        # the outer loop will continue:
        if flag == True:
            break
 
 
# Driver Code:
arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
x = 4
elementInArray(arr, x)


#Product from itertools
from itertools import product
for x, y in product(range(10), range(10)):
    #do whatever you want
    break

#Comprehension
print([(x, y) for y in ['y1', 'y2'] for x in ['x1', 'x2']])