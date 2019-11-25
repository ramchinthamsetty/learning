#Set functions in Python

def main():
    
    str1 = "Hello! this is a new world. This is again a new set"
    str2 = "Hello! this is a sample program"
    print(str1[:6]) #Till index 6 values from 0
    print(str1[2:5]) #Only from index 2 to index 5
    print(str1[:-5]) #Excluding last 5 characters

    print(str1.splitlines())

    l1 = str1.split(' ') #Split the string by spaces
    print(l1) #Converts words into lists
    l2 = str2.split(' ')
    s1 = set(l1)
    s2 = set(l2)
    print(s1.symmetric_difference(s2)) #Get unique words between data sets
    print(s1.intersection(s2)) # Get common words from data set
    print(s1.union(s2)) #Get all words without duplicates from both data sets

    #lists - Allows duplicates, Indexing, Mutable
    #Sets - No duplocates, Mutable, Unoredered
    #Dictionary - No duplicate keys, 
    # Tuples - Immutable, Indexing, 

    #lamda expressions
    #iterators & generators
    #

    return

if __name__ == '__main__':
    main()
    