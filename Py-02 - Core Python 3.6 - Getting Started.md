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
    - sequence of objects
    - **mutable**
- `str`
    - data type for string in Python
    - sequence of unicode code points
    - **immutable**
    - single quotes or double quotes
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

**Pyhon Execution Model**
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
- ... references to objects are copie, not the objets themselves

**Function Arguments - Default Values**
- Must come after those without default values
