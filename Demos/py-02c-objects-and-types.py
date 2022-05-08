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
