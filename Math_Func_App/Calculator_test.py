from tkinter import *
calc=Tk()
calc.title("Calculator App")
calc.geometry('350x200')
#numbers=["nine","eight","seven","six","five,","four","three","two","one"]
def click():
    equation=Label(calc,text=x)
    equation.grid(column=3,row=3)
y=z=0
for x in range(9):
    numbers=Button(calc,text=9-x,font=("Arial",20),command=click)
    numbers.grid(column=y,row=z)
    y=y+1
    if y==3:
        y=0
        z=z+1

calc.mainloop()