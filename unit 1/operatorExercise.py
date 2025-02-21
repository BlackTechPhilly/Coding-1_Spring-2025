# 1. Which python operator would you use if you were 
# developing a shopping application and wanted to get the 
# sum of all the items in a person's shopping cart?

# Arithmatic Operator
# getting the total checkout amount for items in a cart

bookbag= 20.00
pens= 10.00
notebooks= 10.00
coffeeMug= 20.00

total = bookbag + pens + notebooks + coffeeMug
print(total)

# 2. Which python operator would you use if you wanted to 
# determine if a user is old enough to 
# purchase a video game?

# Comparison operator
# checking if someone is old enouggh to buy game
age = 17
ageToBuy = 17

print(age > ageToBuy)

# 3. Boys Latin has asked you to develop a program to track 
# students who are eligible to attend the spring college 
# tour field trip. The school would like to the program 
# check each student’s ID and do the following: check if 
# the student has taken the coding 1 programming class, 
# and the student’s grade level. If the student has taken 
# the coding class and are is in 12th grade, they may go on 
# the trip. If the student’s ID does not meet this condition, 
# they cannot attend the trip. 

# logical operator
# we need to check if the student is in 12 AND has taken
# coding close.

studentGrade = 12
studentHasTakenCode = True

print(studentGrade == 12 and studentHasTakenCode == True)