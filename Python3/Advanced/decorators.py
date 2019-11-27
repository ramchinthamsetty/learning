import os
import inspect

#Passing function reference as variable
def hello_world(func):
    print("hello world")
    print(func.__repr__())
    def hello_there():
        print("hello there",func)  #accessing variales from parent function, called Closure.
    func() #Calling the function Hi by reference
    hello_there() #calling function that is defined in function scope
    print(hello_there)

def hi():
    print("Hi! there")


print(hi.__repr__()) #Address location of Hi function
hello_var = hello_world #Assigning the reference to variable
print(hello_var)
hello_var(hi)
# hello_there() #Gives Name error

