
def get_even_num(x):
    if not x & 1:
        return x

#Functional programming using Map, Filter, Reduce functions
list1 = range(1,100)
even_list1 = list(map(get_even_num,list1))
filter_list1 = list(filter(lambda x: x%2 == 0,list1)) # getting even numbers with single expression.
filter_list2 = list(filter(get_even_num,list1))


# Advanced Lambda Expressions
#Calling function in Lamda Expression

servers_config = {
        "AD-LDS": ['10.99.16.20', '10.99.16.21'],
        "SQL": ['10.99.16.27'],
        "Application": ['10.99.16.23', '10.99.16.26'],
        "Support": ['10.99.252.30', '10.99.252.31'],
        "ADFS": ['10.99.16.15', '10.99.16.17'],
        "WAP": ['10.99.252.42', '10.99.252.43']
    }

def func1(x,y):
    return x + y

add = lambda x, y: func1(x , y)
result = add(2,3)

result_map = map(add, range(1,100), range(1,100))

def get_ip_type_map(key, val_list):
    result_dict = {}
    for each_val in val_list:
        result_dict.update({each_val:key})
    return result_dict

func = lambda val: get_ip_type_map(val[0], val[1])

ip_map = map(func, servers_config.items())
list_map = list(ip_map)
# Result Printing here
print(result)
print(list(result_map))
print(list(ip_map))

final_dict = {}
for each_val in list_map:
    final_dict.update(each_val)
print(final_dict)