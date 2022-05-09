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
    - fundamentals data structure in Python
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
