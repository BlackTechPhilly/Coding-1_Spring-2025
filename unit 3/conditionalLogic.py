
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




