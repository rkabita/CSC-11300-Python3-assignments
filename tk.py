from tkinter import *

def DATA():
    r = Tk()
    r.geometry("600x600")
    r.title("letters")

    def get_data(event):
        print("letters included", intVar.get())
    def bind_button(event):
        if boolVar.get():
            getDataButton.unbind("<Button-1>")
        else:
            getDataButton.bind("<Button-1>", get_data)
    intVar = IntVar()

    intVar.set("number of letters")

    intEntry = Entry(r, textvariable=intVar)
    intEntry.pack(side=TOP)

    getDataButton = Button(r, text=" Data")
    getDataButton.bind("<Button-1>", get_data)
    getDataButton.pack(side=TOP)

    r.mainloop()

    number = int(intVar.get())
    return(number)


