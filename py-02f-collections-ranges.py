import os
os.system("cls")
print()


print("###################################################################")
print("### RANGE")
print("###################################################################")

print("""
- Sequence representing an arithmetic progression of integers
""")


print("##################################")
print("### Range basics")
print("##################################\n")

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


print("\n##################################")
print('### For loop with "range"')
print("##################################\n")

for i in range(5):   # range(0, 5) - 0, 1, 2, 3, 4
    print(i)
