print("Hello World")
print('Doesn\'t')#use \ to escape quotes

#If you don’t want characters prefaced by \ to be interpreted as special characters, 
#you can use raw strings by adding an r before the first quote:
print('c:\some\name') #\n prints in the next line
print(r'c:\some\name') #using r at the start takes in the raw format

#String literals can span multiple lines. 
# One way is using triple-quotes: """...""" or '''...'''. 
# End of lines are automatically included in the string, 
# but it’s possible to prevent this by adding a \ at the end of the line. 
# The following example:
print('''\
Usage: things
    -h      Diwpla
    -H      wig
    ''')

#Strings can be concatenated (glued together) with the + operator, and repeated with *:
#3 times 'un' followed by 'ium'
print(3 * 'un' + 'ium')

#concatenante strings
prefix = 'py'
print(prefix+'thon')

#Indexing
word = 'python'
print(word[0])
print(word[4])

#use negative to start counting from right:
print(word[-1]) #prints last character
print(word[-2]) #second last character

#Slicing
#Slicing allows you to obtain substring:
print(word[2:4])
print(word[3:5])