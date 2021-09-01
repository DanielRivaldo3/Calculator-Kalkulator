#Calculator with GUI/ kalkulator dengan tampilan GUI

#Tkinter for interface / tkinter untuk tampilan interface
from tkinter import *
calculator_interface = Tk()
calculator_interface.title("Calculator")


calculator_fill = Entry(calculator_interface, width=50, borderwidth=5)
calculator_fill.grid(row = 0, column=0, columnspan=3, padx= 10,pady=10)

#function every operation (+,-,*,/,=,clear)
def button_click(number):
    current_number = calculator_fill.get()
    calculator_fill.delete( 0,END)
    calculator_fill.insert(0,str(current_number + str(number)))

def button_clear():
    calculator_fill.delete(0,END)

def button_add():
    first_number = calculator_fill.get()
    global f_number
    global math
    math = 'addition'
    f_number = int(first_number)
    calculator_fill.delete(0,END)
    
def button_subtract():
    first_number = calculator_fill.get()
    global f_number
    global math
    math = 'subtract'
    f_number = int(first_number)
    calculator_fill.delete(0,END)

def button_multiply():
    first_number = calculator_fill.get()
    global f_number
    global math
    math = 'multiply'
    f_number = int(first_number)
    calculator_fill.delete(0,END)

def button_divide():
    first_number = calculator_fill.get()
    global f_number
    global math
    math = 'divide'
    f_number = int(first_number)
    calculator_fill.delete(0,END)

def button_equal():
    second_number = calculator_fill.get()
    calculator_fill.delete(0,END) 
    if math == 'addition':
        calculator_fill.insert(0,f_number + int( second_number))
    if math == 'subtract':
        calculator_fill.insert(0,f_number - int( second_number))
    if math == 'multiply':
        calculator_fill.insert(0,f_number * int( second_number))
    if math == 'divide':
        calculator_fill.insert(0,f_number / int( second_number))

#Calculator Button Interface
button_1 = Button(calculator_interface, text='1', padx=40, pady=20, command= lambda: button_click(1))
button_2 = Button(calculator_interface, text='2', padx=40, pady=20,  command= lambda: button_click(2))
button_3 = Button(calculator_interface, text='3', padx=40, pady=20,  command= lambda: button_click(3))
button_4 = Button(calculator_interface, text='4', padx=40, pady=20,  command= lambda: button_click(4))
button_5 = Button(calculator_interface, text='5', padx=40, pady=20,  command= lambda: button_click(5))
button_6 = Button(calculator_interface, text='6', padx=40, pady=20,  command= lambda: button_click(6))
button_7 = Button(calculator_interface, text='7', padx=40, pady=20,  command= lambda: button_click(7))
button_8 = Button(calculator_interface, text='8', padx=40, pady=20,  command= lambda: button_click(8))
button_9 = Button(calculator_interface, text='9', padx=40, pady=20,  command= lambda: button_click(9))
button_0 = Button(calculator_interface, text='0', padx=40, pady=20,  command= lambda: button_click(0))

operator_add = Button(calculator_interface, text='+', padx=40, pady=20,  command= button_add)
operator_equal = Button(calculator_interface, text='=', padx=40, pady=20,  command= button_equal)
operator_clear = Button(calculator_interface, text='Clear', padx=80, pady=20,  command= button_clear)

operator_subtract = Button(calculator_interface, text='-', padx=40, pady=20,  command= button_subtract)
operator_multipy = Button(calculator_interface, text='*', padx=40, pady=20,  command= button_multiply)
operator_divide = Button(calculator_interface, text='/', padx=40, pady=20,  command= button_divide)

#put button on the screen
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_0.grid(row=4, column=0)
operator_subtract.grid(row=4, column=2)
operator_add.grid(row=4, column= 1)
operator_clear.grid(row = 6, column =1)
operator_equal.grid(row=5, column=2)
operator_multipy.grid(row=5, column= 1)
operator_divide.grid(row = 5, column =0)

calculator_interface.mainloop()