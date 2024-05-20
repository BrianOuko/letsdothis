#print welcome message
print ('Hello world!')


#lesson II; 
#strings: working with textual data
#we can pass the data using a variable/ also we use backslash to escape problems with single/ double quotes in 
message = 'Bobby\'s world'
print(message)

#for multi-line strings, we use triple double quotes at the beginning and the end of a string
message= """Bobby's world was one of 
my favorite movies as a kid"""
print(message)

#manipulating individual characters in a string
message = 'Hello world'
# we can access specific elements using index
print (message[10])
#accessing a range of characters- the first index (0) is included while the last index isn't
print (message[0:5]) #same as print (message[:5])
print (message[6:]) #more on slicing

#applying methods on data types
print (message.upper()) #changes case to upper
print (message.count('l')) #the methods takes str arg and outputs the count
print(message.find('l')) #method takes arg and prints out index of string

#the replacement is not in-place, rather returns a new strings with the relevant values replaced
message ='Hello World'
message= message.replace('World', 'Universe') #Returns a copy with all occurrences of substring old replaced by new.

greeting ='Hello'
name = 'Mike'
message= greeting + name
print(message)#concatenates without spacing

message= greeting +', ' + name + '. Weclome.'
print(message) #spacing out using strings of spaces

#alternatively we could use a formatted string with placeholders ({}) for variables
greeting= 'Hello'
name = 'Mike'

message='{}, {}. Welcome.'.format(greeting, name) # string formatted using placeholders
print (message)

#we could also use fstrings to format the variables directly into the placeholders.
message =f'{name},{greeting}, Welcome'
print(message)

#more than that fstrings allow us to manipulate variables directly within the placeholders in the string
message =f'{name}, {greeting.upper()}'
print (message)

#some python hacks; dir and help functions
#in the print(dir()), the dir() function takes a variable, and shows all attributes and methods that we have access to wrt that function
print(dir(name))

#this section is commented purposefully, there's code here tho!
#with the help function, we can see these resources by parsing the string class into the function. It provides more detailed info than dir
#print (help(str))
#to be even more specific
#print(help(str.replace))




