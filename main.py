import pyperclip
from tkinter import *
from tkinter import scrolledtext
from tkinter import ttk
from tkinter.ttk import *
from random import randint

#Scripts and functions


#Window settings
mainWindow = Tk()
mainWindow.title("Alpha Diceroller App")

#Frames
#   Frame with the user name
NameFrame = Frame(mainWindow)
#   Frame with the user stats
StatFrame = LabelFrame(mainWindow, text="Player stats")
#   Roll control frame
RollFrame = LabelFrame(mainWindow, text="Roll settings")
#   Output text frame
TextFrame = LabelFrame(mainWindow, text="Output")


#   Inputs
#       Player name
NameLabel = Label(NameFrame, text="Character name:")
NameInput = Entry(NameFrame, width=25)

#       Strength stat
StrengthStatFrame = Frame(StatFrame)
StrengthLabel = Label(StrengthStatFrame, width=15, text="Strength:")
StrengthValue = Spinbox(StrengthStatFrame, from_=0, to=50, width=5)
#       Mobility stat
MobilityStatFrame = Frame(StatFrame)
MobilityLabel = Label(MobilityStatFrame, width=15, text="Mobility:")
MobilityValue = Spinbox(MobilityStatFrame, from_=0, to=50, width=5)
#       Intelligence stat
IntelligenceStatFrame = Frame(StatFrame)
IntelligenceLabel = Label(IntelligenceStatFrame, width=15, text="Intelligence:")
IntelligenceValue = Spinbox(IntelligenceStatFrame, from_=0, to=50, width=5)
#       Willpower stat
WillpowerStatFrame = Frame(StatFrame)
WillpowerLabel = Label(WillpowerStatFrame, width=15, text="Willpower:")
WillpowerValue = Spinbox(WillpowerStatFrame, from_=0, to=50, width=5)
#       Style stat
StyleStatFrame = Frame(StatFrame)
StyleLabel = Label(StyleStatFrame, width=15, text="Style:")
StyleValue = Spinbox(StyleStatFrame, from_=0, to=50, width=5)

#   Roll type adjustment
#       Base roll on which stat:
RollBaseFrame = Frame(RollFrame)
RollBaseLabel = Label(RollBaseFrame, width=15, text="Base roll on:")
RollBaseValue = Combobox(RollBaseFrame)
RollBaseValue['values']=("Strength", "Mobility", "Intelligence", "Willpower", "Style")
RollBaseValue.current(0)
#       Expertise level:
RollTypeFrame = Frame(RollFrame)
RollTypeLabel = Label(RollTypeFrame, width=15, text="Expertise level:")
SelectedExpertise = IntVar()
RollBasic = Radiobutton(RollTypeFrame,text='Basic (d6)', value=6, variable=SelectedExpertise)
RollImproved = Radiobutton(RollTypeFrame,text='Improved (d8)', value=8, variable=SelectedExpertise)
RollExpert = Radiobutton(RollTypeFrame,text='Expert (d10)', value=10, variable=SelectedExpertise)
#       Amount of assist dice:
RollAssistFrame = Frame(RollFrame)
RollAssistLabel = Label(RollAssistFrame, width=15, text="Assist dice:")
RollAssistValue = Spinbox(RollAssistFrame, from_=0, to=5, width=5)
#       Choose X best dice:
RollChoiceFrame = Frame(RollFrame)
RollChoiceLabel = Label(RollChoiceFrame, width=15, text="Choose X dice:")
RollChoiceValue = Spinbox(RollChoiceFrame, from_=0, to=10, width=5)
#   Roll button:
outputField=scrolledtext.ScrolledText(TextFrame)

def clickedRoll():
    diceAmount = 0
    if RollBaseValue.get() == "Strength":
        diceAmount = int(StrengthValue.get()) + int(RollAssistValue.get())
    elif RollBaseValue.get() == "Mobility":
        diceAmount = int(MobilityValue.get()) + int(RollAssistValue.get())
    elif RollBaseValue.get() == "Intelligence":
        diceAmount = int(IntelligenceValue.get()) + int(RollAssistValue.get())
    elif RollBaseValue.get() == "Willpower":
        diceAmount = int(WillpowerValue.get())+ int(RollAssistValue.get())
    elif RollBaseValue.get() == "Style":
        diceAmount = int(StyleValue.get())+ int(RollAssistValue.get())
    else:
        diceAmount = 1


    diceType = ""
    if int(SelectedExpertise.get()) == 6:
        diceType = "a basic "
    elif int(SelectedExpertise.get()) == 8:
        diceType = "an improved "
    elif int(SelectedExpertise.get()) == 10:
        diceType = "an expert "
    else:
        diceType = "a "

    firstSeed=[]
    additionalSeed=[]
    intermediateDump = []
    slicedDump = []
    totalResult = 0
    explodingDiceAmount = 0
    explodingDiceString = ""
    rolledDice = diceAmount
    bestDice = int(RollChoiceValue.get())
    limit = int(SelectedExpertise.get())

    while rolledDice > 0:
        a = randint(1, limit)
        firstSeed.append(a)
        rolledDice = rolledDice - 1

    explodingDiceAmount = firstSeed.count(limit)
    explodingDice = explodingDiceAmount

    if explodingDiceAmount != 0:
        while explodingDice > 0:
            a = randint(1, limit)
            additionalSeed.append(a)
            explodingDice = explodingDice - 1
        explodingDiceString = " with " + str(explodingDiceAmount) + " additional exploding dice: " + str(additionalSeed)
        intermediateDump = firstSeed + additionalSeed
    else:
        explodingDiceString = " with no additional exploding dice."
        intermediateDump = firstSeed
    intermediateDump.sort(reverse=True)
    firstSeedString = str(firstSeed)
    slicedDump = intermediateDump[0:bestDice]
    totalResult = sum(slicedDump)
    outputString = str(NameInput.get()) + " rolls for " + str(diceType) + str(RollBaseValue.get()) + "-based check with " + str(RollAssistValue.get()) + " assist dice! \n" + str(diceAmount) + "d" + str(SelectedExpertise.get()) + ": " + firstSeedString + str(explodingDiceString) + "\n" + "Choosing " + str(RollChoiceValue.get()) + " best dice: " + str(slicedDump) + " for a total result of " + str(totalResult)
    outputField.delete(1.0, END)
    outputField.insert(INSERT, outputString)
    pyperclip.copy(outputString)

RollButton = Button(RollFrame, text="Roll!", command=clickedRoll)




#Putting elements out
NameFrame.pack(anchor=NW)
StatFrame.pack(anchor=NW)
RollFrame.pack(anchor=NW)
TextFrame.pack(anchor=NW)


NameLabel.pack(side=LEFT)
NameInput.pack(side=LEFT)

StrengthStatFrame.pack()
StrengthLabel.pack(side=LEFT)
StrengthValue.pack(side=LEFT)

MobilityStatFrame.pack()
MobilityLabel.pack(side=LEFT)
MobilityValue.pack(side=LEFT)

IntelligenceStatFrame.pack()
IntelligenceLabel.pack(side=LEFT)
IntelligenceValue.pack(side=LEFT)

WillpowerStatFrame.pack()
WillpowerLabel.pack(side=LEFT)
WillpowerValue.pack(side=LEFT)


StyleStatFrame.pack()
StyleLabel.pack(side=LEFT)
StyleValue.pack(side=LEFT)

RollBaseFrame.pack()
RollBaseLabel.pack(side=LEFT)
RollBaseValue.pack(side=LEFT)

RollTypeFrame.pack()
RollTypeLabel.pack(side=TOP)
RollBasic.pack(side=TOP)
RollImproved.pack(side=TOP)
RollExpert.pack(side=TOP)


RollAssistFrame.pack()
RollAssistLabel.pack(side=LEFT)
RollAssistValue.pack(side=LEFT)

RollChoiceFrame.pack()
RollChoiceLabel.pack(side=LEFT)
RollChoiceValue.pack(side=LEFT)
RollButton.pack(side=LEFT)
outputField.pack()


#main loop
mainWindow.mainloop()