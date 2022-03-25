from email.utils import parsedate_tz
from tkinter import *
from xml.dom.minidom import ReadOnlySequentialNamedNodeMap

# Patient Diagnositics Form


def Diagnosis():
    window = Tk()
    window.configure(background="light blue")
    window.title("Covid-19 Diagnosis System")
    window.geometry("1000x800")
    window.resizable(False, False)

    namelabel = Label(window, text="Full Name: ")
    agelabel = Label(window, text="Age: ")
    templabel = Label(window, text="Temperature (Celsius): ")
    genderlabel = Label(window, text="Gender: ")
    syslabel = Label(window, text="Systolic Reading: ")
    dialabel = Label(window, text="Diastolic Reading: ")
    symlabel = Label(
        window, text="Have you experienced any of the following sysmptoms? ")
    diasym1 = Label(window, text="Dizziness")
    diasym2 = Label(window, text="Fainting")
    diasym3 = Label(window, text="Blurred Vision")
    covidlabel = Label(
        window, text="Have you experienced any of the following symptoms lately?")
    covid_symptom1 = Label(window, text="Fever")
    covid_symptom2 = Label(window, text="Cough")
    covid_symptom3 = Label(window, text="Fatigue")
    covid_symptom4 = Label(window, text="Loss of Taste")
    covid_symptom5 = Label(window, text="Headache")
    covid_symptom6 = Label(window, text="Runny Nose")
    covid_symptom7 = Label(window, text="Sore Throat")
    covid_symptom8 = Label(window, text="Muscle Pain")
    covid_symptom9 = Label(window, text="Difficulty Breathing")
    covid_symptom10 = Label(window, text="Sneezing")
    covid_symptom11 = Label(window, text="Chest Pain")
    covid_symptom12 = Label(window, text="Burst of Confusion")
    covid_symptom13 = Label(window, text="Loss of Speech or Mobility")

    nameentry = Entry(window)
    ageentry = Entry(window)
    tempentry = Entry(window)
    sysentry = Entry(window)
    diaentry = Entry(window)

    w = Canvas(window, width=3, height=250)
    w.create_rectangle(0, 0, 250, 250, fill="black", outline="black")

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

    diz_option1 = Checkbutton(
        window,
        text='Yes',
        onvalue='0',
        offvalue='1'
    )

    diz_option2 = Checkbutton(
        window,
        text='No',
        onvalue='1',
        offvalue='0'
    )

    faint_option1 = Checkbutton(
        window,
        text='Yes',
        onvalue='0',
        offvalue='1'
    )

    faint_option2 = Checkbutton(
        window,
        text='No',
        onvalue='1',
        offvalue='0'
    )

    vision_option1 = Checkbutton(
        window,
        text='Yes',
        onvalue='0',
        offvalue='1'
    )

    vision_option2 = Checkbutton(
        window,
        text='No',
        onvalue='1',
        offvalue='0'
    )

    symp1_option1 = Checkbutton(
        window,
        text='Yes',
        onvalue='0',
        offvalue='1'
    )

    symp1_option2 = Checkbutton(
        window,
        text="No",
        onvalue='1',
        offvalue='0'
    )

    symp2_option1 = Checkbutton(
        window,
        text="Yes",
        onvalue='0',
        offvalue='1'
    )

    symp2_option2 = Checkbutton(
        window,
        text="No",
        onvalue='1',
        offvalue='0'
    )
    symp3_option1 = Checkbutton(
        window,
        text="Yes",
        onvalue='0',
        offvalue='1'
    )

    symp3_option2 = Checkbutton(
        window,
        text="No",
        onvalue='1',
        offvalue='0'
    )

    symp4_option1 = Checkbutton(
        window,
        text="Yes",
        onvalue='0',
        offvalue='1'
    )

    symp4_option2 = Checkbutton(
        window,
        text="No",
        onvalue='1',
        offvalue='0'
    )

    symp5_option1 = Checkbutton(
        window,
        text="Yes",
        onvalue='0',
        offvalue='1'
    )

    symp5_option2 = Checkbutton(
        window,
        text="No",
        onvalue='1',
        offvalue='0'
    )

    symp6_option1 = Checkbutton(
        window,
        text="Yes",
        onvalue='0',
        offvalue='1'
    )

    symp6_option2 = Checkbutton(
        window,
        text="No",
        onvalue='1',
        offvalue='0'
    )

    symp7_option1 = Checkbutton(
        window,
        text="Yes",
        onvalue='0',
        offvalue='1'
    )

    symp7_option2 = Checkbutton(
        window,
        text="No",
        onvalue='1',
        offvalue='0'
    )

    symp8_option1 = Checkbutton(
        window,
        text="Yes",
        onvalue='0',
        offvalue='1'
    )

    symp8_option2 = Checkbutton(
        window,
        text="No",
        onvalue='1',
        offvalue='0'
    )

    symp9_option1 = Checkbutton(
        window,
        text="Yes",
        onvalue='0',
        offvalue='1'
    )
    symp9_option2 = Checkbutton(
        window,
        text="No",
        onvalue='1',
        offvalue='0'
    )

    symp10_option1 = Checkbutton(
        window,
        text="Yes",
        onvalue='0',
        offvalue='1'
    )

    symp10_option2 = Checkbutton(
        window,
        text="No",
        onvalue='1',
        offvalue='0'
    )

    symp11_option1 = Checkbutton(
        window,
        text="Yes",
        onvalue='0',
        offvalue='1'
    )

    symp11_option2 = Checkbutton(
        window,
        text="No",
        onvalue='1',
        offvalue='0'
    )

    symp12_option1 = Checkbutton(
        window,
        text="Yes",
        onvalue='0',
        offvalue='1'
    )

    symp12_option2 = Checkbutton(
        window,
        text="No",
        onvalue='1',
        offvalue='0'
    )

    symp13_option1 = Checkbutton(
        window,
        text="Yes",
        onvalue='0',
        offvalue='1'
    )

    symp13_option2 = Checkbutton(
        window,
        text="No",
        onvalue='1',
        offvalue='0'
    )

    submit_button = Button(
        window,
        text="Submit"
    )

    namelabel.grid(row=0, column=0, padx=2, pady=5)
    agelabel.grid(row=0, column=2,  padx=2, pady=5)
    genderlabel.grid(row=2, column=0,  padx=2, pady=5)
    templabel.grid(row=3, column=0,  padx=2, pady=5)

    symlabel.grid(row=4, column=0, columnspan=3, padx=2, pady=5)
    diasym1.grid(row=5, column=0, padx=2, pady=5)
    diasym2.grid(row=6, column=0, padx=2, pady=5)
    diasym3.grid(row=7, column=0, padx=2, pady=5)
    syslabel.grid(row=8, column=0, padx=2, pady=5)
    dialabel.grid(row=9, column=0, padx=2, pady=5)
    covidlabel.grid(row=10, column=0, columnspan=3, padx=2, pady=5)
    covid_symptom1.grid(row=11, column=0, padx=2, pady=5)
    covid_symptom2.grid(row=11, column=4, padx=2, pady=5)
    covid_symptom3.grid(row=12, column=0, padx=2, pady=5)
    covid_symptom4.grid(row=12, column=4, padx=2, pady=5)
    covid_symptom5.grid(row=13, column=0, padx=2, pady=5)
    covid_symptom6.grid(row=13, column=4, padx=2, pady=5)
    covid_symptom7.grid(row=14, column=0, padx=2, pady=5)
    covid_symptom8.grid(row=14, column=4, padx=2, pady=5)
    covid_symptom9.grid(row=15, column=0, padx=2, pady=5)
    covid_symptom10.grid(row=15, column=4, padx=2, pady=5)
    covid_symptom11.grid(row=16, column=0, padx=2, pady=5)
    covid_symptom12.grid(row=16, column=4, padx=2, pady=5)
    covid_symptom13.grid(row=17, column=0, padx=2, pady=5)

    nameentry.grid(row=0, column=1,  padx=2, pady=5)
    ageentry.grid(row=0, column=3,  padx=2, pady=5)
    tempentry.grid(row=3, column=1,  padx=2, pady=5)
    sysentry.grid(row=8, column=1, padx=2, pady=5)
    diaentry.grid(row=9, column=1, padx=2, pady=5)

    w.grid(row=11, column=3, rowspan=12)

    fgender.grid(row=2, column=1,  padx=2, pady=5)
    mgender.grid(row=2, column=2,  padx=2, pady=5)
    diz_option1.grid(row=5, column=1, padx=2, pady=5)
    diz_option2.grid(row=5, column=2, padx=2, pady=5)
    faint_option1.grid(row=6, column=1, padx=2, pady=5)
    faint_option2.grid(row=6, column=2, padx=2, pady=5)
    vision_option1.grid(row=7, column=1, padx=2, pady=5)
    vision_option2.grid(row=7, column=2, padx=2, pady=5)
    symp1_option1.grid(row=11, column=1, padx=2, pady=5)
    symp1_option2.grid(row=11, column=2, padx=2, pady=5)
    symp2_option1.grid(row=11, column=5, padx=2, pady=5)
    symp2_option2.grid(row=11, column=7, padx=2, pady=5)
    symp3_option1.grid(row=12, column=1, padx=2, pady=5)
    symp3_option2.grid(row=12, column=2, padx=2, pady=5)
    symp4_option1.grid(row=12, column=5, padx=2, pady=5)
    symp4_option2.grid(row=12, column=7, padx=2, pady=5)
    symp5_option1.grid(row=13, column=1, padx=2, pady=5)
    symp5_option2.grid(row=13, column=2, padx=2, pady=5)
    symp6_option1.grid(row=13, column=5, padx=2, pady=5)
    symp6_option2.grid(row=13, column=7, padx=2, pady=5)
    symp7_option1.grid(row=14, column=1, padx=2, pady=5)
    symp7_option2.grid(row=14, column=2, padx=2, pady=5)
    symp8_option1.grid(row=14, column=5, padx=2, pady=5)
    symp8_option2.grid(row=14, column=7, padx=2, pady=5)
    symp9_option1.grid(row=15, column=1, padx=2, pady=5)
    symp9_option2.grid(row=15, column=2, padx=2, pady=5)
    symp10_option1.grid(row=15, column=5, padx=2, pady=5)
    symp10_option2.grid(row=15, column=7, padx=2, pady=5)
    symp11_option1.grid(row=16, column=1, padx=2, pady=5)
    symp11_option2.grid(row=16, column=2, padx=2, pady=5)
    symp12_option1.grid(row=16, column=5, padx=2, pady=5)
    symp12_option2.grid(row=16, column=6, padx=2, pady=5)
    symp13_option1.grid(row=17, column=1, padx=2, pady=5)
    symp13_option2.grid(row=17, column=2, padx=2, pady=5)

    submit_button.grid(row=18, column=0, padx=2, pady=10)

    window.mainloop()
