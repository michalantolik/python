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
