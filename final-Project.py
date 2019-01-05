#Rezwana Kabita

from tk import DATA

from itertools import cycle

import turtle

from tkinter import *


def GetN():

    r = Tk()

    r.geometry("600x600")

    r.title("letter:")

    print("letters included", intVar.get())



    def bind_button(event):

        if boolVar.get():

            getDataButton.unbind("<Button-1>")

        else:

            getDataButton.bind("<Button-1>", get_data)

    intVar = IntVar()


    intVar.set("number of integer")


    intEntry = Entry(root, textvariable=intVar)

    intEntry.pack(side=TOP)


    getDataButton = Button(root, text="Get Data")

    getDataButton.bind("<Button-1>", get_data)

    getDataButton.pack(side=TOP)



    root.mainloop()



    number = int(intVar.get())

    return(number)



def MAIN_function():

    def count_char(text, char):

        count = 0

        for a in text:

            if a == char:

              count += 1

        return count


    file = open("Words.txt", "r")

    text = file.read()

    textUP = text.upper()

    list_of_percentage = {}

    sumOfPercentages = 0

    for char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":

        perc = (100 * count_char(textUP, char) / len(textUP))

        list_of_percentage[char] = round(perc, 2)

        sumOfPercentages = sumOfPercentages + perc

        print("{0} - {1}%".format(char, round(perc, 2)))



    list_of_percentage["white-space and symbols"] = round(100-sumOfPercentages,2)

    (number_of_letters) = DATA()



    copyOfDict = list_of_percentage.copy()

    listToPie = []



    for n in range(number_of_letters+1):

        listToPie.append(max(list_of_percentage, key=list_of_percentage.get))

        del list_of_percentage[max(list_of_percentage, key=list_of_percentage.get)]



    listToPie.append("the rest of letters")

    print(listToPie)



    sumOfTheShowingLetters = 0

    for each in listToPie[:-1]:

        print(each, copyOfDict[each],"%")

        sumOfTheShowingLetters = sumOfTheShowingLetters + copyOfDict[each]



    sumOfTheRest = round (100 - sumOfTheShowingLetters,2)



    window = turtle.Screen()

    window.setup(720, 720)

    window.bgcolor('white')

    COLORS = cycle(["black", "purple", "red", "blue","pink", "green", "white"])

    RADIUS = 150

    LABEL_RADIUS = 160

    FONTSIZE = 9

    FONT = ("Ariel", FONTSIZE, "bold")



    t = turtle.Turtle()

    t.pensize(1)

    t.shape('turtle')

    t.penup()

    t.sety(-RADIUS)

    t.pendown()



    for SECTOR in listToPie[:-1]:

        t.fillcolor(next(COLORS))

        t.begin_fill()

        t.circle(RADIUS, copyOfDict[SECTOR] * 360 / 100)

        position = t.position()

        t.goto(0, 0)

        t.end_fill()

        t.setposition(position)

    t.fillcolor(next(COLORS))

    t.begin_fill()

    t.circle(RADIUS, sumOfTheRest * 360 / 100)

    position = t.position()

    t.goto(0, 0)

    t.end_fill()

    t.setposition(position)

    t.penup()

    t.sety(-RADIUS)



    for SECTOR in listToPie[:-1]:

        t.circle(LABEL_RADIUS, copyOfDict[SECTOR] * 360 / 100 / 2)

        t.write((SECTOR, copyOfDict[SECTOR]), align="center", font=FONT)

        t.circle(LABEL_RADIUS, copyOfDict[SECTOR] * 360 / 100 / 2)

    t.circle(LABEL_RADIUS, sumOfTheRest * 360 / 100 / 2)

    t.write(('All Other Letters', sumOfTheRest), align="center", font=FONT)



    t.ht()

    window.mainloop()



MAIN_function()

