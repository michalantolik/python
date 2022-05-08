import os
os.system("cls")


print("###################################################################")
print("### VALUE EQUALITY vs IDENTITY EQUALITY")
print("###################################################################\n")

p = [4, 7, 11]
q = [4, 7, 11]

print("p =", p)
print("q =", q, "\n")
print()

print("### Value Equality:\n")
print("p == q :", p == q, "\n") # True

print("### Identity Equality:\n")
print("p is q :", p is q) # False
print("p is p :", p is p) # True


print("\n###################################################################")
print("### FUNCTION ARGUMENTS - DEFAULT VALUES")
print("###################################################################\n")

def banner(message, border="-"):
    line = border * len(message)
    print(line)
    print(message)
    print(line)
    
banner("Hello My Friend!")
print()
banner("Hello My Friend!", "*")
print()


print("###################################################################")
print("### FUNCTION ARGUMENTS - NAMED ARGUMENTS")
print("###################################################################\n")

banner(message="Hello My Friend!", border="*")
print()

banner(border="*", message="Hello My Friend!")
print()


print("###################################################################")
print("### FUNCTION ARGUMENTS - DEFAULT VALUE EVALUATION - TRICKY !!!")
print("###################################################################\n")

print("""
- Default values are evaluated only ONCE ...
- ... when a "def" statement is executed !!!

-----------------------------
See the function calls below:
-----------------------------

""")


import time
def showCurrentTime(arg=time.ctime()):
    print(arg)
    
showCurrentTime()
time.sleep(1)
showCurrentTime()
time.sleep(1)
showCurrentTime()

print("\n###################################################################")
print("### FUNCTION ARGUMENTS - MUTABLE DEFAULT VALUE - TRICKY !!!")
print("###################################################################\n")

#######################################
### Tricky behavior - AVOID !!!
#######################################
def add_spam(menu=[]):
    menu.append("spam")
    return menu

# Calling "add_spam()" will result with ['spam', 'spam'].

#######################################
### Tricky behavior - SOLUTION !!!
#######################################
def add_spam(menu=None):
    if menu is None:
        menu = []
    menu.append("spam")
    return menu

# Calling "add_spam()" more than once will result with ['spam'] for each call.
# This is because a new object is created and pointed to by the "menu" variable ...
# ... in each call of the "add_spam()" (provided that no argument is passed).

print("###################################################################")
print("### SCOPES - REBIND GLOBAL NAMES")
print("###################################################################\n")

count = 0
def set_count(c):
    global count # rebinding - global "count" variable will be used
    count = c

print("###################################################################")
print("### CHECKING OBJECT TYPE AND ITS ATTRIBUTES")
print("###################################################################\n")

import math
type(math)

print("dir(math) =", "\n", dir(math), "\n")
print("dir(math.sin) =", "\n", dir(math.sin), "\n")

print("math.sin.__name__ =", math.sin.__name__)
print("math.sin.__doc__ =", math.sin.__doc__)
