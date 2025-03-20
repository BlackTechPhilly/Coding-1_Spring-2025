
# You have been hired as an engineer to develop a 
# passcode system for the companies entrance system. 
# The company would like to have a system in place 
# that will check the passcode entered by users at 
# the door, and if the code matches the code in the 
# program, the user may enter, but if it does not
#  match, their credentials will be rejected. The 
# client has provided you with the passcode that 
# users must use to enter.

# Passcode that must be used: “get_this_money”

def doorEntranceCode(userPin):
    pinCode = 12345
    if userPin == pinCode:
        print("access granted. Door is unlocked")
    else:
        print("access denied, Door will remain locked")

doorEntranceCode(12345)




# You have been hired as an 
# engineer to develop a quiz program 
# for a school. The client has specified 
# that the quiz should have two questions,
# which will be provided below. When 
# the quiz program starts the user 
# taking the quiz must enter their 
# answers. When they are finished 
# the quiz programs needs to evaluate
# oth answers. If both answers are 
# true, the person taking the quiz has 
# passed, but if the person taking the 
# quiz misses even just one question, 
# they fail. 

# Quiz questions:

# What is the capital of Pennsylvania ?
# How many national parks are in Pennsylvania ? 

# Hint:
# You will need to use one of the logical operators. 
