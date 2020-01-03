from collections import Counter

string = "aaaaabbbbbbvvvvvvccccccddddd"
string2 = "vvvvvvvvvvbbbbbbbbbbbbbvvvvvvvvvvvvvfffffffffff"
my_counter = Counter(string) # Summarizes the count of characters with counts
print(my_counter)
print(my_counter.values()) # All the counts of the keys Dicts
output = list(my_counter.elements())
unique_chars = set(output)
print(output)
print(unique_chars)


from collections import namedtuple

Point = namedtuple('Point', 'x, y')
pt = Point(1,-4)
print(pt)
print(pt.x, pt.y)

from collections import OrderedDict

