import os
os.system("cls")
print()


print("###################################################################")
print("### SETS")
print("###################################################################")

print("""
- Unordered MUTABLE collection of unique IMMUTABLE elements
- ... it's like a set of keys of a dictionary, but without values
""")


print("##################################")
print("### Set basics")
print("##################################\n")

s1 = ()                            # empty set,
s2 = (4, 53, 835, 6345, 33634636)  # set
s3 = set([1, 1, 2, 3, 3, 6, 7])    # set from list (duplicates discarded)


print("\n##################################")
print("### Set - adding new element")
print("##################################\n")

s3.add(99)
s3.add(99) # this will have NO EFFECT (element already exists)


print("\n####################################")
print("### Set - adding new elements (set)")
print("#####################################\n")

s3.update([101, 102, 103])


print("\n####################################")
print("### Set - removing element - remove()")
print("#####################################\n")

s3.remove(103)

# s3.remove(999) # this would prode KeyError (element  is not present)


print("\n####################################")
print("### Set - removing element - discard()")
print("#####################################\n")

s3.discard(103)

s3.discard(999) # this has NO EFFECT and does NOT produce any error

    
print("\n##################################")
print('### Set - "in" and "not in"')
print("##################################\n")

isIn = 6 in s3          # check whether 6 is in "s3"
isNotIn = 6 not in s3   # check whether 6 is NOT in "s3"


print("\n##################################")
print("### Set - iterating")
print("##################################\n")

for i in s3:
    print(i)
    
    
print("\n##################################")
print("### Set - shallow copy")
print("##################################\n")

s1 = {1, 2, 3, 4}

# "copy()" function
c1 = s1.copy()

# using "set()" constructor
c2 = set(s1)


print("\n##################################")
print("### Set - algebra")
print("##################################\n")

blueEyes = {"Olivia", "Harry", "Lily", "Jack", "Amelia"}
blondHair = {"Harry", "Jack", "Amelia", "Mia", "Joshua"}
smellHcn = {"Harry", "Amelia"}
tastePtc = {"Harry", "Lily", "Amelia", "Lola"}
oBlood = {"Mia", "Joshua", "Lily", "Olivia"}
bBlood = {"Amelia", "Jack"}
aBlood = {"Harry"}
abBlood = {"Joshua", "Lola"}

# union
blueEyesOrBlondHair = blueEyes.union(blondHair)

# intersection
blueEyesAndBlondHair = blueEyes.intersection(blondHair)

# difference
blondHardWithoutBlueEyes = blondHair.difference(blueEyes)

# symmetric_difference
eitherBlondHairOrBlueEyesExclusive = blondHair.symmetric_difference(blueEyes)

# issubset
isSubset = smellHcn.issubset(blondHair)

# issuperset
isSuperset = tastePtc.issuperset(smellHcn)

# isdisjoint
isDisjoint = aBlood.isdisjoint(oBlood)
