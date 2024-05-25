#imports run all the code from imported module
#to import it directly, module must be in same directory as target file
#print(find_index([1,2,3,4,5,6], 4))

import my_module as mm #note that we usually import modules as alias
courses = ["Art", "Architecture", "Biology", "Physics"]
#we can no longer call find_index directly
print(mm.find_index(courses, 'Math'))
print(mm.find_index(courses, 'Biology'))

#we can also import specifics from the module
#we can also give the specifics aliases
from my_module import find_index as fi, test as ts
print (ts)

#we can also import by 'from my_module import *'
#this is however discouraged as it does not allow us to see which specific modules are imported

#note that imports use sys to determine where to find modules
import sys
print(sys.path)
#for a module the pc cannot locate, we can append its path to the sys.path list
sys.path.append('/home/oukobrian/projects')
# we can also add this path above to the python path env. variable by editing the .bashrc file
print(sys.path)

#standard libary helps us use code without any other installs
import random
courses = ["Art", "Architecture", "Biology", "Physics"]
print(random.choice(courses)) #choice is a function of the random module

import math
print(math.sin(math.radians(90))) #radian and sin are functions of the math module

import datetime
import calendar

today = datetime.date.today()
print(f'The date today is {today}!')

#calendar functions differently and can help check if year is leap
print(calendar.isleap(2021))

import os#gives access to underlying os
import os
print(os.getcwd()) #present directory
print(os.__file__)#prints path of os directory
#dunders/magic methods (the dashes) customize how objects interact with python's built in mechanisms
