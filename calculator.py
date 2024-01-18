from tkinter import *

root = Tk()
root.title("Calculator")

num = Entry(root, width=35, borderwidth=5)
num.grid(row=0, column=0, columnspan=3, padx=10,pady=10)


def button_add():
    global operator, first_num
    first_num = int(num.get())
    num.delete(0, END)
    operator = '+'

def button_sub():
    global operator, first_num
    first_num = int(num.get())
    num.delete(0, END)
    operator = '-'

def button_mul():
    global operator, first_num
    first_num = int(num.get())
    num.delete(0, END)
    operator = '*'

def button_div():
    global operator, first_num
    first_num = int(num.get())
    num.delete(0, END)
    operator = '/'



def button_click(number):
    current = num.get()  
    num.delete(0, END) #This delete the number which inside the input box
    num.insert(0, str(current) + str(number))

def button_clear():
    num.delete(0, END)

def button_equal():
    global operator, first_num, second_num
    second_num = int(num.get())
    num.delete(0, END)

    if operator == '+':
        result = first_num + second_num
    elif operator == '-':
        result = first_num - second_num
    elif operator == '*':
        result = first_num * second_num
    elif operator == '/':
        if second_num != 0:  # Check for division by zero
            result = first_num / second_num
        else:
            result = "Error: Division by zero"
    
    num.insert(0, result)

# Button numbering

button1 = Button(root, text="1", padx=40, pady=20, command=lambda : button_click(1))
button2 = Button(root, text="2", padx=40, pady=20, command=lambda : button_click(2))
button3 = Button(root, text="3", padx=40, pady=20, command=lambda : button_click(3))
button4 = Button(root, text="4", padx=40, pady=20, command=lambda : button_click(4))
button5 = Button(root, text="5", padx=40, pady=20, command=lambda : button_click(5))
button6 = Button(root, text="6", padx=40, pady=20, command=lambda : button_click(6))
button7 = Button(root, text="7", padx=40, pady=20, command=lambda : button_click(7))
button8 = Button(root, text="8", padx=40, pady=20, command=lambda : button_click(8))
button9 = Button(root, text="9", padx=40, pady=20, command=lambda : button_click(9))
button0 = Button(root, text="0", padx=40, pady=20, command=lambda : button_click(0))
button_add = Button(root, text="+", padx=39, pady=20, command=button_add)
button_sub = Button(root, text="-", padx=39, pady=20, command=button_sub)
button_mul = Button(root, text="*", padx=38, pady=20, command=button_mul)
button_div = Button(root, text="/", padx=38, pady=20, command=button_div)
button_equal = Button(root, text="=", padx=80, pady=20, command=button_equal)
button_clear = Button(root, text="C", padx=80, pady=20, command=button_clear)


# Arraning button on widget


button1.grid(row=3, column=0)
button2.grid(row=3, column=1)
button3.grid(row=3, column=2)

button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)

button7.grid(row=1, column=0)
button8.grid(row=1, column=1)
button9.grid(row=1, column=2)

button0.grid(row=4, column=0)
button_clear.grid(row=4, column=1, columnspan=2)
button_add.grid(row=5, column=0)
button_equal.grid(row=5, column=1, columnspan=2)
button_sub.grid(row=6, column=0)
button_mul.grid(row=6, column=1)
button_div.grid(row=6, column=2)



root.mainloop()