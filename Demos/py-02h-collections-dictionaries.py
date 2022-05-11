import os
os.system("cls")
print()


print("###################################################################")
print("### DICTIONARY")
print("###################################################################")

print("""
- Fundamentals data structure in Python
- Maps keys to values
- Also known as map or associative array
- Keys must be unique and immutable (strings, numbers, tuples)
- Duplicate values are fine
- Values can be mutable (and often are)
""")


print("##################################")
print("### Dictionary basics")
print("##################################\n")

d1 = {}                                        # empty dictionary
d2 = {'alice': 1, 'bob': 2, 'eve': 3}          # dictionary

d3 = dict(a='alfa', b='bravo')                 # dictionary from keyword arguments

li = [('alice', 1), ('bob', 2), ('eve', 3)]    # dictionary from list of tuples
d4 = dict(li)

print("d1 =", d1)
print("d2 =", d2)
print("d3 =", d3)
print("d4 =", d4)

print("\n##################################")
print("### Dictionary - iterating")
print("##################################\n")

colors = {"crimson": 0xdc143c, "coral": 0xff7f50, "teal": 0x008080}

# print keys
for color in colors:
    print(color)
    
print()

# print keys
for key in colors.keys():
    print(key)
    
print()
    
# print keys and values
for color in colors:
    print(color, colors[color])

print()

# print keys and values
for key, value in colors.items():
    print(key, value)

print()

# print values
for value in colors.values():
    print(value)
    
print()


print("\n##################################")
print('### Dict - "in" and "not in"')
print("##################################\n")

isIn = 'alice' in d2          # check whether 'alice' key is in "d2"
isNotIn = 'alice' not in d2   # check whether 'alice' key is NOT in "d2"

print('d2 =', d2, "\n")
print('"alice" in d2 =', isIn)
print('"alice" not in d2  =', isNotIn)


print("\n##################################")
print('### List - "del"')
print("##################################\n")

print("d2 =", d2)

del d2['alice']   # remove item from the dictionary

print("d2 =", d2)


print("\n##################################")
print('### List - add new element')
print("##################################\n")

print("d2 =", d2)

d2['alice'] = 1

print("d2 =", d2)


print("\n##################################")
print("### Dictionary - merging")
print("##################################\n")

print("d2 =", d2)

d2 = {'alice': 1, 'bob': 2, 'eve': 3}
d3 = {'alfa': 4, 'bravo': 5}

# TRICKY - this updates "d2" and does NOT return a new object!
# TRICKY - if "d3" contains the same keys as "d2" ...
#          ... then the values for this keys will be replaced in "d2"
#          ... with the values from "d3"
d2.update(d3) 

print("d2 =", d2)


print("\n##################################")
print("### Dictionary - shallow copy")
print("##################################\n")

d2 = {'alice': 1, 'bob': 2, 'eve': 3}

# "copy()" function
c1 = d2.copy()

# using "dict()" constructor
c2 = dict(d2)


print("d2 =", d2)
print("c1 =", c1)
print("c2 =", c2)
