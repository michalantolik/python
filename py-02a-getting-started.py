import os
os.system("cls")


print("#################################")
print("### ZEN")
print("#################################\n")

### Show Zen of Python
# import this


print("#################################")
print("### IMPORT")
print("#################################\n")

### Import "math" module
import math

### Import "factorial" function from "math" module
from math import factorial

### Import "factorial" function from "math" module (with alias)
from math import factorial as fac


print("#################################")
print("### HELP")
print("#################################\n")

### Run interactive help utility
# help()

### Show help for "math" module
# import math
# help(math)


print("#################################")
print('### "INT" TYPE')
print("#################################\n")

### Integer (decimal notation)
i = 10

### Integer (binary notation)
i = 0b10

### Integer (octal notation)
i = 0o10

### Integer (hexadecimal notation)
i = 0x10


print("#################################")
print('### "FLOAT" TYPE')
print("#################################\n")

### Float (standard notation)
f = 3.123
f = 3.0
f = 3.

### Float (scientific notation)
f = 3e8


print("#################################")
print('### "BOOL" TYPE')
print("#################################\n")

### Bool
b = True
b = False


print("#################################")
print('### "NONE" VALUE')
print("#################################\n")

### "None" value
a = None
if a is None:
    print('a is None')


print("\n#################################")
print("### TYPE CONVERSIONS")
print("#################################\n")

### float to int
i = int(3.5)

### string to int (implicit "10" base)
i = int("3")

### string to int (explicit "10" base)
i = int("3", 10)

### string to int (explicit "2" base)
i = int("1010", 2)

### string to int (explicit "16" base)
i = int("0xFF", 16)

### int to float
f = float(7)

### special float values
f = float("nan")
f = float("inf")
f = float("-inf")

### int to bool
b = bool(0)         # False
b = bool(42)        # True
b = bool(-1)        # True

### float to bool
b = bool(0.0)       # False
b = bool(0.207)     # True
b = bool(-1.23)     # True

### string to bool
b = bool("")         # False
b = bool("Spam")     # True
b = bool("True")     # True
b = bool("False")    # True

### list to bool
b = bool([])         # False
b = bool([1, 5, 9])  # True

### int to string
s = str(496)

### float to string
s = str(6.02e23)


print("#################################")
print("### IF STATEMENT, ELIF CLAUSE")
print("#################################\n")

if True:
    print("It's true!")
else:
    print("It's false")
    
    
if False:
    print("It's false!")
else:
    print("It's false")
    
    
if bool("eggs"):
    print("Yes please!")
else:
    print("No, thank you")
    
    
if "eggs":
    print("Yes please!")
else:
    print("No, thank you")


print("\n#################################")
print("### ELIF CLAUSE")
print("#################################\n")


n = 42
if n > 50:
    print("Greaten than 50")
elif n < 20:
    print("Less than 20")
else:
    print("Between 20 and 50")


print("\n#################################")
print("### WHILE LOOP")
print("#################################\n")

n = 4
while n != 0:
    print(n)
    n -= 1
    
print()

n = 5
while n:
    print(n)
    n -= 1
    
print()

n = 10
while n != 0:
    print(n)
    if n == 3:
        break
    n -= 1
    
    
print("\n#################################")
print("### FOR LOOP")
print("#################################\n")

cities = ["London", "New York", "Paris", "Oslo", "Helsinki"]
for city in cities:
    print(city)

print()

colors = {"crimson": 0xdc143c, "coral": 0xff7f50, "teal": 0x008080}
for color in colors:
    print(color, colors[color])

print()

for index, city in enumerate(cities):
    print(f"cities[{index}] = {city}")
    
print()

print("\n#################################")
print('### "STR" TYPE')
print("#################################\n")

# single quotes
s = 'hello'

# double quotes
s = "hello"

# hello world
s = "hello world"

# hello world (concatenated from two strings)
s = "hello" "world"

# access string characters
s = "parrot"
c = s[4]

# multi-line string #1
s = "This is\na multi-line\nstring"

# multi-line string #2
s = """This is
a multi-line
string"""

# raw strings (ignore escape sequences)
s = r"C:\Users\Merlin\Documents\Spells"

# capitalize first characters
s = "olso"
s = s.capitalize()

# split strings
s = "some string"
s = s.split()

# starts with
s = "first"
b = s.startswith("fi")

# ends with
s = "first"
b = s.endswith("st")

# length of string
count = len(s)


print("#################################")
print('### "BYTES" TYPE')
print("#################################\n")

# single quotes
b = b'data'

# double quotes
b = b"data"

# access byte object
b = b"some bytes"
d = b[0]

# split bytes
b = b"some bytes"
b = b.split()

# length of bytes
count = len(b)

# encode string as bytes and decode back
danish = "Har I et værelse til rådighed?"
encoded = danish.encode("utf-8")
decoded = encoded.decode("utf-8")


print("#################################")
print('### "LIST" TYPE')
print("#################################\n")

# empty list
a = []

# list of integers
a = [1, 9, 8]

# list of strings
a = ["apple", "organge", "pear"]

# access list elements
element = a[2]

# update list element
a[2] = "apple"

# list of integers and strings
a = [2, 4, "apple", 6, "organge", "pear", 8, 9]

# append element to list
a.append(1.618)

# length of list
count = len(a)

# list constructor
a = list("characters")


print("#################################")
print('### "DICT" TYPE')
print("#################################\n")

# empty dict
di = {}

# create dict
di = {'alice': 1, 'bob': 2, 'eve': 3}

# acces dict element by key
el = di['alice']

# update dict element
di['alice'] = 0

# add dict element
di['charles'] = 7

# length of dict
count = len(di)
