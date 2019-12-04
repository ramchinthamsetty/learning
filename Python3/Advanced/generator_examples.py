import itertools as it

simple_list = list(range(1,10))
iter1 = iter(simple_list) 
# Calling Iterator to get values
print(next(iter1))
print(next(iter1))
print(next(iter1))
print(next(iter1))

'''
Example of a simple iterator here
'''
while 1: 
    try:
        print(next(iter1))
    except StopIteration as e: #Iterator will raise exception when there is no data in list
        print("Exception occured here, because there is no data")
        break
    
    
iter2 = iter(simple_list)
'''
Demo of itertools libraries here
count function - to increment the range of values to start with value by incrementing by value 5.
'''
even_values = it.count(start=1,step=5)
print(list(next(even_values) for _ in range(5)))