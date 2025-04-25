def depositMoney(money):
    balance= 0 # step 1: get current balance
    newBalance= money + balance # step2 : add new money to balance    
    print('your new balance is : ' + str(newBalance)) # step3: print out balance

depositMoney(100)

# def withdraw():

# conditional statements

# apples= 10
# if apples > 3:
#     print("share your apples")
# else:
#     print('you dont have enough to share.')

# rollercoaster 
# banking

youtubePayout_1000 = 100
youtubePayout_100 = 10

payRate =0.18

#monthly
views= 1001

if views > youtubePayout_100:
    print("congrats! heres your 500 dollars")
elif views > youtubePayout_100: 
    print("congrats! heres you 100 dollars")
else:
    print("sorry, your channel isnt there yet.")