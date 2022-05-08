import os
os.system("cls")
print()


print("###################################################################")
print("### TUPLE")
print("###################################################################")

print("""
- Immutable sequences of arbitrary objects
- Once created, the objects within them cannot be replaced or removed ...
- ... and new elements cannot be added
""")


print("##################################")
print("### Tuple basics")
print("##################################\n")

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

print("t1 =", t1)
print("t1[0] =", t1[0])
print("t1[2] =", t1[2])
print("len(t1) = ", len(t1))
print()

print("t2 = ", t2)
print()

print("t3 = ", t3)
print()

print("t4 = ", t4)
print("t4[2][1] = ", t4[2][1])
print()

print("t5 = ", t5)
print()

print("t6 = ", t6)
print()

print("t7 = ", t7)
print()

print("t8 = ", t8)
print()

print("t9 = ", t9)
print()

print("c = ", c)
print()

print("nc = ", nc)
print()


print("##################################")
print("### Tuple unpacking")
print("##################################")

print("""
- Tuple unpacking is destructuring operation that unpacks data structures ...
- ... into named references
- Tuple unpacking also works with nested tuples
""")


print("### Simple tuple unpacking\n")

def minmax(items):
    return min(items), max(items)

lower, upper = minmax([34, 52, 24, 56, 89, 99, 3])

print("lower =", lower)
print("upper =", upper)


print("\n### Nested tuple unpacking\n")

(a, (b, (c, d))) = (4, (3, (2, 1)))

print("a =", a)
print("b =", b)
print("c =", c)
print("d =", d)

print("\n### Swapping variables using tuples\n")

a = "jelly"
b = "bean"

a, b = b, a
