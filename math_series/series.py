def fibonacci(n):
    if (n == 0):
        return [0]
    elif n == 1:
        return [1]
    elif n == 2:
        return [0,1]
    elif (n < 0):
        return []
    else:
        y = fibonacci(n-1)
        # the new element the sum of the last two elements
        y.append(sum(y[:-3:-1]))
        return y
'''
    This function should have one parameter n. 
    & should return the nth value in the fibonacci series. 

    '''

def lucas(n):
    # return fibonacci(n, x=2, z=1)
    if n == 0:
        return 2
    elif n == 1:
        return n
    elif n > 0:
        return lucas(n-1) + lucas(n-2)
    elif n < 0:
        return lucas(n+2) - lucas(n+1)
    

'''
The function lucas should return the nth value in the lucas numbers 

    '''
    
def sum_series(n, x=0, z=1):
    #Determine nth number in series
    if n == 0:
        return x
    elif n == 1:
        return z
    else:
        return sum_series(n-1,x,z)+ sum_series(n-2,x,z)
'''
The required parameter will determine which element in the series to print. 
The two optional parameters will have default values of 0 and 1 and will determine 
the first two values for the series to be produced.
Calling this function with no optional parameters will produce numbers from the fibonacci series. 
Calling it with the optional arguments 2 and 1 will produce values from the lucas numbers. 
Other values for the optional parameters will produce other series.
    '''
    
    
# print(fibonacci(10))
# print(lucas(9))
print(sum_series(7,7,9))