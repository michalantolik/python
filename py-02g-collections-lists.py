import os
os.system("cls")
print()


print("###################################################################")
print("### LIST")
print("###################################################################")

print("""
- Mutable collection of elements
""")


print("##################################")
print("### List basics")
print("##################################\n")

a1 = []                                           # empty list
a2 = [1, 2, 6, 4, 6, 6, 8]                        # list of integers
a3 = a2 * 4                                       # replicated list
a4 = [0] * 9                                      # replicated list
a5 = ["apple", "organge", "pear"]                 # list of strings
a6 = [2, 4, "apple", 6, "organge", "pear", 8, 9]  # list of integers and strings

print("a1 =", a1)
print("a2 =", a2)
print("a3 =", a3)
print("a4 =", a4)
print("a5 =", a5)
print("a6 =", a6)


print("\n##################################")
print("### List indexing")
print("##################################\n")

a2[0] = 56            # update first element
first = a2[0]         # access first element
first = a2[-0]        # access first element
last = a2[-1]         # access last element
secondLast = a2[-2]   # access second last element

print("a2 =", a2, "\n")
print("first =", first)
print("last =", last)
print("secondLast =", secondLast)


print("\n##################################")
print("### List slicing")
print("##################################\n")

s1 = a2[2:5]     # access slice - [a2[2], a2[3], a2[4]]
s2 = a2[3:]      # access slice - [a2[3], a2[4], ..., a2[-1]]
s3 = a2[:3]      # access slice - [a2[0], a2[1], a2[2]]
s4 = a2[3:-1]    # access slice - [a2[3], a2[4], ..., a2[-2]]
s5 = a2[3:-2]    # access slice - [a2[3], a2[4], ..., a2[-3]]
s6 = a2[:]       # shallow copy of a list

print("a2 =", a2, "\n")
print("a2[2:5] =", s1)
print("a2[3:] =", s2)
print("a2[:3] =", s3)
print("a2[3:-1] =", s4)
print("a2[3:-2] =", s5)
print("a2[:] =", s6)


print("\n#######################################")
print('### List - "len"')
print("#######################################\n")

count = len(a2)  # length of list

print("a2 =", a2, "\n")
print("len(a2)  =", count)


print("\n##################################")
print('### List - "index" and "count"')
print("##################################\n")

index = a2.index(6)      # find the index of the first list element which is equal to "6"
count = a2.count(6)      # count the number of occurrences of "6" in the list

print("a2 =", a2, "\n")
print("a2.index(6)  =", index)
print("a2.count(6)  =", count)


print("\n##################################")
print('### List - "in" and "not in"')
print("##################################\n")

isIn = 6 in a2          # check whether "6" is in the list
isNotIn = 6 not in a2   # check whether "6" is NOT in the list

print("a2 =", a2, "\n")
print("6 in a2   =", isIn)
print("6 not in a2  =", isNotIn)


print("\n##################################")
print('### List - "append" and "insert"')
print("##################################\n")

a2.append(1.618)      # append element to list
a2.insert(2, "536")   # insert element "536" into the list under index [2]

print("a2 =", a2, "\n")
print("6 in a2   =", isIn)
print("6 not in a2  =", isNotIn)


print("\n##################################")
print('### List - "del" and "remove"')
print("##################################\n")

del a2[2]      # remove element from the list
a2.remove(6)   # remove element "6" from the list (first occurrence)


print("\n##################################")
print('### List - "extend"')
print("##################################\n")

a2 += [1, 2, 3]          # extend the list
a2.extend([1, 2, 3])     # extend the list


print("\n#######################################")
print("### Reverse and sort - passed object")
print("#######################################\n")

a2.reverse()             # reverse the list
a2.sort()                # sort the list (in ascending order)
a2.sort(reverse=True)    # sort the list (in descending order)

a7 = "This is an example string".split()  # list of strings
a7.sort(key=len)                          # sort by "len"


print("\n#######################################")
print("### Sorted - into new object")
print("#######################################\n")

sorted1 = sorted(a2)                      # sort the list (in ascending order)
sorted2 = sorted(a2, reverse=True)        # sort the list (in descending order)

a7 = "This is an example string".split()  # list of strings
sorted3 = sorted(a7, key=len)             # sort by "len"


print("\n#######################################")
print("### Reversed - into reversed iterator")
print("#######################################\n")

rev1 = reversed(a2)             # reverse the list
