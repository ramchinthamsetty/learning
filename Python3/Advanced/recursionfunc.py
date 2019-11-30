'''
    Benefits & Application of recursive functions.
    1. Avoid loops
    2. 
'''

def recursive_func(n, total):
    print(n)
    if n== 0:
        return total
    else:
        return recursive_func(n-1,total+n)


print("Simple iteration", recursive_func(0,0))
print("Second iteration", recursive_func(2,1))
