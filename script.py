#Importing tkinter library into the script
from tkinter import *
#Creating the application's main window
root = Tk() 
root.config(background = "white")
root.wm_iconbitmap("/icon.ico")
root.title("Calculator App")
answerLabel = StringVar()
answerLabelGlobal = ""
ans = StringVar()
def changeAnswerLabel(entry):
    global answerLabelGlobal
    answerLabelGlobal = answerLabelGlobal + str(entry)
    answerLabel.set(answerLabelGlobal)
def clearAnswerLabel():
    global answerLabelGlobal
    answerLabelGlobal = ""
    answerLabel.set(answerLabelGlobal)
def calc():
    global answerLabelGlobal
    try:
        eval(answerLabelGlobal)
        calc = str(eval(answerLabelGlobal))
        clearAnswerLabel()
        ans.set(calc)
    except(ValueError,SyntaxError,TypeError, ZeroDivisionError):
        clearAnswerLabel()
        ans.set("Error!")
def cls():
    global answerLabelGlobal
    answerLabel.set("")
    ans.set("")
def createButton(txt,x,y):
    bt = Button(root,font=('aria', 15, 'bold'),padx=16,pady=16, text = str(txt), command = lambda:changeAnswerLabel(txt),height=2, width=7).grid(row = x , column = y, sticky = E)
Label(root,font=('aria', 30, 'bold'), textvariable = answerLabel, justify = LEFT).grid(columnspan=4, ipadx=70)
Label(root,font=('aria', 30, 'bold'), textvariable = ans, justify = LEFT,height=2, width=7).grid(columnspan=4, ipadx=70)
btns = ['7','8','9','+','4','5','6','-','3','2','1','*','.','0','','/']
k = 0
for i in range(3,7):
    for j in range(0,4):
        createButton(btns[k],i,j)
        k = k + 1
bt = Button(root,font=('aria', 15, 'bold'),padx=16,pady=16, text = "=", command = lambda:calc(),height=2, width=7).grid(row = 6 , column = 2, sticky = E)
root.mainloop()