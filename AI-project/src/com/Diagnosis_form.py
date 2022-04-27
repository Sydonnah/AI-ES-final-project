from tkinter import *
from pyswip import Prolog
from setuptools import Command

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

    underlyingsymp4 = Label(window, text="Sickle Cell")

    underlyingsymp6 = Label(window, text="Heart Conditions")
    underlyingsymp7 = Label(window, text="Diabetes")
    underlyingsymp8 = Label(window, text="Alzheimers")

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

    gender = StringVar(window)
    dizzy = StringVar(window)
    faint = StringVar(window)
    blur = StringVar(window)
    fever = StringVar(window)
    cough = StringVar(window)
    fatigue = StringVar(window)
    l_o_t = StringVar(window)
    head = StringVar(window)
    run_nose = StringVar(window)
    sore = StringVar(window)
    muscle = StringVar(window)
    diff_breath = StringVar(window)
    sneeze = StringVar(window)
    chest = StringVar(window)
    b_o_c = StringVar(window)
    losm = StringVar(window)

    fgender = Radiobutton(
        window,
        text='Female',
        variable=gender,
        value="female"
    )
    mgender = Radiobutton(
        window,
        text='Male',
        variable=gender,
        value="male"
    )

    diz_option1 = Checkbutton(
        window,
        text='Yes',
        onvalue='Yes',
        offvalue='No',
        variable=dizzy
    )
    diz_option2 = Checkbutton(
        window,
        text='No',
        onvalue='No',
        offvalue='Yes',
        variable=dizzy
    )

    faint_option1 = Checkbutton(
        window,
        text='Yes',
        onvalue='Yes',
        offvalue='No',
        variable=faint
    )
    faint_option2 = Checkbutton(
        window,
        text='No',
        onvalue='No',
        offvalue='Yes',
        variable=faint
    )

    vision_option1 = Checkbutton(
        window,
        text='Yes',
        onvalue='Yes',
        offvalue='No',
        variable=blur
    )
    vision_option2 = Checkbutton(
        window,
        text='No',
        onvalue='No',
        offvalue='Yes',
        variable=blur
    )

    symp1_option1 = Checkbutton(
        window,
        text='Yes',
        onvalue='Yes',
        offvalue='No',
        variable=fever
    )
    symp1_option2 = Checkbutton(
        window,
        text="No",
        onvalue='No',
        offvalue='Yes',
        variable=fever
    )

    symp2_option1 = Checkbutton(
        window,
        text="Yes",
        onvalue='Yes',
        offvalue='No',
        variable=cough

    )
    symp2_option2 = Checkbutton(
        window,
        text="No",
        onvalue='No',
        offvalue='Yes',
        variable=cough
    )

    symp3_option1 = Checkbutton(
        window,
        text="Yes",
        onvalue='Yes',
        offvalue='No',
        variable=fatigue
    )
    symp3_option2 = Checkbutton(
        window,
        text="No",
        onvalue='No',
        offvalue='Yes',
        variable=fatigue
    )

    symp4_option1 = Checkbutton(
        window,
        text="Yes",
        onvalue='Yes',
        offvalue='No',
        variable=l_o_t
    )
    symp4_option2 = Checkbutton(
        window,
        text="No",
        onvalue='No',
        offvalue='Yes',
        variable=l_o_t
    )

    symp5_option1 = Checkbutton(
        window,
        text="Yes",
        onvalue='Yes',
        offvalue='No',
        variable=head
    )
    symp5_option2 = Checkbutton(
        window,
        text="No",
        onvalue='No',
        offvalue='Yes',
        variable=head
    )

    symp6_option1 = Checkbutton(
        window,
        text="Yes",
        onvalue='Yes',
        offvalue='No',
        variable=run_nose
    )
    symp6_option2 = Checkbutton(
        window,
        text="No",
        onvalue='No',
        offvalue='Yes',
        variable=run_nose
    )

    symp7_option1 = Checkbutton(
        window,
        text="Yes",
        onvalue='Yes',
        offvalue='No',
        variable=sore,
    )
    symp7_option2 = Checkbutton(
        window,
        text="No",
        onvalue='No',
        offvalue='Yes',
        variable=sore
    )

    symp8_option1 = Checkbutton(
        window,
        text="Yes",
        onvalue='Yes',
        offvalue='No',
        variable=muscle
    )
    symp8_option2 = Checkbutton(
        window,
        text="No",
        onvalue='No',
        offvalue='Yes',
        variable=muscle
    )

    symp9_option1 = Checkbutton(
        window,
        text="Yes",
        onvalue='Yes',
        offvalue='No',
        variable=diff_breath
    )
    symp9_option2 = Checkbutton(
        window,
        text="No",
        onvalue='No',
        offvalue='Yes',
        variable=diff_breath
    )

    symp10_option1 = Checkbutton(
        window,
        text="Yes",
        onvalue='Yes',
        offvalue='No',
        variable=sneeze
    )
    symp10_option2 = Checkbutton(
        window,
        text="No",
        onvalue='No',
        offvalue='Yes',
        variable=sneeze
    )

    symp11_option1 = Checkbutton(
        window,
        text="Yes",
        onvalue='Yes',
        offvalue='No',
        variable=chest
    )
    symp11_option2 = Checkbutton(
        window,
        text="No",
        onvalue='No',
        offvalue='Yes',
        variable=chest
    )

    symp12_option1 = Checkbutton(
        window,
        text="Yes",
        onvalue='Yes',
        offvalue='No',
        variable=b_o_c
    )
    symp12_option2 = Checkbutton(
        window,
        text="No",
        onvalue='No',
        offvalue='Yes',
        variable=b_o_c
    )

    symp13_option1 = Checkbutton(
        window,
        text="Yes",
        onvalue='Yes',
        offvalue='No',
        variable=losm
    )
    symp13_option2 = Checkbutton(
        window,
        text="No",
        onvalue='No',
        offvalue='Yes',
        variable=losm
    )

    cancer = StringVar(window)
    stroke = StringVar(window)

    sick = StringVar(window)

    heart = StringVar(window)
    dia = StringVar(window)
    alz = StringVar(window)

    cys = StringVar(window)
    lung = StringVar(window)
    liver = StringVar(window)
    kid = StringVar(window)

    underlyingsymp1_option1 = Checkbutton(
        window,
        text="Yes",
        onvalue='Yes',
        offvalue='No',
        variable=cancer
    )
    underlyingsymp1_option2 = Checkbutton(
        window,
        text="No",
        onvalue="No",
        offvalue="Yes",
        variable=cancer
    )

    underlyingsymp2_option1 = Checkbutton(
        window,
        text="Yes",
        onvalue="Yes",
        offvalue="No",
        variable=stroke
    )
    underlyingsymp2_option2 = Checkbutton(
        window,
        text="No",
        onvalue="No",
        offvalue="Yes",
        variable=stroke
    )

    underlyingsymp4_option1 = Checkbutton(
        window,
        text="Yes",
        onvalue="Yes",
        offvalue="No",
        variable=sick
    )
    underlyingsymp4_option2 = Checkbutton(
        window,
        text="No",
        onvalue="No",
        offvalue="Yes",
        variable=sick
    )

    underlyingsymp6_option1 = Checkbutton(
        window,
        text="Yes",
        onvalue="Yes",
        offvalue="No",
        variable=heart
    )
    underlyingsymp6_option2 = Checkbutton(
        window,
        text="No",
        onvalue="No",
        offvalue="Yes",
        variable=heart
    )

    underlyingsymp7_option1 = Checkbutton(
        window,
        text="Yes",
        onvalue="Yes",
        offvalue="No",
        variable=dia
    )
    underlyingsymp7_option2 = Checkbutton(
        window,
        text="No",
        onvalue="No",
        offvalue="Yes",
        variable=dia
    )

    underlyingsymp8_option1 = Checkbutton(
        window,
        text="Yes",
        onvalue="Yes",
        offvalue="No",
        variable=alz
    )
    underlyingsymp8_option2 = Checkbutton(
        window,
        text="No",
        onvalue="No",
        offvalue="Yes",
        variable=alz
    )

    underlyingsymp10_option1 = Checkbutton(
        window,
        text="Yes",
        onvalue="Yes",
        offvalue="No",
        variable=cys
    )
    underlyingsymp10_option2 = Checkbutton(
        window,
        text="No",
        onvalue="No",
        offvalue="Yes",
        variable=cys
    )

    underlyingsymp11_option1 = Checkbutton(
        window,
        text="Yes",
        onvalue="Yes",
        offvalue="No",
        variable=lung
    )
    underlyingsymp11_option2 = Checkbutton(
        window,
        text="No",
        onvalue="No",
        offvalue="Yes",
        variable=lung
    )

    underlyingsymp12_option1 = Checkbutton(
        window,
        text="Yes",
        onvalue="Yes",
        offvalue="No",
        variable=liver
    )
    underlyingsymp12_option2 = Checkbutton(
        window,
        text="No",
        onvalue="No",
        offvalue="Yes",
        variable=liver
    )

    underlyingsymp13_option1 = Checkbutton(
        window,
        text="Yes",
        onvalue="Yes",
        offvalue="No",
        variable=kid
    )
    underlyingsymp13_option2 = Checkbutton(
        window,
        text="No",
        onvalue="No",
        offvalue="Yes",
        variable=kid
    )

    def GetInfo():

        Status = list(Prolog.query("save_patient_python(" + nameentry.get() + "," + ageentry.get() + ","+gender.get() + ","+tempentry.get()+","+dizzy.get()+","+faint.get()+","+blur.get()+","+sysentry.get()+","+diaentry.get()+","+fever.get() + ","+fatigue.get()+","+head.get()+","+sore.get()+","+diff_breath.get() +
                      ","+chest.get()+","+losm.get()+"," + cough.get()+","+l_o_t.get()+","+run_nose.get()+"," + muscle.get()+","+sneeze.get()+","+b_o_c.get()+","+cancer.get()+","+dia.get()+","+lung.get()+","+kid.get()+","+stroke.get()+","+sick.get()+","+heart.get()+","+alz.get()+","+cys.get()+","+liver.get()+")"))

        print(Status)

    submit_button = Button(
        window,
        text="Submit",
        command=GetInfo

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

    underlyingsymp4.grid(row=21, column=0, padx=2, pady=2)

    underlyingsymp6.grid(row=21, column=4, padx=2, pady=2)
    underlyingsymp7.grid(row=22, column=0, padx=2, pady=2)
    underlyingsymp8.grid(row=22, column=4, padx=2, pady=2)

    underlyingsymp10.grid(row=23, column=0, padx=2, pady=2)
    underlyingsymp11.grid(row=23, column=4, padx=2, pady=2)
    underlyingsymp12.grid(row=24, column=0, padx=2, pady=2)
    underlyingsymp13.grid(row=24, column=4, padx=2, pady=2)

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

    underlyingsymp4_option1.grid(row=21, column=1, padx=2, pady=2)
    underlyingsymp4_option2.grid(row=21, column=2, padx=2, pady=2)

    underlyingsymp6_option1.grid(row=21, column=5, padx=2, pady=2)
    underlyingsymp6_option2.grid(row=21, column=7, padx=2, pady=2)
    underlyingsymp7_option1.grid(row=22, column=1, padx=2, pady=2)
    underlyingsymp7_option2.grid(row=22, column=2, padx=2, pady=2)
    underlyingsymp8_option1.grid(row=22, column=5, padx=2, pady=2)
    underlyingsymp8_option2.grid(row=22, column=7, padx=2, pady=2)

    underlyingsymp10_option1.grid(row=23, column=1, padx=2, pady=2)
    underlyingsymp10_option2.grid(row=23, column=2, padx=2, pady=2)
    underlyingsymp11_option1.grid(row=23, column=5, padx=2, pady=2)
    underlyingsymp11_option2.grid(row=23, column=7, padx=2, pady=2)
    underlyingsymp12_option1.grid(row=24, column=1, padx=2, pady=2)
    underlyingsymp12_option2.grid(row=24, column=2, padx=2, pady=2)
    underlyingsymp13_option1.grid(row=24, column=5, padx=2, pady=2)
    underlyingsymp13_option2.grid(row=24, column=7, padx=2, pady=2)

    submit_button.grid(row=40, column=0, padx=2, pady=15)
    window.mainloop()
