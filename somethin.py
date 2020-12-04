import time


#Function
def equation():
    #Define everything
    x1 = int(input('Please enter your first number - '))
    time.sleep(.5)
    x2 = int(input('Please enter your second number - '))
    time.sleep(.5)
    oper = input('Please select an operator, (+, -) - ')

    #Calculate
    if oper == '+':
        print(x1 + x2)
    elif oper == '-':
        print(x1 - x2)

equation()