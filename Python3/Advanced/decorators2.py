
"""
    1. Demystifying Decorators for Simple Use.
    2. Helps in Building Libraries and Frameworks.
    3. Encapuslating details and providing simple interface.

"""

def simple_func1(x):
    '''
    @return - Square of given values
    '''
    return x*x

# Passing the reference to a varibaale
# dec_func is stored as a variable in Stack and it refers to address of simple_func
dec_func = simple_func1 
print(dec_func(10))  # Complete a simple test

'''
Call function in function by passing function reference as variable
'''
def simple_func2(func, x, y):
    '''
        func - A Function reference called.
        x - an Integer
        y - an Integer. 
        @return - Sum of outputs returned by func() referene called here
        
    '''
    return func(x) + func(y)

print(simple_func2(simple_func1, 10, 10)) # Test the output of function.

def simple_func3(x):
    print("x - {}".format(x))
    def inside_func(y):
        print("y - {}".format(y))
        return x + y
    return inside_func # returns the reference of inside_func
'''
      Found the trick here :)
    1. simple_func calls passing 4 and returns the refence of inside_func
    2. func_var will call the internal reference and it finally exceutes and outputs the results
'''    
func_var = simple_func3(4) # simple_func() returns the interval reference of inside_func
print(func_var(5)) # Calling inside_func with value
'''
Decorator function executes before main starts execution
'''
def trace(f):
    print("I was called here to return internal reference of g")
    def g(x):
        print(f.__name__, x)
        print("I am executing this time!")
        return f(x)
    return g


'''
    Syntactic Sugar of decorator as follows
    1. Simple decorators here.
    2. @trace is euqal to 
        var_func = trace(square) - returns the refernce to square.
        var_func(value) - returns the square value
 '''
 
@trace 
def square(x):
    return x*x

@trace
def add(x):
    return x+x

@trace
def difference(x):
    return x-x




'''
Lets try some here as it is tasting good :)
 1. Passing multiple arguments to decorator functions.
 2. So use *args to perform this.
'''

def trace2(f):
    def g(*args):
        print(f.__name__, args)
        return f(*args)
    return g

@trace2
def square2(x):
    return x*x

@trace2
def sum_of_squares(x,y):    
    return square2(x)+square2(y)



def main():
    print("Checking if decorators execution is done at import time or not")
    print(sum_of_squares(4,9))
    print(square(4))
    print(add(4))
    print(difference(10))

if __name__ == '__main__':
    main()
    



