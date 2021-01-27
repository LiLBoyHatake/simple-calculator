from tkinter import *

expression = ""

def touch(num):
    global expression


    expression = expression + str(num)

    equation.set(expression)

def equalspress():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)

        expression = ""

    except:
        equation.set('Somethings wrong')
        expression = ""


def clear():
    global expression
    expression = ""
    equation.set("")


if __name__ == '__main__':
    gui = Tk()
    gui.configure(background='purple')
    gui.title('Hatake\'s Calculator')
    gui.geometry("270x150")

    equation = StringVar()
    expression_field = Entry(gui, textvariable=equation)
    expression_field.grid(columnspan=4, ipadx=70)
    equation.set('Enter your equation')


    #Buttons
    button1 = Button(gui, text = ' 1 ', fg='black', bg='red', 
        command=lambda: touch(1), height=1, width=7)
    button1.grid(row=2, column=0)
    button2 = Button(gui, text=' 2 ', fg='black', bg='red', 
                     command=lambda: touch(2), height=1, width=7) 
    button2.grid(row=2, column=1) 
  
    button3 = Button(gui, text=' 3 ', fg='black', bg='red', 
                     command=lambda: touch(3), height=1, width=7) 
    button3.grid(row=2, column=2) 
  
    button4 = Button(gui, text=' 4 ', fg='black', bg='red', 
                     command=lambda: touch(4), height=1, width=7) 
    button4.grid(row=3, column=0) 
  
    button5 = Button(gui, text=' 5 ', fg='black', bg='red', 
                     command=lambda: touch(5), height=1, width=7) 
    button5.grid(row=3, column=1) 
  
    button6 = Button(gui, text=' 6 ', fg='black', bg='red', 
                     command=lambda: touch(6), height=1, width=7) 
    button6.grid(row=3, column=2) 
  
    button7 = Button(gui, text=' 7 ', fg='black', bg='red', 
                     command=lambda: touch(7), height=1, width=7) 
    button7.grid(row=4, column=0) 
  
    button8 = Button(gui, text=' 8 ', fg='black', bg='red', 
                     command=lambda: touch(8), height=1, width=7) 
    button8.grid(row=4, column=1) 
  
    button9 = Button(gui, text=' 9 ', fg='black', bg='red', 
                     command=lambda: touch(9), height=1, width=7) 
    button9.grid(row=4, column=2) 
  
    button0 = Button(gui, text=' 0 ', fg='black', bg='red', 
                     command=lambda: touch(0), height=1, width=7) 
    button0.grid(row=5, column=0)

    plus = Button(gui, text = ' + ', fg='black', bg='red', 
        command=lambda: touch("+"), height=1, width=7)
    plus.grid(row=2, column=3)

    minus = Button(gui, text=' - ', fg='black', bg='red', 
        command=lambda: touch("-"), height=1, width=7)
    minus.grid(row=3, column=3)

    multi = Button(gui, text = 'X', fg='black', bg='red', 
        command=lambda: touch('*'), height=1, width=7)
    multi.grid(row=4, column=3)

    division = Button(gui, text = ' / ', fg='black', bg='red',
        command=lambda: touch('/'), height=1, width=7)
    division.grid(row=5, column=3)

    clear = Button(gui, text = ' CLEAR ', fg='black', bg='red', 
        command=clear, height=1, width=7)
    clear.grid(row=5, column='1')
    
    decimal = Button(gui, text = ' . ', fg='black', bg='red',  
        command=lambda: touch('.'), height=1, width=7)
    decimal.grid(row=6, column=0)

    equals = Button(gui, text = ' = ', fg='black', bg='red', 
        command=lambda: equalspress(), height=1, width=7)
    equals.grid(row=6, column=3)

    gui.mainloop()
