#working with key value pairs
#key-value pairs are known as hash maps - java has a hashmap class while js has a built-in object type that can be used to create hash maps
#keys can be any immutable data types (as with  key 1 below) but are mostly strings and integers
#just as an actual dictionary, the words we look up for are keys while their actual meanings are the values

students = {'name': 'John', 'age': 26, 'courses': ['Maths', 'Physics'], 1: 'immutable'}
print(students['name'])
print(students['courses'])
print(students[1])

#we can use the dict's get method to handle errors - try to access non-existint errors
print(students.get('courses'))
print(students.get('class')) #returns none

#rather than return none, a second argument could be parsed to the get method to specify the message to display in the  case of an error
print(students.get('class', 'Not found'))

#adding new entries - new entries to a pre-existing key overwrite its original value
students['class'] = 'Fifth year'
students ['name'] = 'Joan'
print(students.get('class'))
print(students.get('name'))

#to update multiple entries into the dict, we use the udpate method that takes a dict. as an arg.
students.update({'phone':555555555, 'height': 'tall'})
print(students)

#we can use del keyword to delete, or pop method (return the removed value)
del students['age']
print('dict. with age removed:', students) # here I renamed the dict.

#to handle potential key errors related to this, we could use if,in,else
if 'age' in students:
    del students['age']
else:
    print ('Key not found')

#using pop method to delete
popped = students.pop('name')
print (students)
print(popped)

#handling potential errors
popped = students.pop('name', None) #pop takes second value, the default to be displayed if the key is not found
if popped is not None:
    print(popped)
else:
    print('Key not available')

#loop through all dict. values
print(len(students)) #counts number of keys    
print(students.keys()) #lists all keys
print(students.values()) #lists all values
print(students.items()) #values and keys

for key in students: #only prints keys
    print(key)
    
#to print keys and values, we use the students.item(key, value)
for key, value in students.items():
    print(key, value)
