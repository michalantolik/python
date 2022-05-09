import os
os.system("cls")
print()


print("###################################################################")
print("### RANGES")
print("###################################################################")

print("""
- IMMUTABLE sequence of unicode code points
- Single quotes or double quotes
""")


print("##################################")
print("### String basics")
print("##################################\n")

s1 = "hello"                        # String
s2 = "new" + "found" + "land"       # Concatenated string
s3 = "".join(["new", "found"])      # Concatenated string using "join" (more efficient)
s4 = "abc" * 3                      # Replicated string

print("s1 =", s1)
print("s2 =", s2)
print("s3 =", s3)
print("s4 =", s4)


print("\n##################################")
print("### Join and split")
print("##################################\n")

colors = ["red", "green", "blue"]  # List of strings
joined = ";".join(colors)          # Concatenated string
splitted = joined.split(";")       # Splitted string

print("colors = ", colors)
print("joined = ", joined)
print("splitted = ", splitted)


print("\n##################################")
print("### Partition")
print("##################################\n")

s6 = "unforgetable"
partitioned = s6.partition("forget")         # Partitioned string (into tuple)
partA, partB, partC = s6.partition("forget") # Partitioned and unpacked

print("s6 = ", s6)
print("partitioned = ", partitioned)
print("partA = ", partA)
print("partB = ", partB)
print("partC = ", partC)


print("\n##################################")
print("### Format")
print("##################################\n")

f1 = "The age of {} is {}".format("Jim", 32)                                                 # Formatted string
f2 = "The age of {0} is {1}".format("Jim", 32)                                               # Formatted string
f3 = "The age of {0} is {1}. {0} lives in London".format("Jim", 32)                          # Formatted string
f4 = "The age of {name} is {age}. {name} lives in London".format(name="Fred", age=24)        # Formatted string                               # Formatted string
f5 = "Galactic position x = {pos[0]}, y={pos[1]}, z={pos[2]}".format(pos=(65.2, 23.1, 82.2)) # Formatted string

import math
f6 = "Math constants: pi={m.pi}, e={m.e}".format(m=math)                                     # Formatted string
f7 = "Math constants: pi={m.pi:.3f}, e={m.e:.3f}".format(m=math)                             # Formatted string

print("f1 = ", f1)
print("f2 = ", f2)
print("f3 = ", f3)
print("f4 = ", f4)
print("f5 = ", f5)
print("f6 = ", f6)
print("f7 = ", f7)


print("\n################################################")
print("### Literal string interpolation (F-String)")
print("#################################################\n")

f8 = f"one plus one is {1 + 1}"                        # Literal string interpolation (F-String), Python >= 3.6
f9 = f"Math constants: pi={math.pi}, e={math.e}"       # Literal string interpolation (F-String), Python >= 3.6

print("f8 = ", f8)
print("f9 = ", f9)
