# Core Python 3.6: Getting Started

## Installation and Start

**Operating Systems**
- Windows
- macOS
- Linux

**Ways to use Python**
- **Interactive Python** *(REPL - Read-Eval-Print-Loop)*
    - CTRL-Z + ENTER to leave on Windows
    - CTRL-D to leave on macOS/Linux

**Python 2 vs Python 3**
- Python 3 requires parentheses when calling `print` ...
- ... Python 2 doesn't

## Scalar Types
- `int`, `float`, `bool` (`True`/`False` values)
- `NoneType` (`None` value)

## Relational Operators
- `==`, `!=`, `<`, `>`, `<=`, `>=`

## Conditional statements
- `if` statement
- `else` and `elif` clauses

## Loops
- `while`
- `for`

## Collection types
- `dict`
    - fundamental data structure in Python
    - maps keys to values
    - also known as map or associative array
- `list`
    - **Mutable** sequence of objects
- `str`
    - **Immutable** sequence of unicode code points
    - ... single quotes or double quotes
- `bytes`
    - data type for sequences of bytes
    - raw binary data
    - fixed-width single-byte encodings

## Collection indexes
- `[-0]` - first element
- `[0]` - first element
- `[1]` - second element
- `[-1]` - last element
- `[-2]` - second last element

## Collection slicing
- `someList[start:stop]` - first element
- `someList[n:]` - from "n-th" to the end
- `someList[:n]` - from 0th to the "n-th-1"
- `someList[:]` - all elements `# can be used for copying !!!`
- `someList[2:]` - from "2nd" to the end
- `someList[:4]` - from 0th to the "3rd"
- `someList[1:3]` - `[someList[1], someList[2]]`
- `someList[1:-1]` - take all excepct the last element
- `someList[1:-2]` - take all excepct the last two elements

## Modularity

**Functions**

```python
# Function definition
def square(x):
    return x * x

# Function call
square(2)    
```

**Special Functions**
- naming convention: `__specialFunctionName__`
- so called "**dunders**"

**Module**
- For convenient import with API
- Code of imported module is executed during import

**Script**
- For convenient execution from the command line

**Program**
- Perhaps composed of many modules

**`__name__`** variable
- specially named variable ...
- to detect whether a module ...
- ... is run as a "standalone" script
    - ... **`__name__ == __main__`**
- ... or imported and run from another module
    - ... **`__name__ == moduleName`**

**Python Execution Model**
- `def` is a statement ...
- ... top-level functions are defined when
    - ... a module is imported
    - ... or run

**Passing command line arguments**

```python
# "greetings.py" script/module

import sys

def greet(name):
    print("Hello {}!".format(name))

def main(name):
    greet(name)
    
if __name__ == "__main__":
    main(sys.argv[1])

```

```bash
# Running "greetings.py" from command line

python greetings.py Michał

# output: Hello Michał!
```

**Docstrings**
- Literal strings which document functions, modules and classes
- They must be the first statement ...
- ... in the blocks for these constructs

```python
# greetings.py

"""Greet a user

Usage:

    python3 greetings.py <name>
"""


import sys


def greet(name):
    """Greet a user.

        Args:
            name: Name of a user.
        
        Returns:
            No return value.  
    """
    print("Hello {}!".format(name))


def main(name):
    """Greet a user.

    Args:
        name: Name of a user.
        
    Returns:
        No return value.  
    """    
    greet(name)
    

if __name__ == "__main__":
    main(sys.argv[1])
```

**Comments**
- Start with `#` and extend to the end of the line

**Shebang**
- First line of a Python script/module which starts with `#!` ...
- ... and allows to run correct Python interpreter
- ... `#!/usr/bin/env python3`

## Objects and Types

### **EVERTHING IN PYTHON IS AN OBJECT:**
### - Variables (even integers) ...
### - Modules, Functions, ...

**Python variables - Core Rules !!!**
- The assignment operator only binds an object to a name ...
- ... it never copies an object to a value
- So Python does NOT have variables ...
- ... in the sense of boxes holding a values
- Python has named references to objects !!! *(like labels)*

**Value Equality vs Identity Equality**

```python
p = [4, 7, 11]
q = [4, 7, 11]

# Value Equality

p == q # True

# Identity Equality

p is q # False

p is p # True
```

**Passing Arguments and Returning Values**
- Function arguments are transferred using **pass-by-object-reference** ...
- ... references to objects are copied, not the objets themselves

**Function Arguments - Default Values**
- Must come after those without default values

**Default Value Evaluation**
- `def` statement is executed at runtime
- default arguments are evaluated when `def` is executed
- Immutable default values do NOT cause problems
- Mutable default values can cause confusing effects !!!

### **CONCLUSION:**
### - ALWAYS USE IMMUTABLE OBJECTS ...
### - ... FOR DEFAULT VALUES !!

<br>

**Python Type System**
- **Dynamic**
    - type of objects are resolved at runtime
    - you do NOT declare types for function parameters
    - type declarations are unnecessary in Python
    - names can be rebound as necessary to objects of any type
- **Strong**

**Python Scopes (LEGB)**
- **Local**
    - inside the current function
    - ... function parameters
    - ... other function variables
- **Enclosing**
    - inside enclosing functions
    - ... function parameters
    - ... other function variables    
- **Global**
    - at the top level of the module
    - ... import statements
    - ... funcation definitions
    - ... class definitions
- **Local**
    - in the special built in modules

**Python Scope - Notes**
- Scopes in Python do NOT correspond to source code blocks

**Python Scope - Rebinding Global Names**
```python
count = 0
def set_count(c):
    # rebinding ...
    # ... global "count" variable will be used
    global count 
    count = c
```
**Checking Object type and its Attributes**
```python
import math
type(math)

print("dir(math) =", "\n", dir(math), "\n")
print("dir(math.sin) =", "\n", dir(math.sin), "\n")

print("math.sin.__name__ =", math.sin.__name__)
print("math.sin.__doc__ =", math.sin.__doc__)
```

## Collections - Tuples

**Tuple basics**
- Immutable sequences of arbitrary objects
- Once created, the objects within them cannot be replaced or removed ...
- ... and new elements cannot be added

```python
t1 = ("Norway", 4.953, 3)   # Tuple
t2 = t1 + ("a", "b", "c")   # Concatenated tuple
t3 = t1 * 3                 # Replicated tuple
t4 = ((1,2), (3,4), (5,6))  # Nested tuple
t5 = (391,)                 # Single element tuple ("," is required, otherwise -> int)
t6 = ()                     # Empty tuple
t7 = 4, 5, 2, 7, 6          # Parentheses omitted
t8 = tuple([45, 73, 56])    # Tuple constructor (from list)
t9 = tuple("Bicycle")       # Tuple constructor (from str)
c  = 5 in (4, 5, 6)         # Check if tuples contains given element
nc  = 5 not in (4, 5, 6)    # Check if tuples does NOT contains given element
```

**Simple tuple unpacking**
- Tuple unpacking is destructuring operation that unpacks data structures ...
- ... into named references

```python
def minmax(items):
    return min(items), max(items)

lower, upper = minmax([34, 52, 24, 56, 89, 99, 3])
```

**Nested tuple unpacking**
- Tuple unpacking also works with nested tuples

```python
(a, (b, (c, d))) = (4, (3, (2, 1)))
```

**Swapping variables using tuples**
```python
a = "jelly"
b = "bean"

a, b = b, a
```

## Collections - Strings

**String basics**
- IMMUTABLE sequence of unicode code points
- Single quotes or double quotes

```python
s1 = "hello"                        # String
s2 = "new" + "found" + "land"       # Concatenated string
s3 = "".join(["new", "found"])      # Concatenated string using "join" (more efficient)
s4 = "abc" * 3                      # Replicated string
```

**String - join and split**
```python
colors = ["red", "green", "blue"]  # List of strings
joined = ";".join(colors)          # Concatenated string
splitted = joined.split(";")       # Splitted string

print("colors = ", colors)
print("joined = ", joined)
print("splitted = ", splitted)
```

**String - partition**
```python
s6 = "unforgetable"
partitioned = s6.partition("forget")         # Partitioned string (into tuple)
partA, partB, partC = s6.partition("forget") # Partitioned and unpacked

print("s6 = ", s6)
print("partitioned = ", partitioned)
print("partA = ", partA)
print("partB = ", partB)
print("partC = ", partC)
```

**String - format**
```python
f1 = "The age of {} is {}".format("Jim", 32)
f2 = "The age of {0} is {1}".format("Jim", 32)
f3 = "The age of {0} is {1}. {0} lives in London".format("Jim", 32)
f4 = "The age of {name} is {age}. {name} lives in London".format(name="Fred", age=24)
f5 = "Galactic position x = {pos[0]}, y={pos[1]}, z={pos[2]}".format(pos=(65.2, 23.1, 82.2))

import math
f6 = "Math constants: pi={m.pi}, e={m.e}".format(m=math)
f7 = "Math constants: pi={m.pi:.3f}, e={m.e:.3f}".format(m=math)
```

**String - literal string interpolation (F-String)**
```python
# Literal string interpolation (F-String) ...
# ... available in Python >= 3.6

import math

f8 = f"one plus one is {1 + 1}"
f9 = f"Math constants: pi={math.pi}, e={math.e}"
```

**Range - basics**
- Sequence representing an arithmetic progression of integers
```python
# range(stop)
# range(start, stop)
# range(start, stop, step)

r1 = range(5)             # range(0, 5)        - 0, 1, 2, 3, 4
r2 = range(0, 5)          # range(0, 5)        - 0, 1, 2, 3, 4
r3 = range(6, 8)          # range(6, 8)        - 6, 7
r4 = range(10, 51, 10)    # range(10, 51, 10)  - 10, 20, 30, 40, 50
r5 = list(range(5, 10))   # range(5, 10)       - [5, 6, 7, 8, 9]

print("r1 =", list(r1))
print("r2 =", list(r2))
print("r3 =", list(r3))
print("r4 =", list(r4))
print("r5 =", list(r5))
```

**Range - `for` loop with `range`**
```python
for i in range(5):   # range(0, 5) - 0, 1, 2, 3, 4
    print(i)
```

**List**
```python
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
a2 = [1, 2, 6, 4, 6, 9, 8]                        # list of integers
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
print('### List - "find" and "count"')
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
```

**Collections - Dictionaries**
```python
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

del d2['alice']   # remove item from the dictionary


print("\n##################################")
print('### List - add new element')
print("##################################\n")

d2['alice'] = 1


print("\n##################################")
print("### Dictionary - merging")
print("##################################\n")

d2 = {'alice': 1, 'bob': 2, 'eve': 3}
d3 = {'alfa': 4, 'bravo': 5}

# TRICKY - this updates "d2" and does NOT return a new object!
# TRICKY - if "d3" contains the same keys as "d2" ...
#          ... then the values for this keys will be replaced in "d2"
#          ... with the values from "d3"
d2.update(d3) 


print("\n##################################")
print("### Dictionary - shallow copy")
print("##################################\n")

d2 = {'alice': 1, 'bob': 2, 'eve': 3}

# "copy()" function
c1 = d2.copy()

# using "dict()" constructor
c2 = dict(d2)

```

**Collections - Set**
```python
print("###################################################################")
print("### SETS")
print("###################################################################")

print("""
- Unordered MUTABLE collection of unique IMMUTABLE elements
- ... it's like a set of keys of a dictionary, but without values
""")


print("##################################")
print("### Set basics")
print("##################################\n")

s1 = ()                            # empty set,
s2 = (4, 53, 835, 6345, 33634636)  # set
s3 = set([1, 1, 2, 3, 3, 6, 7])    # set from list (duplicates discarded)


print("\n##################################")
print("### Set - adding new element")
print("##################################\n")

s3.add(99)
s3.add(99) # this will have NO EFFECT (element already exists)


print("\n####################################")
print("### Set - adding new elements (set)")
print("#####################################\n")

s3.update([101, 102, 103])


print("\n####################################")
print("### Set - removing element - remove()")
print("#####################################\n")

s3.remove(103)

# s3.remove(999) # this would prode KeyError (element  is not present)


print("\n####################################")
print("### Set - removing element - discard()")
print("#####################################\n")

s3.discard(103)

s3.discard(999) # this has NO EFFECT and does NOT produce any error

    
print("\n##################################")
print('### Set - "in" and "not in"')
print("##################################\n")

isIn = 6 in s3          # check whether 6 is in "s3"
isNotIn = 6 not in s3   # check whether 6 is NOT in "s3"


print("\n##################################")
print("### Set - iterating")
print("##################################\n")

for i in s3:
    print(i)
    
    
print("\n##################################")
print("### Set - shallow copy")
print("##################################\n")

s1 = {1, 2, 3, 4}

# "copy()" function
c1 = s1.copy()

# using "set()" constructor
c2 = set(s1)


print("\n##################################")
print("### Set - algebra")
print("##################################\n")

blueEyes = {"Olivia", "Harry", "Lily", "Jack", "Amelia"}
blondHair = {"Harry", "Jack", "Amelia", "Mia", "Joshua"}
smellHcn = {"Harry", "Amelia"}
tastePtc = {"Harry", "Lily", "Amelia", "Lola"}
oBlood = {"Mia", "Joshua", "Lily", "Olivia"}
bBlood = {"Amelia", "Jack"}
aBlood = {"Harry"}
abBlood = {"Joshua", "Lola"}

# union
blueEyesOrBlondHair = blueEyes.union(blondHair)

# intersection
blueEyesAndBlondHair = blueEyes.intersection(blondHair)

# difference
blondHardWithoutBlueEyes = blondHair.difference(blueEyes)

# symmetric_difference
eitherBlondHairOrBlueEyesExclusive = blondHair.symmetric_difference(blueEyes)

# issubset
isSubset = smellHcn.issubset(blondHair)

# issuperset
isSuperset = tastePtc.issuperset(smellHcn)

# isdisjoint
isDisjoint = aBlood.isdisjoint(oBlood)
```

**Collections - Protocols**
```python
print("###################################################################")
print("### PROTOCOLS")
print("###################################################################")

print("""
- Set of operations that a type must support to ...
- ... implement the protocol

- Protocols do NOT need to be defined as interfaces or base classes..
- ... types only need to provide working implementations
""")


print("##################################")
print("### Container")
print("##################################\n")

print("item in container")
print("item not in container")


print("\n##################################")
print("### Sized")
print("##################################\n")

print("len(container)")


print("\n##################################")
print("### Iterable")
print("##################################\n")

print("Yields items one by one as they are requested:")
print()
print("""for item in iterable:
    print(item)
""")

print("\n##################################")
print("### Sequence")
print("##################################\n")

print("item = sequence[index]")
print()
print("i = index(item)")
print()
print("count = sequence.count(item)")
print()
print("r = reversed(sequence)")
print()
```

**Pyton - Exceptions - Example Functions**
```python
import sys

DIGIT_MAP = {
    'zero':  '0',
    'one':   '1',
    'two':   '2',
    'three': '3',
    'four':  '4',
    'five':  '5',
    'six':   '6',
    'seven': '7',
    'eight': '8',
    'nine':  '9',
}


def convert(s):
    number = ''
    for token in s:
        number += DIGIT_MAP[token]
    x = int(number)
    return x


def tryConvert(s):
    try:
        number = ''
        for token in s:
            number += DIGIT_MAP[token]
        x = int(number)
        print("Conversion succeeded! x =", x)
    except KeyError:
        print("Conversion failed!")
        x = -1
    except TypeError:
        print("Conversion failed!")
        x = -1
    return x


def tryConvertShorter(s):
    x = -1                                      # <<< ----- LOOK HERE
    try:
        number = ''
        for token in s:
            number += DIGIT_MAP[token]
        x = int(number)
        print("Conversion succeeded! x =", x)
    except (KeyError, TypeError):               # <<< ----- LOOK HERE
        print("Conversion failed!")
    return x


def tryConvertShorterNoPrint(s):
    x = -1
    try:
        number = ''
        for token in s:
            number += DIGIT_MAP[token]
        x = int(number)
        print("Conversion succeeded! x =", x)
    except (KeyError, TypeError):
        pass                                    # <<< ----- LOOK HERE
    return x


def tryConvertEvenShorterNoPrint(s):
    try:
        number = ''
        for token in s:
            number += DIGIT_MAP[token]
        x = int(number)
        print("Conversion succeeded! x =", x)
    except (KeyError, TypeError):
        return -1                               # <<< ----- LOOK HERE
    return x


def tryConvertPrintExceptionMessage(s):
    try:
        number = ''
        for token in s:
            number += DIGIT_MAP[token]
        x = int(number)
        print("Conversion succeeded! x =", x)
    except (KeyError, TypeError):
        print(f"Conversion error: {e!r}", file=sys.stderr) # <<< ----- LOOK HERE
        return -1
    return x


def tryConvertReraiseException(s):
    try:
        number = ''
        for token in s:
            number += DIGIT_MAP[token]
        x = int(number)
        print("Conversion succeeded! x =", x)
    except (KeyError, TypeError):
        print(f"Conversion error: {e!r}", file=sys.stderr)
        raise                                              # <<< ----- LOOK HERE
    return x


def string_log(s):
    v = convert(s)
    return log(v)


def tryDivideByZeroReplaceAnotherException(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        raise ValueError()
    
    
def tryDivideByZeroReplaceAnotherExceptionBetter(x, y):
    if y == 0:
        raise ValueError("Cannot divde by zero")
    return x / y
```

**Python - Exceptions - Example Function Calls**
```python
import os
os.system("cls")
print()

from modules.exceptional import convert, tryConvert


print("###################################################################")
print("### EXCEPTIONS")
print("###################################################################")

print("""
- Exception handling is a mechanism for interrupting normal program flow ...
- ... and continuing in surrounding context (or code block)

Key Concepts:

1. Raising an exception
2. Handling an exception
3. Unhandled exceptions
4. Exception objects

Exceptions resulting from developer's errors.
Should be fixed by devloper in code.
Should NEVER be CAUGHT:

1. IndentationError
2. SyntaxError
3. NameError

""")


print("##################################")
print("### No exception")
print("##################################\n")

c1 = convert("one three three seven".split())
c2 = tryConvert("one three three seven".split())


print("\n##################################")
print("### Exception")
print("##################################\n")

# c3 = convert("around two grillion".split())  # this would raise "KeyError"
c4 = tryConvert("around two grillion".split()) # exception handled

# c5 = convert(512)     # this would raise "TypeError"
c6 = tryConvert(512)  # exception handled


print("\n##################################")
print("### Exception - IndexError")
print("##################################\n")

print('Sequences raise "IndexError" exceptions')

a = [1, 2, 3]
# a[99]                                        # this would raise "IndexError"


print("\n##################################")
print("### Exception - ValueError")
print("##################################\n")

# b = int("jim")                               # this would raise "ValuError"


print("\n##################################")
print("### Exception - KeyError")
print("##################################\n")

codes = dict(gb=44, us=1, no=47, fr=33)
# c = codes['de']                              # this would raise "ValuError"


print("\n##################################")
print("### Exception - TypeError")
print("##################################\n")

print('Avoid catching "TypeError" !!!\n')

def convert(s):
    if not isinstance(s, list):
        raise(TypeError("Argument must be a list"))
    # ...


print("\n##################################")
print("### Exception - LBYL & EAFP")
print("##################################\n")    

print('LBYL - Look before you leap\n')

print('EAFP - Easier to ask forgiveness than permission\n')


print("\n##################################")
print("### Exception - TypeError")
print("##################################\n")

print('Avoid catching "TypeError" !!!\n')

def convert(s):
    if not isinstance(s, list):
        raise(TypeError("Argument must be a list"))
    # ...
    

print("\n##################################")
print("### Exception - Try ... Finally")
print("##################################\n")    

try:
    # try block
    pass
finally:
    # executed no matter how the try block terminates
    pass
```

