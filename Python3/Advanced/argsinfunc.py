def func1(name_val, *args):
    for val in args:
        print(val, name_val)

def func2(name_val,**kwargs):
    for key,val in kwargs.items():
        print(key,val)
 
        
kwargs2 = {"arg3": 3, "arg2": "two","arg1":5}    
func2("rama", key1="ram",key2="rk",key3="ramya")


func1("rama", "python", "is","good", "to", "learn")

    