#conditionals - if, elif, else
#loop statements - for
nums = [1,2,3,4,5,6,7]
for num in nums: #num takes on the value of each element in nums lits one by one, in order
    print(num)

#break and continue keywords help when working with loops
#break exits loop immediately a certain condition is satisfied
#continue skips current iteration of loop and the code after the continue statement is not implemented for current iteration of the loop

#break
#this code block evaluates the nums one by one, printing out until 3 is found
nums = [1,2,3,4,5]
for num in nums:
    if num == 3:
        print('found it') #this print is only executed once 3 has been found, by then 1&2 are printed out by the print(num) below
        break
    print(num)

#continue
for num in nums:
    if num==3:
        print('found three')
        continue
    print(num)

#remember we could use else alongside for loop, but would only execute after the for loop runs entirely without break or continue
nums = [1,2,3,4,6]
for num in nums:
    if num ==5:
        print('found it!')
        continue
    print(num)
else:
    print("6 was not found!")

#an illustration of the above is the prime number check
#without a break statement it prints out all numbers that can't div. 29
number =53
for i in range(2, int(number**0.5 + 1)):
    if number%i==0:
        print(f'{number} is not prime as it is divisible by {i}')
        break #exit the loop if a divisor is found
else:
    print(f'{number} is a prime number as it is not div. by any number from 2 to {int(number**0.5+1)}')

#loop within a loop
#code below loops abc for each num one by one- so 1a,1b,1c,2a,2b,2c
nums = [1,2,3,4,5]
for num in nums:
    for letter in 'abc':
        print(num,letter)

#to avoid infinite loops we could use range()
for i in range (10): # starts at 0, and loops to 9
    print (i)
for i in range (1,10):# starts at 1, but still doesn't print the last value
    print(i)

#while loop
x=0
while x<10:
    print(x) #prints all values of x until x=10
    x+=2 #loop would be infinite without this statement

#we could also get out of the loop using break
x=0
while x<10:
    if x==5:
        break
    print("count", x)
    x+=1
#example 2 - infinite loop that doesn't end till it see a certain value
x=0
while True:
    print('count', x)
    x+=1
    if x==9: #infinite loop runs until it breaks when x=9
        break