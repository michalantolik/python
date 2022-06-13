import os
os.system("cls")
print()


print("###################################################################")
print("### FILES")
print("###################################################################")

print("""
File Modes:

- Binary
- Text

open():

- opens a file for reading or writing
- file: the path to the file (required)
- mode: read (r), write (w), append (a), plus binary (b) or text (t)
- encoding: encoding to use in text mode

Class Invariant:

- Truth about an object that endure for its lifetime

Inheritance:

- Inheritance in Python is primirily useful for ...
- ... sharing implementation between classes
""")


print("\n##################################")
print("### Default encoding")
print("##################################\n")

import sys
defaultEncoding = sys.getdefaultencoding()


print("sys.getdefaultencoding() =", defaultEncoding)


print("\n##################################")
print("### Writing Text")
print("##################################\n")

# Open file for write in text mode
fw = open('dummy.txt', mode='wt', encoding='utf-8')

# "write()" returns the number of codepoints written (NOT the file length !)
fw.write("hello\n") 
fw.write("123\n")
fw.write("abc")

fw.close()


print("\n##################################")
print("### Appending Text")
print("##################################\n")

# Open file for write in append mode
fw = open('dummy.txt', mode='at', encoding='utf-8')

# writelines()
fw.writelines(
    ['Hello\n',
     'again'])

# write()
fw.write("123")

# Close the file
fw.close()


print("\n##################################")
print("### Reading Text")
print("##################################\n")

# Open file for read
fr = open('dummy.txt', mode='rt', encoding='utf-8')

# Read the whole file (this advances file pointer)
s1 = fr.read()

# Reset file pointer (only 0 and values form "tell()" are allowed)
fr.seek(0)

# Read five characters
s2 = fr.read(5)

# Reset file pointer (only 0 and values form "tell()" are allowed)
fr.seek(0)

# Read the file line by line
s3 = fr.readline()
s4 = fr.readline()
s5 = fr.readline()
s6 = fr.readline() # this return an empty string (end of file reached)

# Reset file pointer (only 0 and values form "tell()" are allowed)
fr.seek(0)

# Read all lines (into a list)
lines = fr.readlines()

# Close the file
fr.close()

# Print the results
print("fr.read() = ", s1)
print()
print("fr.read(5) = ", s2)
print()
print("fr.readline() = ", s3)
print("fr.readline() = ", s4)
print("fr.readline() = ", s5)
print("fr.readline() = ", s6)
print()
print("fr.readlines() = ", lines)


print("\n##################################")
print("### Iterating over Files")
print("##################################\n")

# Open file for read
fr = open('dummy.txt', mode='rt', encoding='utf-8')

# Iterate over lines
for line in fr:
    print(line) # this adds duplicate newline characters
    
# Reset file pointer (only 0 and values form "tell()" are allowed)
fr.seek(0)

print("\n----------------\n")
    
# Iterate over lines
import sys
for line in fr:
    sys.stdout.write(line) # no duplicate newline characters    

# Close the file
fr.close()


print("\n\n########################################")
print('### Closing Files with "finally"')
print("########################################\n")

try:
    fr = open('dummy.txt', mode='rt', encoding='utf-8')
    text = fr.read()
finally:
    fr.close()


print("########################################")
print('### "with-block" - like "using" in C#')
print("########################################\n")

with open('dummy.txt', mode='rt', encoding='utf-8') as fr:
    text = fr.read()
