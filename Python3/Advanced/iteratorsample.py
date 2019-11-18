def get_even_num(x):
    if not x & 1:
        return x

#initializing a list function
list1 = range(1,100)
even_list1 = list(map(get_even_num,list1))
filter_list1 = list(filter(lambda x: x%2 == 0,list1)) # getting even numbers with single expression.
filter_list2 = list(filter(get_even_num,list1))
print(even_list1) 
print(filter_list1)
print(filter_list2)

