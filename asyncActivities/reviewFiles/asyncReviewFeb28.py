# 1. what is a function?
'A container for code instructions.'

'Function run code instructions only' 
'when its callled.'

# 2. Create a function that uses the input function
# and out the result

# step 1. create function definition
def message():
    response = input('please enter a message? ')
    print(response)

# step 2. "call" the function 
# message()

# 3. Create a function that compares if a user has enough
# money to buy a house

def canIAffordHouse():
    housePrice = 500000
    myBudget= int(input('how much do you have for this house? '))
    print(myBudget> housePrice)

canIAffordHouse()