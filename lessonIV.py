#lists, tuples and sets
#lists are the most prevalent
courses = ['History', 'Maths', 'Physics', ' CS',]
print(courses)

print (courses[0]) # prints location of index 1
print (courses[2]) # prints location of index 2
print (courses[-1]) # we can also use negative indices. Eg using index -1 to access the last item

#we can also access values at a range of indices
print (courses[1:3]) #does not include the first index
print (courses[0:2]) #ignore first index so is same as print (courses [:2])
print (courses [:2])
print (courses [2:]) #spans from index 2 to the last

#methods that enable us to manipulate our lists
courses.append('Art') #appending a list - append takes a single argument
print (courses)

courses.insert(0, 'Art') #insert takes two args - one specifying the index, and the other, the string
print (courses)

courses_2= ['Art', 'Education']
courses.insert(0, courses_2) #inserts and append add the actual list to the orig. list, while extend adds the values of the second list to the first
print (courses)

courses.append(courses_2) #inserts and append add the actual list to the orig. list, while extend adds the values of the second list to the first
print (courses)

#extend allows us to add multiple values to our list - takes only one arg
courses.extend(courses_2)
print (courses)

#removing values
courses = ['History', 'Maths', 'Physics', 'CS']
print(courses)
courses.remove('CS')
print(courses)
#alternatively we'll use pop, which by default removes last value of list - useful for a stack 
courses.pop()
print(courses) 
#pop returns teh popped variable and thus we can store it
popper=courses.pop()
print(popper)


#methods to sort a list
courses = ['History', 'Maths', 'Physics', 'CS']
num = [3,6,8,1,0,3,4]
courses.reverse() #reverse the list
print(courses)
courses.sort() #sorts in ascending order
num.sort()#ascending numbers
print(courses)
print(num)

#we can also pass the reverse arg to the sort method to sort in descending order
courses.sort(reverse=True) #sorts in descending order
num.sort(reverse=True) #descending numbers
print(courses)
print(num)

#in the above the original list is affected - in place sorting
#the sorted function, instead, does not sort in place, hence its returned value must be stored in a new variable
courses = ['History', 'Maths', 'Physics', 'CS']
num = [3,6,8,1,0,3,4]
sorted_function= sorted(courses)# we parse the courses variable into sorted and store it in sorted function
print(courses) #courses maintains the orig. list
print(sorted_function) # sorted_function now contains new list variable 

#min, max, sum
print(sum(num))
print(min(num))
print(max(num))

#finding index of an item
print(courses.index('CS'))

#the in statement helps determine if an item is in a list (false/true)
print ('Art' in courses)
print ('CS' in courses)

#in is also relevant in looping using 'for'
for item in courses: #remember item is a variable not a keyword
    print(item) #prints the items of the list with in new lines

#to give the list's items indices
for index, course in enumerate(courses): #wrap courses in enumerate function which returns the index and value
    print (index, course)

#to force index to start at 1
for index, course in enumerate (courses, start=1):
    print()
    print(index, course)

#changing the list into a string seperated by something, eg , or space
course_str = ', '.join(courses) #joins the courses list by csv-ing it
print(course_str)

course_str = ' - '.join(courses) #joins the courses list by csv-ing it
print(course_str)

#changing the csv back into list
new_list = course_str.split(' - ')
print(new_list)

#replacing an item on a list's specific index
courses[-1] = 'Geography' #lists can allow replacing elements as they are immutable
print(courses)

###tuples and sets - tuples are immutable
#all list operations can be done on tuples except changing the original list
tuple_1 = ('History', 'Physics', 'CS', 'Geography')
set_1 = {'History', 'Physics', 'CS', 'Geography'}
print(tuple_1) # as tuple is immutable, they don't have as many manipulation methods
print(set_1)
 
 #sets are unordered, with no duplicates - are used for membership tests and to rid of duplicates
set_1 = {'History', 'Physics','History', 'CS', 'Geography'} #removes duplicate
print(set_1)
print ('Math' in set_1) #checks for membership

set_1 = {'History', 'Physics','History', 'CS', 'Geography'}
set_2 = {'History', 'Maths', 'Art and Design', 'History'}

print(set_1.intersection(set_2)) #courses in set_1 and set_2 
print(set_1.difference(set_2)) # courses in set_1 but not in set_2
print(set_1.union(set_2)) # courses in both sets


#creating empty lists, tuples, and sets
empty_list = [] # use the square brackets
empty_list = list () # or call the list constructor without args

empty_tuple = () #empty parentheses
empty_tuple = tuple() #or call the tuple constructor without args

# empty_set = directly using {} is wrong as this creates a dictionary
# to use curly brackets they need to be inside the set function
empty_set = set ({})
empty_set = set()

