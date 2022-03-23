
from tkinter import *
from pyswip import Prolog

prolog = Prolog()
# connects the prolog to python
prolog.consult(
    '/Users/Carlisha Nicholson/OneDrive/Documents/GitHub/AI-ES-final-project/AI-project/src/knowledge_base.pl')

#c = list(prolog.query("illness(Who)"))

# Home Page of Expert Systems


def Main():

    main = Tk()
    main.configure(background="light blue")
    main.title("Covid-19 Diagnosis System")
    main.geometry("500x400")
    main.resizable(False, False)

    head = Label(main,
                 text="Welcome to the Ministry of Health's Covid-19 patient Diagnosis System")

    first = Button(main,
                   text="Diagnose Patient",
                   command=Diagnosis)

    first.grid(row=1, column=0, padx=5, pady=10)
    head.grid(row=0, column=0, padx=5, pady=10)
    main.mainloop()


# Patient Diagnositics Form
def Diagnosis():
    window = Tk()
    window.configure(background="light blue")
    window.title("Covid-19 Diagnosis System")
    window.geometry("700x600")
    window.resizable(False, False)

    namelabel = Label(window, text="Full Name: ")
    agelabel = Label(window, text="Age: ")
    templabel = Label(window, text="Temperature (Celsius): ")
    genderlabel = Label(window, text="Gender: ")
    syslabel = Label(window, text="Systolic Reading: ")
    dialabel = Label(window, text="Diastolic Reading: ")
    symlabel = Label(
        window, text="Please select all the symptoms that you have experienced from the list below : ")

    nameentry = Entry(window)
    ageentry = Entry(window)
    tempentry = Entry(window)
    sysentry = Entry(window)
    diaentry = Entry(window)

    fgender = Radiobutton(
        window,
        text='Female',
        value='female'
    )
    mgender = Radiobutton(
        window,
        text='Male',
        value='male'
    )

    back = Button(
        window,
        text="Back",
        command=Main)

    namelabel.grid(row=0, column=0, padx=5, pady=10)
    agelabel.grid(row=1, column=0,  padx=5, pady=10)
    genderlabel.grid(row=2, column=0,  padx=5, pady=10)
    templabel.grid(row=3, column=0,  padx=5, pady=10)
    syslabel.grid(row=4, column=0,  padx=5, pady=10)
    dialabel.grid(row=5, column=0, padx=5, pady=10)
    symlabel.grid(row=6, column=0, columnspan=3, padx=5, pady=10)

    nameentry.grid(row=0, column=1,  padx=5, pady=10)
    ageentry.grid(row=1, column=1,  padx=5, pady=10)
    tempentry.grid(row=3, column=1,  padx=5, pady=10)
    sysentry.grid(row=4, column=1, padx=5, pady=10)
    diaentry.grid(row=5, column=1, padx=5, pady=10)

    fgender.grid(row=2, column=1,  padx=5, pady=10)
    mgender.grid(row=2, column=2,  padx=5, pady=10)

    back.grid(row=9, column=0, padx=5, pady=10)

    window.mainloop()


Main()
