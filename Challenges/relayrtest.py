
string1 = ["!@#$This1123\n", "his", "here"]
match_string = "".join(sorted("this1123!@#$"))
print(match_string)
for each_string in string1:
    result = "".join(sorted(each_string))
    print(result.isprintable())
    if match_string == result:
        print("matched string ", match_string, result)
    print(result)
    