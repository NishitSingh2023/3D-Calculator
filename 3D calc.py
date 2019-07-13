import sys
from tkinter import *



def btnClick(numbers):
    global operator
    operator = operator+ str(numbers)
    text_input.set(operator)


def btnClearDisplay():
    global operator
    operator=""
    text_input.set("")


def btnequalsto():
    global operator
    sumup = str(eval(operator))
    text_input.set(sumup)
    operator = ""


cal = Tk()
cal.title("CALCULATOR v0.1.3")
operator=""
text_input=StringVar()
 
txtdisplay= Entry(cal , font=('arial', 20, 'bold'),textvariable=text_input, bd=40, insertwidth=5, bg='powder blue', justify='right').grid(columnspan=4)




#=====================================================================================================


cal.mainloop()
