import os
os.system("cls")
print()


print("###################################################################")
print("### ITERATION AND ITERABLES")
print("###################################################################")

print("""
Iterable:

- Object which can be iterated ...
- ... can be passed to "iter()" to produce an "iterator"

Iterator:

- Object which actually implement iteration ...
- ... can be passed to "next()" to get the next value in the sequence
- ... "next()" raises "StopIteration" exception when iterator is exhausted

Generator Functions:

- Iterable define by functions ...
- ... lazy evaluation
- ... can be used to model infinite sequences (or very large)
      - ... sensor readings
      - ... mathematical sequences
      - ... contents of large files
- ... composable into pipelines
- ... MUST include at leat one "yield" statement
- ... may also include "return statements"
- ... only do enough work to produce requested data

Comprehension:

- Concise syntax for describing lists, sets and dictionaries
- Readable and expressive
- Close to natural language

Generator Expressions:

- Comprehension-like expressions ...
- ... which produce "generator" object
- To recreate a generator from a generator expression ...
- ... you must execute the expression again
""")


print("\n##################################")
print("### Iteration Procotols")
print("##################################\n")

iterable = ["Sprint", "Summer", "Autumn", "Winter"]
iterator = iter(iterable)

next(iterator) # returns "Spring"
next(iterator) # returns "Summer"
next(iterator) # returns "Autumn"
next(iterator) # returns "Winter"
# next(iterator) # throws "StopIteration" exception


print("##################################")
print("### List Comprehensions")
print("##################################\n")

words = "My name is Johnny".split()

comp1 = [word for word in words]
comp2 = [len(word) for word in words]


print("word = ", words)
print()

print("SYNTAX: [expr(item) for item in iterable]")
print()

print("[word for word in words]      = ", comp1)
print("[len(word) for word in words] = ", comp2)


print("\n##################################")
print("### Set Comprehensions")
print("##################################\n")

comp3 = {x for x in range(10)}


print("SYNTAX: {expr(item) for item in iterable}")
print()

print("{x for x in range(20)}      = ", comp3)


print("\n##################################")
print("### Dict Comprehensions")
print("##################################\n")

countryToCapital = { 'United Kingdom': 'London',
                     'Brazil': 'Brasilia',
                     'Morocoo': 'Rabat',
                     'Sweden': 'Stockholm' }

capitalToCountry = {capital: country for country, capital in countryToCapital.items()}


print("SYNTAX: {keyExpr: ValueEpxr for key, value in dictionary}")
print()

from pprint import pprint as pp
pp(capitalToCountry)


print("\n##################################")
print("### Filtering Comprehensions 1")
print("##################################\n")

comp4 = [x for x in range(11) if x % 2 == 0]


print("SYNTAX: [expr(item) for item in iterable if condition]")
print()

print("[x for x in range(11) if x % 2 == 0] = ", comp4)


print("\n##################################")
print("### Filtering Comprehensions 2")
print("##################################\n")

comp5 = {x: (1, x, x*x) for x in range(11) if x % 2 == 0}


print("SYNTAX: [expr(item) for item in iterable if condition]")
print()

print("[x: (1, x, x*x) for x in range(11) if x % 2 == 0] = \n")
from pprint import pprint as pp
pp(comp5)


print("\n##################################")
print("### Generator Functions")
print("##################################\n")

def gen123():
    yield 1
    yield 2
    yield 3
    
for x in gen123():
    print(x)
    

print("\n##################################")
print("### Infinite Generator Functions")
print("##################################\n")

def fibonacci():
    yield 0
    yield 1
    a = 0
    b = 1
    while True:
        yield a + b
        a, b = b, a + b

# import time
# for x in fibonacci():
#     print(x)
#     time.sleep(3)


print("\n##################################")
print("### Generator Expressions")
print("##################################\n")

print("SYNTAX: (expr(item) for item in iterable)")
print("SYNTAX: func((expr(item) for item in iterable))")
print()

squares = (x*x for x in range(1, 11))
           
someSum = sum(x for x in range(11) if x % 2 == 0)

print("type(squares) = ", type(squares))
print("list(squares) = ", list(squares))
print()
print("type(someSum) = ", type(someSum))
print("someSum = ", someSum)    


print("\n##################################")
print('### "any", "all"')
print("##################################\n")

anyTrue = any([False, False, True])
allTrue = all([False, False, True])

print("any([False, False, True]) =", any([False, False, True]))
print()
print("all([False, False, True]) =", all([False, False, True]))
