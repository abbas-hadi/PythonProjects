#lab 6 by Hadi A
print ("lab 6 - dealing with numbers")

#grab some inputs from user
firstNum = float(input('Enter num 1'))
secondNum = float(input('Enter num 2'))
thirdNum = float(input('Enter num 3'))
fourthNum = float(input('Enter num 4'))
fifthNum = float(input('Enter num 5'))

#let's do some calculating
totalNum = firstNum + secondNum + thirdNum + fourthNum + fifthNum
avgNum = totalNum / 5

print ('\n')
print ('The sum is', totalNum)
print ('\n')
print ('The average is' , avgNum) 

























#lab 7 by Hadi A
print ("lab 7 - calculator")

#grab some inputs from user
firstNum = float(input('Enter num 1'))
secondNum = float(input('Enter num 2'))
doWhat = input('a,s,d,m:')

#logic to figure out what to do
if doWhat=='a':
    totalNum = firstNum + secondNum
    sayThis = str(firstNum) + " plus " + str(secondNum) + " is " + str(totalNum)

if doWhat=='s':
    totalNum = firstNum - secondNum
    sayThis = str(firstNum) + " minus " + str(secondNum) + " is " + str(totalNum)

if doWhat=='d':
    totalNum = firstNum / secondNum
    sayThis = str(firstNum) + " divide " + str(secondNum) + " is " + str(totalNum)

if doWhat=='m':
    totalNum = firstNum * secondNum
    sayThis = str(firstNum) + " times " + str(secondNum) + " is " + str(totalNum)

print ('\n')
print (sayThis) 
















#lab 8 by Hadi A
print ("Lab 8 - Minimum Numbers")
print ("Hadi")
print ("Comsci 101\n")

#Capture Variables with Input Prompts Code Block
firstNum = float(input( 'Enter your first number =' ))
secondNum = float(input( 'Enter your second number =' ))
thirdNum = float(input( 'Enter your third number =' ))
fourthNum = float(input( 'Enter your fourth number =' ))
fifthNum = float(input( 'Enter your fifth number =' ))


#Assign Min Value
minNum = firstNum

#Calculate Output determine Min
if secondNum<minNum:
    minNum = secondNum
if thirdNum<minNum:
    minNum = thirdNum
if fourthNum<minNum:
    minNum = fourthNum
if fifthNum<minNum:
    minNum = fifthNum
    
#Output Code Block
print ('\n')
print ('The numbers you entered are:' , firstNum, secondNum, thirdNum, fourthNum, fifthNum, '\n', 'Your lowest number is', minNum)













#lab 9 by Hadi A
print ("Lab 9 - Swap Name")
print ("Hadi Abbas")
print ("Comsci 101\n")

firstName = input( 'Enter your first name =>' )
secondName = input( 'Enter your second name =>' )
thirdName = input( 'Enter your third name =>' )
fourthName = input( 'Enter your fourth name =>' )
fifthName = input( 'Enter your fifth name =>' )

# Sort First Name
if firstName > secondName:
    firstName, secondName = secondName, firstName
if firstName > thirdName:
    firstName, thirdName = thirdName, firstName
if firstName > fourthName:
    firstName, fourthName = fourthName, firstName
if firstName > fifthName:
    firstName, fifthName = fifthName, firstName
    
# Sort Second Name
if secondName > thirdName:
    secondName, thirdName = thirdName, secondName
if secondName > fourthName:
    secondName, fourthName = fourthName, secondName
if secondName > fifthName:
    secondName, fifthName = fifthName, secondName
    
#Sort Third Name
if thirdName > fourthName:
    thirdName, fourthName = fourthName, thirdName
if thirdName > fifthName:
    thirdName, fifthName = fifthName, thirdName
    
#Sort Fourth Name
if fourthName > fifthName:
    fourthName, fifthName = fifthName, fourthName
    
#Output Code Block
print ('\n')
print (firstName, '\n')
print (secondName, '\n')
print (thirdName, '\n')
print (fourthName, '\n')
print (fifthName, '\n')








































#lab 10 by Hadi A
print ("Lab 10 - Quiz")
print ("Hadi Abbas")
print ("Comsci 101\n")

#Capture Variables with Input Prompts Code Block

q1answer = float(input('Q1 - How many bits are in 1 kilobyte? => '))
q2answer = input ("Q2 - What is Amazon's new tablet called? =? ")
q3answer = input('Q3 - Steve Jobs was the CEO of which company? => ')

#Output Code Block
print ('\n')

if (q1answer == 1024):
    print('Q1 - Correct! It is => ', q1answer)
else:
    print('Q1 - Sorry, it is 1024')
    
if (q2answer.lower ( ) == "kindle fire"):
     print('Q2 - Correct! It is => ', q2answer)
else:
    print('Q2 - Sorry, it is the Kindle Fire')
if (q3answer.lower ( ) == "apple"):
    print('Q3 - Correct! It is => ', q3answer)
else:
    print('Q3 - Sorry, it is Apple!')
