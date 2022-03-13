from tkinter import *
from pyswip import Prolog

prolog = Prolog()
# connects the prolog to python
prolog.consult(
    '/Users/Carlisha Nicholson/OneDrive/Documents/GitHub/AI-ES-final-project/AI-project/src/knowledge_base.pl')

c = list(prolog.query("illness(Who)"))

# this is line comment syntax
window = Tk()
greeting = Label(text=c)
print(c)
greeting.pack()
window.mainloop()
