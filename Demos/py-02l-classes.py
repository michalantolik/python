import os
os.system("cls")
print()


print("###################################################################")
print("### CLASSES")
print("###################################################################")

print("""
Class:

- Defines the sctructure and behavior of objects
- Act as a template for creating new objects
- "self" keyword is similar to "this" in Java, C++, C#
- All class functions and attributes are public !!!

Class Initializer:

- "__init__()" is intializer, NOT constructor
- it initializes an object which already exists !!!

Class Invariant:

- Truth about an object that endure for its lifetime

Inheritance:

- Inheritance in Python is primirily useful for ...
- ... sharing implementation between classes
""")


print("\n##################################")
print("### MyEmpty class")
print("##################################\n")

class MyEmpty:
    pass

o1 = MyEmpty()
t1 = type(o1)


print("type(o1) = ", t1)
    

print("\n##################################")
print("### BasicFlight class")
print("##################################\n")

class BasicFlight:
    
    def number(self):
        return "SN060"

f1 = BasicFlight()

n1 = f1.number()
n2 = BasicFlight.number(f1) # also works, but AVOID this form

t2 = type(f1)


print("type(f1) = ", t2)
print()
print("f1.number() = ", n1)
print()
print("f2.number() = ", n2)


print("\n##################################")
print("### BetterFlight class")
print("##################################\n")

class BetterFlight:
    
    def __init__(self, number):
        self._number = number
    
    def number(self):
        return self._number

f3 = BetterFlight("SN060")
n3 = f3.number()
n4 = f3._number # possible, useful for debugging, AVOID in production
t3 = type(f3)


print("type(f3) = ", t3)
print()
print("f3.number() = ", n3)
print()
print("f3._number = ", n4)


print("\n##################################")
print("### Aircraft class")
print("##################################\n")

class Aircraft:
    
    def __init__(self, registration, model, num_rows, num_seats_per_row):    
        self._registration = registration
        self._model = model
        self._num_rows = num_rows
        self._num_seats_per_row = num_seats_per_row
    
    def registration(self):
        return self._registration
    
    def model(self):
        return self._model
    
    def seating_plan(self):
        return (range(1, self._num_rows + 1),
                "ABCDEFGHJK"[:self._num_seats_per_row])

a6 = Aircraft("G-EUPT", "Airbus A319", num_rows=22, num_seats_per_row=6)
r6 = a6.registration()
m6 = a6.model()
s6 = a6.seating_plan()
t6 = type(a6)


print("type(a6) = ", t6)
print()
print("r6.registration() = ", r6)
print()
print("a6.model() = ", m6)
print()
print("s6.seating_plan() = ", s6)
print()
print("type(a6) = ", t6)


print("\n##################################")
print("### GuardedFlight class")
print("##################################\n")

class GuardedFlight:
    """A flight with a particular passenger aircraft."""
    
    def __init__(self, number, aircraft):
        if not number[:2].isalpha():
            raise ValueError("No airline code in ", number)
        
        if not number[:2].isupper():
            raise ValueError("Invalid airline code ", number)
        
        if not (number[2:].isdigit() and int(number[2:]) <= 9999):
            raise ValueError("Invalid route number ", number)
        
        self._number = number
        self._aircraft = aircraft
    
    def number(self):
        return self._number
    
    def airline(self):
        return self._number[:2]
    
    def aircraft_model(self):
        return self._aircraft.model()
    

f5 = GuardedFlight("SN060", Aircraft("G-EUPT", "Airbus A319", num_rows=22, num_seats_per_row=6))
n5 = f5.number()
airline5 = f5.airline();
aircraft_model5 = f5.aircraft_model()
t5 = type(f5)


print("type(f5) = ", t5)
print()
print("f5.number() = ", n5)
print()
print("f5.airline() = ", airline5)
print()
print("f5.aircraft_model() = ", aircraft_model5)


print("\n##################################")
print("### Class inheritance")
print("##################################\n")

class BaseClass:
    
    def say_hello(self):
        print('Hello!')
        
class DerivedClass1(BaseClass):
    pass

class DerivedClass2(BaseClass):
    pass
    
    
bc = BaseClass()
dc1 = DerivedClass1()
dc2 = DerivedClass2()


bc.say_hello()
dc1.say_hello()
dc2.say_hello()
