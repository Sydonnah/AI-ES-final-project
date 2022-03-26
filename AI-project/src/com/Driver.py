from Diagnosis_form import *
from tkinter import *
from pyswip import Prolog

prolog = Prolog()
# connects the prolog to python
prolog.consult(
    '/Users/Carlisha Nicholson/OneDrive/Documents/GitHub/AI-ES-final-project/AI-project/src/knowledge_base.pl')

# c = list(prolog.query("illness(Who)"))

# Home Page of Expert Systems


def Main():

    main = Tk()
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


Main()
