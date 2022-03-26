from email.utils import parsedate_tz
from operator import truediv
from tkinter import *
from xml.dom.minidom import ReadOnlySequentialNamedNodeMap

# Patient Diagnositics Form


def Diagnosis():
    window = Tk()
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
        window, text="Have you experienced any of the following symptoms? ")
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
    underlyinglabel = Label(
        window, text="Do you or your family have a history of any of the following conditions?")
    underlyingsymp1 = Label(window, text="Cancer")
    underlyingsymp2 = Label(window, text="Stroke")
    underlyingsymp3 = Label(window, text="Tuberulosis")
    underlyingsymp4 = Label(window, text="Sickle Cell")
    underlyingsymp5 = Label(window, text="HIV")
    underlyingsymp6 = Label(window, text="Heart Conditions")
    underlyingsymp7 = Label(window, text="Diabetes")
    underlyingsymp8 = Label(window, text="Alzheimers")
    underlyingsymp9 = Label(window, text="Dementia")
    underlyingsymp10 = Label(window, text="Cystic Fibrosis")
    underlyingsymp11 = Label(window, text="Lung Disease")
    underlyingsymp12 = Label(window, text="Liver Disease")
    underlyingsymp13 = Label(window, text="Kidney Disease")

    nameentry = Entry(window)
    ageentry = Entry(window)
    tempentry = Entry(window)
    sysentry = Entry(window)
    diaentry = Entry(window)

    w = Canvas(window, width=2, height=220)
    w.create_rectangle(0, 0, 220, 220, fill="black")

    s = Canvas(window, width=2, height=220)
    s.create_rectangle(0, 0, 220, 220, fill="black")

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

    underlyingsymp1_option1 = Checkbutton(
        window,
        text="Yes",
        onvalue="0",
        offvalue="1"
    )
    underlyingsymp1_option2 = Checkbutton(
        window,
        text="No",
        onvalue="1",
        offvalue="0"
    )
    underlyingsymp2_option1 = Checkbutton(
        window,
        text="Yes",
        onvalue="0",
        offvalue="1"
    )
    underlyingsymp2_option2 = Checkbutton(
        window,
        text="No",
        onvalue="1",
        offvalue="0"
    )
    underlyingsymp3_option1 = Checkbutton(
        window,
        text="Yes",
        onvalue="0",
        offvalue="1"
    )
    underlyingsymp3_option2 = Checkbutton(
        window,
        text="No",
        onvalue="1",
        offvalue="0"
    )
    underlyingsymp4_option1 = Checkbutton(
        window,
        text="Yes",
        onvalue="0",
        offvalue="1"
    )
    underlyingsymp4_option2 = Checkbutton(
        window,
        text="No",
        onvalue="1",
        offvalue="0"
    )
    underlyingsymp5_option1 = Checkbutton(
        window,
        text="Yes",
        onvalue="0",
        offvalue="1"
    )
    underlyingsymp5_option2 = Checkbutton(
        window,
        text="No",
        onvalue="1",
        offvalue="0"
    )
    underlyingsymp6_option1 = Checkbutton(
        window,
        text="Yes",
        onvalue="0",
        offvalue="1"
    )
    underlyingsymp6_option2 = Checkbutton(
        window,
        text="No",
        onvalue="1",
        offvalue="0"
    )
    underlyingsymp7_option1 = Checkbutton(
        window,
        text="Yes",
        onvalue="0",
        offvalue="1"
    )
    underlyingsymp7_option2 = Checkbutton(
        window,
        text="No",
        onvalue="1",
        offvalue="0"
    )
    underlyingsymp8_option1 = Checkbutton(
        window,
        text="Yes",
        onvalue="0",
        offvalue="1"
    )
    underlyingsymp8_option2 = Checkbutton(
        window,
        text="No",
        onvalue="1",
        offvalue="0"
    )
    underlyingsymp9_option1 = Checkbutton(
        window,
        text="Yes",
        onvalue="0",
        offvalue="1"
    )
    underlyingsymp9_option2 = Checkbutton(
        window,
        text="No",
        onvalue="1",
        offvalue="0"
    )
    underlyingsymp10_option1 = Checkbutton(
        window,
        text="Yes",
        onvalue="0",
        offvalue="1"
    )
    underlyingsymp10_option2 = Checkbutton(
        window,
        text="No",
        onvalue="1",
        offvalue="0"
    )
    underlyingsymp11_option1 = Checkbutton(
        window,
        text="Yes",
        onvalue="0",
        offvalue="1"
    )
    underlyingsymp11_option2 = Checkbutton(
        window,
        text="No",
        onvalue="1",
        offvalue="0"
    )
    underlyingsymp12_option1 = Checkbutton(
        window,
        text="Yes",
        onvalue="0",
        offvalue="1"
    )
    underlyingsymp12_option2 = Checkbutton(
        window,
        text="No",
        onvalue="1",
        offvalue="0"
    )
    underlyingsymp13_option1 = Checkbutton(
        window,
        text="Yes",
        onvalue="0",
        offvalue="1"
    )
    underlyingsymp13_option2 = Checkbutton(
        window,
        text="No",
        onvalue="1",
        offvalue="0"
    )

    submit_button = Button(
        window,
        text="Submit"
    )

    namelabel.grid(row=0, column=0, padx=2, pady=2)
    agelabel.grid(row=0, column=2,  padx=2, pady=2)
    genderlabel.grid(row=2, column=0,  padx=2, pady=2)
    templabel.grid(row=3, column=0,  padx=2, pady=2)

    symlabel.grid(row=4, column=0, columnspan=3, padx=2, pady=2)
    diasym1.grid(row=5, column=0, padx=2, pady=2)
    diasym2.grid(row=6, column=0, padx=2, pady=2)
    diasym3.grid(row=7, column=0, padx=2, pady=2)
    syslabel.grid(row=8, column=0, padx=2, pady=2)
    dialabel.grid(row=9, column=0, padx=2, pady=2)
    covidlabel.grid(row=10, column=0, columnspan=3, padx=2, pady=2)
    covid_symptom1.grid(row=11, column=0, padx=2, pady=2)
    covid_symptom2.grid(row=11, column=4, padx=2, pady=2)
    covid_symptom3.grid(row=12, column=0, padx=2, pady=2)
    covid_symptom4.grid(row=12, column=4, padx=2, pady=2)
    covid_symptom5.grid(row=13, column=0, padx=2, pady=2)
    covid_symptom6.grid(row=13, column=4, padx=2, pady=2)
    covid_symptom7.grid(row=14, column=0, padx=2, pady=2)
    covid_symptom8.grid(row=14, column=4, padx=2, pady=2)
    covid_symptom9.grid(row=15, column=0, padx=2, pady=2)
    covid_symptom10.grid(row=15, column=4, padx=2, pady=2)
    covid_symptom11.grid(row=16, column=0, padx=2, pady=2)
    covid_symptom12.grid(row=16, column=4, padx=2, pady=2)
    covid_symptom13.grid(row=17, column=0, padx=2, pady=2)
    underlyinglabel.grid(row=19, column=0, columnspan=3, padx=2, pady=10)
    underlyingsymp1.grid(row=20, column=0, padx=2, pady=2)
    underlyingsymp2.grid(row=20, column=4, padx=2, pady=2)
    underlyingsymp3.grid(row=21, column=0, padx=2, pady=2)
    underlyingsymp4.grid(row=21, column=4, padx=2, pady=2)
    underlyingsymp5.grid(row=22, column=0, padx=2, pady=2)
    underlyingsymp6.grid(row=22, column=4, padx=2, pady=2)
    underlyingsymp7.grid(row=23, column=0, padx=2, pady=2)
    underlyingsymp8.grid(row=23, column=4, padx=2, pady=2)
    underlyingsymp9.grid(row=24, column=0, padx=2, pady=2)
    underlyingsymp10.grid(row=24, column=4, padx=2, pady=2)
    underlyingsymp11.grid(row=25, column=0, padx=2, pady=2)
    underlyingsymp12.grid(row=25, column=4, padx=2, pady=2)
    underlyingsymp13.grid(row=26, column=0, padx=2, pady=2)

    nameentry.grid(row=0, column=1,  padx=2, pady=2)
    ageentry.grid(row=0, column=3,  padx=2, pady=2)
    tempentry.grid(row=3, column=1,  padx=2, pady=2)
    sysentry.grid(row=8, column=1, padx=2, pady=2)
    diaentry.grid(row=9, column=1, padx=2, pady=2)

    w.grid(row=8, column=3, rowspan=12)
    s.grid(row=18, column=3, rowspan=12)

    fgender.grid(row=2, column=1,  padx=2, pady=2)
    mgender.grid(row=2, column=2,  padx=2, pady=2)
    diz_option1.grid(row=5, column=1, padx=2, pady=2)
    diz_option2.grid(row=5, column=2, padx=2, pady=2)
    faint_option1.grid(row=6, column=1, padx=2, pady=2)
    faint_option2.grid(row=6, column=2, padx=2, pady=2)
    vision_option1.grid(row=7, column=1, padx=2, pady=2)
    vision_option2.grid(row=7, column=2, padx=2, pady=2)
    symp1_option1.grid(row=11, column=1, padx=2, pady=2)
    symp1_option2.grid(row=11, column=2, padx=2, pady=2)
    symp2_option1.grid(row=11, column=5, padx=2, pady=2)
    symp2_option2.grid(row=11, column=7, padx=2, pady=2)
    symp3_option1.grid(row=12, column=1, padx=2, pady=2)
    symp3_option2.grid(row=12, column=2, padx=2, pady=2)
    symp4_option1.grid(row=12, column=5, padx=2, pady=2)
    symp4_option2.grid(row=12, column=7, padx=2, pady=2)
    symp5_option1.grid(row=13, column=1, padx=2, pady=2)
    symp5_option2.grid(row=13, column=2, padx=2, pady=2)
    symp6_option1.grid(row=13, column=5, padx=2, pady=2)
    symp6_option2.grid(row=13, column=7, padx=2, pady=2)
    symp7_option1.grid(row=14, column=1, padx=2, pady=2)
    symp7_option2.grid(row=14, column=2, padx=2, pady=2)
    symp8_option1.grid(row=14, column=5, padx=2, pady=2)
    symp8_option2.grid(row=14, column=7, padx=2, pady=2)
    symp9_option1.grid(row=15, column=1, padx=2, pady=2)
    symp9_option2.grid(row=15, column=2, padx=2, pady=2)
    symp10_option1.grid(row=15, column=5, padx=2, pady=2)
    symp10_option2.grid(row=15, column=7, padx=2, pady=2)
    symp11_option1.grid(row=16, column=1, padx=2, pady=2)
    symp11_option2.grid(row=16, column=2, padx=2, pady=2)
    symp12_option1.grid(row=16, column=5, padx=2, pady=2)
    symp12_option2.grid(row=16, column=6, padx=2, pady=2)
    symp13_option1.grid(row=17, column=1, padx=2, pady=2)
    symp13_option2.grid(row=17, column=2, padx=2, pady=2)
    underlyingsymp1_option1.grid(row=20, column=1, padx=2, pady=2)
    underlyingsymp1_option2.grid(row=20, column=2, padx=2, pady=2)
    underlyingsymp2_option1.grid(row=20, column=5, padx=2, pady=2)
    underlyingsymp2_option2.grid(row=20, column=7, padx=2, pady=2)
    underlyingsymp3_option1.grid(row=21, column=1, padx=2, pady=2)
    underlyingsymp3_option2.grid(row=21, column=2, padx=2, pady=2)
    underlyingsymp4_option1.grid(row=21, column=5, padx=2, pady=2)
    underlyingsymp4_option2.grid(row=21, column=7, padx=2, pady=2)
    underlyingsymp5_option1.grid(row=22, column=1, padx=2, pady=2)
    underlyingsymp5_option2.grid(row=22, column=2, padx=2, pady=2)
    underlyingsymp6_option1.grid(row=22, column=5, padx=2, pady=2)
    underlyingsymp6_option2.grid(row=22, column=7, padx=2, pady=2)
    underlyingsymp7_option1.grid(row=23, column=1, padx=2, pady=2)
    underlyingsymp7_option2.grid(row=23, column=2, padx=2, pady=2)
    underlyingsymp8_option1.grid(row=23, column=5, padx=2, pady=2)
    underlyingsymp8_option2.grid(row=23, column=7, padx=2, pady=2)
    underlyingsymp9_option1.grid(row=24, column=1, padx=2, pady=2)
    underlyingsymp9_option2.grid(row=24, column=2, padx=2, pady=2)
    underlyingsymp10_option1.grid(row=24, column=5, padx=2, pady=2)
    underlyingsymp10_option2.grid(row=24, column=7, padx=2, pady=2)
    underlyingsymp11_option1.grid(row=25, column=1, padx=2, pady=2)
    underlyingsymp11_option2.grid(row=25, column=2, padx=2, pady=2)
    underlyingsymp12_option1.grid(row=25, column=5, padx=2, pady=2)
    underlyingsymp12_option2.grid(row=25, column=7, padx=2, pady=2)
    underlyingsymp13_option1.grid(row=26, column=1, padx=2, pady=2)
    underlyingsymp13_option2.grid(row=26, column=2, padx=2, pady=2)

    submit_button.grid(row=40, column=0, padx=2, pady=15)

    window.mainloop()
