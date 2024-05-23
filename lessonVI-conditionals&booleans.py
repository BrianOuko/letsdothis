#conditionals help control the flow of execution
#conditional if executes the code just below the if statement when the condition is true
#if false, the condition just below the if is 
if True:
    print("I'm true and real")
 
if False:
    print('This was true') #prints nothing

#using conditionals to execute code
language = 'Python'
if language == 'Python':
    print('I a not a snake')
else:
    print('green grass')

if language != 'Python':
    print('I a not a snake')
else:
    print('green grass')

if language > 'Python': #in .py this checks for alphabetical order
    print('I a not a snake')
else:
    print('green grass')


#using else-if serves as an alt. to the switch-case statement in Java 
speak = 'Python'
language = 'PHP'
if speak !='Python':
    print('I am not a snake')
elif language == 'PHP':
    print('Language is the hard-ass PHP')
else:
    print('No match!')

#we can supercharge our else, and elif statements with booleans - keywords and, or, not
user = 'admin'
logged_in = False

if user== 'admin' and logged_in: #does not allows access (logegd_in must be true to allow access)
    print('admin page')
else:
    print('Not authorized')

if user=='admin' or logged_in: #allows access
    print('admin page')
else:
    print('Not authorized')

if not logged_in: #if not false(not logged-in),
    print("Please log in...")
else:
    print("Welcome!")

#is checks object identity ie if they have same id in memory
#the operator is check if objects have the same location in memory
a= [1,2,3]
b= [1,2,3]

print (a==b) #checks to values equality, hence true
print (a is b) #different memory locations hence evaluates to false

#their actual ids
print(id(a))
print (id(b))


#these conditions evaluate to false (jump else part of the code) in python everything else evaluatea to True
#False; None; Zero of all numeric types; any empty sequence eg '', (), []; empty mapping ie dict. {};

condition = False
if condition:
    print('evaluated to true')
else:
    print('evaluated to false')

condition = None
if condition:
    print ('evaluated to sumn')
else:
    print('evaluated to nun')

condition = 0
if condition:
    print('true one')
else:
    print('not one')

condition = {}
if condition:
    print('full dict.')
else:
    print('empty dict.')


##everything else evaluates to true eg.
condition ='123'
if condition:
    print('evaluated to true')
else:
    print('just not true')