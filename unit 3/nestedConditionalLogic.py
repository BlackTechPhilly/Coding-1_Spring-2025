# What is a conditional statement?
# A conditional statement is a type of construct
# that checks for a specific condition and will output
# a specific result. If the condition is not met,
# it will return a different result.

# We use the IF/ELSE keywords to create conditions.

def schoolHours(hour, meridiem):
    print('connected')
    if meridiem == 'am':
        print('it\'s the AM')
        if 7 < hour < 12:
            print('school is IN session')
        else:
            print('school is NOT in session')
    elif meridiem == 'pm':
        print('it\'s the PM')
        if 1 <= hour <= 3:
            print('school is IN session')
        else:
            print('school is NOT in session')
    else:
        print('Invalid time format. Use "am" or "pm".')

# Example call
# schoolHours(7, 'am')  # This should print "school is NOT in session"



# choose one of the scenarios to create a function
# thats uses a conditional statement to solve the issue

# 1. Ticket price for amusement park by age

# 2. School letter grade by score

# 3. Email recovery function for missing email or password

def letterGradeByScore(score):
    if score >= 90 and score <= 100:
        print('Your score is a A.')
    elif score >= 80 and score <= 89:
        print('Your score is a B.')
    elif score >= 70 and score <= 79:
        print('Your score is an C.')
    elif score >= 60 and score <= 69:
        print('Your score is an D')   
    elif score <= 59:
        print('Your score is a F.')
    else:
        print('Cant process this grade. please check your code.')

letterGradeByScore(78)
