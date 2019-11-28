
#takes arguments.

def func1(*args):
    for each_val in args:
        print(each_val)
    return

#Takes positional arguments. Key value pairs as arguments

def func2(**kargs):
    for key,val in kargs.items():
        print(key,val)
list1 = ["server","ip","cluster"]
dict1 = {"key1":"valuue1", "key2":"value2"}

#Calling the funcs with arguments, key value arguemnts.
func1("server","ip")
func2(value=dict1)





