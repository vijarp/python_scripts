import time

def calc_time(func):
    # added arguments inside the inner1,
    # if function takes any arguments,
    # can be added like this.
    def inner1(*args,**kwargs):
        # storing time before function execution
        begin = time.time()
        val =  func(*args,**kwargs)
        # storing time after function execution
        end = time.time()
        print("Total time taken in : ",func.__name__,end-begin)
        return val
    return inner1

@calc_time
def factorial1(n):
    ans = 1
    for i in range(1,n+1):
        ans = ans * i
    return ans


print(factorial1(4))