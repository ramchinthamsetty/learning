import itertools

data = list(range(1,10))

results = itertools.combinations(data, 2)
for each_result in results:
    print(each_result)

for i in itertools.count(0,2):
    if i > 10:
        break
    print(i)
    
