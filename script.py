#Importing tkinter library into the script
from tkinter import *
import math
answerLabelGlobal = ""
answerLabelForSquareRoot = ""
#Creating the application's main window
root = Tk() 
root.config(background = "white")
root.title("Calculator App")
answerEntryLabel = StringVar()
answerFinalLabel = StringVar()
def changeAnswerLabel(entry):
    global answerLabelGlobal
    answerLabelGlobal = answerLabelGlobal + str(entry)
    answerLabelForSquareRoot = answerLabelGlobal
    answerEntryLabel.set(answerLabelGlobal)
def clearAnswerLabel():
    global answerLabelGlobal
    global answerLabelForSquareRoot
    answerLabelForSquareRoot = eval(answerLabelGlobal)
    answerLabelGlobal = ""
    answerEntryLabel.set(answerLabelGlobal)
def changeAnswerLabelToSquareRoot():
    global answerLabelGlobal
    global answerLabelForSquareRoot
    try:
        sqrta = math.sqrt(eval(str(answerLabelForSquareRoot)))
    except(ValueError,SyntaxError,TypeError, ZeroDivisionError):
        sqrta = math.sqrt(eval(str(answerLabelGlobal)))
    answerEntryLabel.set("")
    answerFinalLabel.set(sqrta)
def calc():
    global answerLabelGlobal
    try:
        eval(answerLabelGlobal)
        calc = str(eval(answerLabelGlobal))
        clearAnswerLabel()
        answerFinalLabel.set(calc)
    except(ValueError,SyntaxError,TypeError, ZeroDivisionError):
        clearAnswerLabel()
        answerFinalLabel.set("Error!")
def cls():
    global answerLabelGlobal
    global answerLabelForSquareRoot
    answerLabelGlobal = ""
    answerLabelForSquareRoot = ""
    answerEntryLabel.set("")
    answerFinalLabel.set("")
def createButton(txt,x,y):
    Button(root,font=('futura', 15, 'bold'),padx=16,pady=16, text = str(txt), command = lambda:changeAnswerLabel(txt),height = 2, width=9).grid(row = x , column = y, sticky = E)
Label(root,font=('futura', 30, 'bold'), textvariable = answerEntryLabel, justify = LEFT).grid(columnspan=4, ipadx=120)
Label(root,font=('futura', 30, 'bold'), textvariable = answerFinalLabel, justify = LEFT,height=2, width=7).grid(columnspan = 4 , ipadx=120)
btns = ['AC','sqrt','%','/','7','8','9','*','4','5','6','-','1','2','3','+']
k = 0
for i in range(3,7):
    for j in range(0,4):
        createButton(btns[k],i,j)
        k = k + 1
Button(root,font=('futura', 15, 'bold'),padx=16,pady=16, text = "sqrt", command = lambda:changeAnswerLabelToSquareRoot(),height=2, width=9).grid(row = 3 , column = 1, sticky = E)
Button(root,font=('futura', 15, 'bold'),padx=16,pady=16, text = "AC", command = lambda:cls(),height=2, width=9).grid(row = 3 , column = 0 , sticky = E)
Button(root,font=('futura', 15, 'bold'),padx=16,pady=16, text = "0", command = lambda:changeAnswerLabel(0),height=2, width=21).grid(row = 7 , column = 0 , columnspan=2 , sticky = E)
Button(root,font=('futura', 15, 'bold'),padx=16,pady=16, text = ".", command = lambda:changeAnswerLabel("."),height=2, width=9).grid(row = 7 , column = 2, sticky = E)
Button(root,font=('futura', 15, 'bold'),padx=16,pady=16, text = "=", command = lambda:calc(),height=2, width=9).grid(row = 7 , column = 3, sticky = E)
root.mainloop()