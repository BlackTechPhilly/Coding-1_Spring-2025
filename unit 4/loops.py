# While Loops are a type of loop that will
# keep the code running so long as the 
# looping condition is true. 

endOfSchool ='April 2nd'

#while endOfSchool !='May 31st':
 #   print('school is in session.')

dismissalHour = 3
while dismissalHour != 3:
    print('school is in session.')

# 1 kosher menu
# 2 vegitarian menu
# 3 allergy menu
# 4 lactose intolerant menu
# 5 nothing  menu

# foodOrder = 1

# while foodOrder == 1:
#     print('You will get the kosher option')


# Class activity # 1
# Create a simple count-down timer using a while loop
# Your code should count down from 10 and stop at zero.
# - HINT: you will need to use either assignment or an arithmatic operator
# to make the numbers count down. 


i = 10
while i >= 0:
    print(i)
    i-=1

# Class activity # 2
# Create a function that will take a number in as a parameter
# and continue to multiply a number passed by 2.  
# The loop will stop when the number reaches 40. 




# Python loops are a construct 
# for repeating blocks of code.

# While Loop: so long as a condition is true, 
# the loop will continue to run

# Create a function with a while loop that will 
# print out a message, so long as we enter the 
# correct number code.  

def codeToSeeMsg():
    code = input("Please enter code to see message: ")
    while code != '123':
        print('locked out')
    else:
        print('Have a great day!')        

#codeToSeeMsg()

# Class activity # 3
# Create a guess-the-word function. Your function 
# should printout a hint of what the word is and 
# then ask the user to enter the correct word. 
# if the user enters the wrong word, the game will 
# tell the user that it
# is incorrect and guess again. If the user gets 
# the answer correct, the
# function will tell the user that the answer 
# is correct and the game 
# loop will end. 



    # function should print out a hint as to what the word 
    # is function should allow the user to enter a word
    # function should check if the word is correct or not
    # if the word is not correct, ask the user to try again
    # in a loop
    # if the word is correct, end the loop
def wordGuessingGame():
    print('guess the word:')
    print('circular object on a car. Comes in 2 pairs')
    userGuess = input("What is your guess? ")
    while userGuess != 'wheel':
        print('Try again')
        userGuess = input("What is your guess? ")
    else: 
        print("Correct! ")

# wordGuessingGame()

# For Loops - are a type of loop that runs  through 
# specific conditions on a list of data. 

# List - a collection data type for storing
# different types of data.

bobby_Coding = ['Bobby', 16, True, 96.6]
david_Coding =['David', 15, False, 85.9]

blPowerSchool_Class = [bobby_Coding, david_Coding]

class student:
    name:''
    grade:3
    age: 12
    classes:[]
    
class BLHS:
    grade_9: [student]
    grade_10: []
    grade_11:[ ]




# a list is identified by square brackets

# studentQuiz() = round brackets means it is function
# studentQuiz[] = square brackets means it is a list

studentQuiz = [90, 100, 70, 85, 65, 70, 82, 90]

# We can access values in a list using the list index 
#system. 

# When accessing a list, the first piece of data in the list
# is always identified as being in position zero (0).
# Lists always start their count from zero. 

print(studentQuiz[2])

studentQuiz = [90, 100, 70, 85, 65, 70, 82, 90]

# basic structure (sytnax) for creating a for loop

for x in studentQuiz:
  print(x + 5)






