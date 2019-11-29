def func_read_input():
    values = input("enter values")
    print(type(values))
    list_vals = values.split(' ')
    print([int(val) for val in list_vals])
    
    return

func_read_input()
