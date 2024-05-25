#the pass keyword
def hello_func(): #an empty function mass have pass keyword to not throw errors
    pass
print(hello_func())

#functions help keep the code DRY
def hello_func():
    print('Hello')
hello_func()

#functions can also have an output defined as return but not necessarily printed
def hello_func():
    return 'Hello Function'
#printing the function output then displays the string above
print(hello_func())

#fundamentally for functions, we need to understand the input and output, rather than focus on what's going on in the black box
#an example is that the len function is a blackbox
print(len(hello_func()))
print(len('Test'))

#as such we ought to treat functions' return value as a datatype, allowing us to chain functions
print(hello_func().upper())

#passing args to functions
#note that greeting variable only has scope within the function
def hello_func(greeting):
    #return f'{greeting} Function' does same thing as line below:
    return '{} Function.'.format(greeting)
print(hello_func('Hi'))
#in the example above greeting is a required arg as it does not have a default value

# below we specify default value for name hence, feeding a name arg to the function is not a must!
def hello_func(greeting, name='You'):
    return f'{greeting}, {name}'
print(hello_func('Hello'))


def students_info(*args, **kwargs):
    print(args)
    print(kwargs)
students_info('12', 237123, name = 'Brian', age = '24', sport ='b-ball')
#the output here is ('12', 237123) and {'name': 'Brian', 'age': '24', 'sport': 'b-ball'}
#it outputs the args as a tuple, and kwargs as a dict.

#reverse-engineering the above
def students_info(*args, **kwargs):
    print(args)
    print(kwargs)
p_info = ['12', 237123]
s_info = {'name':'Brian', 'age': 24, 'sport':'b-ball'}
#students_info(p_info,s_info) -creates a tuple with the list and dict, as elements without unpacking them
students_info(*p_info, **s_info)


#example -checking whether year is leap or not
month_days=[0,31,28,31,30,31,30,31,31,30, 31,30,31]

def is_leap(year):
    """returns true or false to check for leap year"""
    return year%4 ==0 and (year%100 !=0 or year%400==0)
print(is_leap(2024))

def days_in_month(year, month):
    """returns no of days in that month, that year"""
    if not 1<=month<=12:
        return 'Invalid month'
    if month ==2 and is_leap(year):
        return 29
    return(month_days[month])
print(days_in_month(2023,2))