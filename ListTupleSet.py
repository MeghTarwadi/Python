# Lists []:
# Ordered collection of elements.
# Mutable (can be changed after creation).
# Allows duplicate elements.
# Accessed by index.
# Defined using square brackets: my_list = [1, 2, 3]

# Tuples ():
# Ordered collection of elements.
# Immutable (cannot be changed after creation).
# Allows duplicate elements.
# Accessed by index.
# Defined using parentheses: my_tuple = (1, 2, 3)

# Sets {}:
# Unordered collection of unique elements.
# Mutable (can be changed after creation).
# Does not allow duplicate elements.
# Cannot be accessed by index.
# Defined using curly braces or the set() function: my_set = {1, 2, 3} or my_set = set([1, 2, 3])
# s=set([])   s=set(())   s=set({})

# Dictionaries {}:
# Dictionaries are unordered collections of items, each item having a key-value pair.
# They are mutable (can be changed after creation).
# Accessed by keys rather than indexes.
# Keys must be unique and immutable (strings, numbers, tuples), while values can be any data type.
# Defined using curly braces {} and colon : to indicate key-value pairs: my_dict = {'key1': 'value1', 'key2': 'value2'}

l=[1,12,1,5]                #kinda string
t=(5,9,5,"a")               #kinda array
s=set((49,8,49,9))          #
d={"a":11,"b":14,"c":11,"d":6}  #kinda structure


print(type(l))
for list in l:
    print(f"{list}")
# l.append(6)               #adds at last
# l.insert(2, 20)           #adds after specific...
# print(l)
# l.pop()                   #Removing last element
# l.remove(1)               #Removing by value
# del l[0]                  #Removing by index
# print(l)
# print(len(l))             #Length of the list
# print(sum(l))             #Sum of all elements
# l.sort()                  #to sort in ascending 1,12,97,100
# print(l)
# l.sort(reverse=1)         #sort in descending 100,97,12,1
# print(l)
# l.reverse()               #revrese existing list 
# print(l)
# l.clear()                 #to delete data in list
# print(l)
# cpy=l.copy()              #to copy whole
# print(cpy)

print(type(t))
for tuple in t:
    print(f"{tuple}")
# k=(9 in t)                #checks whether given input exits or not if yes than true else flase
# print(k)                    
t1 = [("yash", 18), ("megh", 17), ("parth", 19),
      ("harsh", 19), ("meet", 18), ("parama", 21),
      ("manan", 23), ("man", 22), ("piyush", 21)]
# print(18 in t1)
# for tuple in t1:
#     r1,r2=tuple
#     print("megh" in r1)
#     print(18==r2)
# print("\n")
# for name,age in t1:
#     print("megh" in name)
#     print(18==age)


print(type(s))
for set in s:
    print(f"{set}")
#can perform set operations


print(type(d))
for dict in d:
    print(f"{dict},{d[dict]}")
#     d[dict]=int(d[dict])+1
# for dict in d:
#     print(f"{dict},{d[dict]}")

