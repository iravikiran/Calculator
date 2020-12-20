#
#               Python-Tkinter - Calculator v1.0
#
#   A Simple Python based GUI Calculator Application written
#   with Tkinter.
#       This code performs following functions:
#           ->   Addation of Numbers.
#           ->   Subtraction of Numbers.
#           ->   Multiplication of Numbers.
#           ->   Division of Numbers.
#           ->	 Power of a Number.
#			->   Square of a Number.
#			->   Percentage of a Number.
#
#   Feel free to add more features to the code and create a PR
#   i'm working on adding more features on the next releases.
#
#                   Author : Ravi Kiran
#                   GitHub : iravikiran
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

#importing tkinter.
from tkinter import *

# A container for TK.
root = Tk()

# Title of the Application.
root.title("Calculator")

root.geometry('395x370')

# User Input field, 40px width set as default.
e = Entry(root, width=45, borderwidth=5)

# Grid based orintation of the application, produces 4 columns.
e.grid(row=0, column=0, columnspan=4, padx=10, pady=10)


# Gets the input number from the User.
def button_click(num):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(num))


# Clears the Input screen of the Entered Number.
def button_clear():
    e.delete(0, END)


# Checks for the Math operand and then performs the arthematic operation.
def button_equal():
	if math == "square":
		e.insert(0, f_num * f_num)
	elif math == "percent":
		e.insert(0, f_num / 100)
	else:
		sec = e.get()
		e.delete(0, END)
		if math == "addition":
		    e.insert(0, f_num + int(sec))
		if math == "subtract":
		    e.insert(0, f_num - int(sec))
		if math == "multiply":
		    e.insert(0, f_num * int(sec))
		if math == "divide":
		    e.insert(0, f_num / int(sec))
		if math == "power":
			e.insert(0, f_num ** int(sec))


# Function to Add and capture the first number.
def button_add():
    first = e.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first)
    e.delete(0, END)


# Function to Sub and capture the first number.
def button_sub():
    first = e.get()
    global f_num
    global math
    math = "subtract"
    f_num = int(first)
    e.delete(0, END)


# Function to Multiply and capture the first number.
def button_mul():
    first = e.get()
    global f_num
    global math
    math = "multiply"
    f_num = int(first)
    e.delete(0, END)


# Function to Divide and capture the first number.
def button_div():
    first = e.get()
    global f_num
    global math
    math = "divide"
    f_num = int(first)
    e.delete(0, END)


# Function to Power and capture the first number.
def button_pow():
    first = e.get()
    global f_num
    global math
    math = "power"
    f_num = int(first)
    e.delete(0, END)


# Function to Squaring and capture the first number.
def button_sqr():
    first = e.get()
    global f_num
    global math
    math = "square"
    f_num = int(first)
    e.delete(0, END)


# Function to Percentage and capture the first number.
def button_pst():
    first = e.get()
    global f_num
    global math
    math = "percent"
    f_num = int(first)
    e.delete(0, END)


# Buttons declarations, from numbers 0 to 9..
button1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
button2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
button3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
button4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
button5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
button6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
button7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
button8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
button9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
button0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))

# Buttons declaration for add, mul, sub, equal, div, clear, percent, power of, & square.
button_add = Button(root, text="+", padx=39, pady=20, command=button_add, bg="#ff9e00", fg="#fbfbfb")
button_equal = Button(root, text="=", padx=39, pady=51, command=button_equal, bg="#ffe95a")
button_clear = Button(root, text="C", padx=39, pady=20, command=button_clear, bg="#ff9e00", fg="#fbfbfb")
button_sub = Button(root, text="—", padx=38, pady=20, command=button_sub, bg="#ff9e00", fg="#fbfbfb")
button_mul = Button(root, text="X", padx=39, pady=20, command=button_mul, bg="#ff9e00", fg="#fbfbfb")
button_div = Button(root, text="/", padx=42, pady=20, command=button_div, bg="#ff9e00", fg="#fbfbfb")
button_pow = Button(root, text="Pow", padx=30, pady=20, command=button_pow, bg="#ff9e00", fg="#fbfbfb")
button_sqr = Button(root, text="x^2", padx=31, pady=20, command=button_sqr, bg="#ff9e00", fg="#fbfbfb")
button_pst = Button(root, text="%", padx=38, pady=20, command=button_pst, bg="#ff9e00", fg="#fbfbfb")

# Packing up the buttons 1, 2, 3, & + on Row3.
button1.grid(row=3, column=0)
button2.grid(row=3, column=1)
button3.grid(row=3, column=2)
button_add.grid(row=3, column=3)

# Packing up the buttons  4, 5, 6 & * on Row2.
button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)
button_mul.grid(row=2, column=3)

# Packing up the buttons for 7, 8, 9 & / on Row1.
button7.grid(row=1, column=0)
button8.grid(row=1, column=1)
button9.grid(row=1, column=2)
button_div.grid(row=1, column=3)

# Packing up the buttons for 0, clear, -, equals on Row4.
button0.grid(row=4, column=1)
button_clear.grid(row=4, column=0)
button_sub.grid(row=4, column=2)
button_equal.grid(row=4, column=3, rowspan=2)

# Packing up the buttons for Power, Square, & Percentage on Row5. 
button_pow.grid(row=5, column=0)
button_sqr.grid(row=5, column=1)
button_pst.grid(row=5, column=2)

# Loop GUI. 
root.mainloop()