# create a clone function where data 
# that is passed in will be copied 
# and then printed out

def cloneMachine(name):
    print('this is the original: '+ name)
    print('this is the clone: '+ name)

cloneMachine('Ian')

def cloneMachine2(number):
    result= str(number)
    print('original number is: '+  result)
    print(2 * number)

cloneMachine2(4)


def email(emailAddress, password):
    captcha ='aseoep'    
    if emailAddress and password:
        print('great you have access')
        if captcha == captcha:
            print('2-step complete')
    else:
        print('you cannot enter')

email('ian','eiofeiwoj')