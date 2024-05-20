#lesson III
#Integers and floats

print (3+2)
print(3/2)
print (3//2) #floor division drops the dps
print (3**2)#exponent
print (3%2) #modulus, can be used to check even and odd numbers ie modulus of a number by 2
print (3+(3*2)) #obeys bodmas

#incrementing
num =3
num-=10
num *=10
num +=10
print (num)

#there's also built-in functions to work with numbers
print(abs(num))

print (round(3.75)) #rounding off
print (round(3.75,1)) #round off to one number

#comparisons - they return booleans
num_1=3
num_2=2
print(num_1==num_2) #compares if equal
print(num_1!=num_2)#if not equal 
print(num_1>=num_2)
print(num_1<num_2)

#how to handle numbers indicated as strings
num_1='100'
num_2='200'
num_1= int(num_1)#cast to an integer by wrapping with int function
num_2= int(num_2)
print (num_1+num_2)

#to use sum function, remember it expects and iteratable argument such as list/ tuple, hence we hold the variables in those datatypes
numbers = [num_1, num_2]
print(sum(numbers))