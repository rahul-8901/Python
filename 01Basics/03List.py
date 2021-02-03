fruits = ['Apple', 'Orange', 'Lemon', 'Grapes']
people = ['andrew', 'junju', 'Narendra', 'Rahul']
print(fruits)
print(fruits[2])# indexing returns the item
print(fruits[:2])# slicing returns a new list
print(fruits[:])
print(fruits + people)

fruits[3] = 64 # Lists are mutable, Unlike strings 
print(fruits)

fruits.append('new fruit')
print(fruits)

#Assignment to slices is also possible
fruits[1:3] = ['ORANGE', 'Lemon']
print(len(fruits))

#nested Lists
peopleGroups = [['Naren', 'Adil', 'Junju'], ['Rahul', 'Murali', 'Sindhuja']]
print(peopleGroups)