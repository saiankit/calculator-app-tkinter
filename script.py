#Importing tkinter library for GUI and math library for square root function.
from tkinter import *
import math

###Global Variables###
answerVariableGlobal = ""
answerLabelForSquareRoot = ""

root = Tk() #Creating the application's main window
root.title("Calculator App") #Title for the application's main window

#Label - Entry Label where the expressions being clicked will be shown
answerEntryLabel = StringVar()
Label(root,font=('futura', 25, 'bold'), textvariable = answerEntryLabel, justify = LEFT,height=2, width=7).grid(columnspan=4, ipadx=120)
#Label - Answer Label where the final answer would be shown after evaluating the expression entered.
answerFinalLabel = StringVar()
Label(root,font=('futura', 25, 'bold'), textvariable = answerFinalLabel, justify = LEFT,height=2, width=7).grid(columnspan = 4 , ipadx=120)
def changeAnswerEntryLabel(entry):
    #changeAnswerEntryLabel - adds the entry on click on a particular button 
    #to the answerVariableGlobal and also appends the entry to the answerEntryLabel
    global answerVariableGlobal
    global answerLabelForSquareRoot
    answerVariableGlobal = answerVariableGlobal + str(entry) #Adding entry on click of button to the answerVariableGlobal
    answerLabelForSquareRoot = answerVariableGlobal #Also modifying the answerVariableGlobal to the answerLabelForSquareRoot for future use  
    answerEntryLabel.set(answerVariableGlobal)#Showing each entry onto the answerEntryLabel of calculator by appending each entry to the previously entered values before evaluation or allClear
def clearAnswerEntryLabel():
    #clears the answerEntryLabel and also clears answerVariableGlobal
    global answerVariableGlobal
    global answerLabelForSquareRoot
    answerLabelForSquareRoot = answerVariableGlobal
    answerVariableGlobal = ""
    answerEntryLabel.set(answerVariableGlobal)
def evaluateSquareRoot():
    #evaluateSquareRoot - evaluates the expression present in
    #the answerLabelForSquareRoot for square root of that value and 
    #returns that value to answerFinalLabel
    global answerVariableGlobal
    global answerLabelForSquareRoot
    try:
        sqrtAnswer = math.sqrt(eval(str(answerLabelForSquareRoot)))
        clearAnswerEntryLabel()
        answerFinalLabel.set(sqrtAnswer)
    except(ValueError,SyntaxError,TypeError, ZeroDivisionError):
        try:
            sqrtAnswer = math.sqrt(eval(str(answerVariableGlobal)))
            clearAnswerEntryLabel()
            answerFinalLabel.set(sqrtAnswer)
        except(ValueError,SyntaxError,TypeError, ZeroDivisionError):#ErrorHandling
            clearAnswerEntryLabel()
            answerFinalLabel.set("Error!")
def evaluateAnswer():
    #evaluateAnswer - evaluates the expression present in
    #the answerVariableGlobal and returns the value to answerFinalLabel
    #also clearing the answerEntryLabel using clearAnswerEntryLabel()
    global answerVariableGlobal
    try:
        eval(answerVariableGlobal)
        evaluatedValueAnswerLabelGlobal = str(eval(answerVariableGlobal))
        clearAnswerEntryLabel()
        answerFinalLabel.set(evaluatedValueAnswerLabelGlobal)
    except(ValueError,SyntaxError,TypeError, ZeroDivisionError):#ErrorHandling
        clearAnswerEntryLabel()
        answerFinalLabel.set("Error!")
def allClear():
    #All Clear (AC) - clears out the current data,
    #and prepares the calculator to start a new calculation
    global answerVariableGlobal
    global answerLabelForSquareRoot
    answerVariableGlobal = ""
    answerLabelForSquareRoot = ""
    answerEntryLabel.set("")
    answerFinalLabel.set("")
def createButton(txt,x,y):#Function used to create a button.
    Button(root,font=('futura', 15, 'bold'),padx=16,pady=16,text = str(txt), command = lambda:changeAnswerEntryLabel(txt),height = 2, width=9).grid(row = x , column = y, sticky = E)

###Buttons###
#buttons list stores the button values to be incoroporated in the calculator for first 4 rows
buttons = ['AC','sqrt','%','/','7','8','9','*','4','5','6','-','1','2','3','+']
buttonsListTraversalCounter = 0 #buttonsListTraversalCounter is used to traverse across the buttons list  
for i in range(3,7):
    for j in range(0,4):
        createButton(buttons[buttonsListTraversalCounter],i,j)
        buttonsListTraversalCounter = buttonsListTraversalCounter + 1
Button(root,font=('futura', 15, 'bold'),padx=16,pady=16, text = "sqrt", command = lambda:evaluateSquareRoot(),height=2, width=9).grid(row = 3 , column = 1, sticky = E)#Button for SquareRoot
Button(root,font=('futura', 15, 'bold'),padx=16,pady=16, text = "AC", command = lambda:allClear(),height=2, width=9).grid(row = 3 , column = 0 , sticky = E)#Button for AC button - clear the workspace
Button(root,font=('futura', 15, 'bold'),padx=16,pady=16, text = "0", command = lambda:changeAnswerEntryLabel(0),height=2, width=21).grid(row = 7 , column = 0 , columnspan=2 , sticky = E)#Button for value 0
Button(root,font=('futura', 15, 'bold'),padx=16,pady=16, text = ".", command = lambda:changeAnswerEntryLabel("."),height=2, width=9).grid(row = 7 , column = 2, sticky = E)#Button for "."
Button(root,font=('futura', 15, 'bold'),padx=16,pady=16, text = "=", command = lambda:evaluateAnswer(),height=2, width=9).grid(row = 7 , column = 3, sticky = E)#Button for "=" - final calc button  
#############

#Running the application's main loop
root.mainloop()