import time


start = input('Want to use the calculator? (Y for yes) - ')


#Function
if start == 'Y':
    #Define everything
    x1 = int(input('Please enter your first number - '))
    time.sleep(.5)
    x2 = int(input('Please enter your second number - '))
    time.sleep(.5)
    oper = input('Please select an operator, (+, -, /) - ')

    #Calculate
    if oper == '+':
        print(x1 + x2)
    elif oper == '-':
        print(x1 - x2)
    elif oper == '/':
        print(x1 / x2)
    
else:
    print("Error please make sure everything is correct")
    pass
time.sleep(1.8)
print('Thank you for using LiLBoyHatake\'s calculator! It is much appreciated. Please visit my website lilboyhatake.me')
time.sleep(2)
print('if you would like to use the calculator again, please restart the program')
time.sleep(3)
