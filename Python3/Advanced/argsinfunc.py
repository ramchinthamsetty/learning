

def func1(name_val, *args):
        """
                Function to parse arguments given. *args are simple arguments.
        """
        for val in args:
                # To print all values in the arguments.
                print(val, name_val)

def func2(name_val,**kwargs):
        """
                Function to process **kargs as key value pairs.
                Args can be anything, but as key value pairs.
                1. Application to constannt changing data types.
        """
        for key,val in kwargs.items():
                print(key,val)
 
 
 
func2("rama", key1="ram",key2="rk",key3="ramya")
func1("rama", "python", "is","good", "to", "learn")
# Passing more complex data as key value pairs.
func2("Passing Dict", value1 = ["This", "is", "Somthing","Challenging"], value2= {"key1":"value1"})



    