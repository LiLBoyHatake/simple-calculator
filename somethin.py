import time

#Just setting things up to make it a application
import tkinter as tk


start = input('Want to use the calculator? (Y for yes) - ')


#Application base

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()


    def create_widgets(self):
        #create first button
        self.simp_one = tk.Button(self)
        self.simp_one['text'] = ' 1 ' #Am I suppossed to make it a command?
        self.simp_one.pack(side='top')

        #Create second button
        self.simp_two = tk.Button(self)
        self.simp_two['text'] = ' 2 '
        self.simp_two.pack(side='top')

        #Third button
        self.simp_third = tk.Button(self)
        self.simp_third['text'] = ' 3 '
        self.simp_third.pack(side='top')

        #Fourth button
        self.simp_four = tk.Button(self)
        self.simp_four['text'] = ' 4 '
        self.simp_four.pack(side='top')

        #Fifth button
        self.simp_five = tk.Button(self)
        self.simp_five['text'] = ' 5 '
        self.simp_five.pack(side='top')

        #Sixth button
        self.simp_six = tk.Button(self)
        self.simp_six['text'] = ' 6 '
        self.simp_six.pack(side='top')

        #Seventh button
        self.simp_sev = tk.Button(self)
        self.simp_sev['text'] = ' 7 '
        self.simp_sev.pack(side='top')

        #Button eight
        self.simp_eight = tk.Button(self)
        self.simp_eight['text'] = ' 8 '
        self.simp_eight.pack(side='top')
        
        #Ninth button
        self.simp_ninth = tk.Button(self)
        self.simp_ninth['text'] = ' 9 '
        self.simp_ninth.pack(side='right')


        #Create the zero button
        self.simp_zed = tk.Button(self)
        self.simp_zed['text'] = ' 0 '
        self.simp_zed.pack(side='bottom')


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



root = tk.Tk()
app = Application(master=root)
app.mainloop()
