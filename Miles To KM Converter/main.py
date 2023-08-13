from tkinter import *
from programme_Labels import Labels
FONT = ("Arial", 13,"normal")
FONT_BOLD = ("Arial", 13,"bold")


def IsButttonClicked():
    ValueDisplay.UpdateTheValue(float(ValueEntry.get()))

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300,height=150)
window.config(padx=30,pady=30)

MileDisplay = Labels(text="Miles",row=1,column=3,font = FONT)

IsEqualToDisplay = Labels(text="is equal to",row=2,column=1, font=FONT)

ValueDisplay = Labels(text=0, row=2, column=2, font=FONT_BOLD)
ValueDisplay.config(padx=20)

CalculateButton = Button(text="Calculate",font=FONT,command=IsButttonClicked)
CalculateButton.grid(row=3,column=2)
CalculateButton.config(padx=20)

ValueEntry = Entry(width=15)
ValueEntry.focus()
ValueEntry.grid(row=1,column=2)








window.mainloop()