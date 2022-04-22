%C:\Program Files\swipl\bin\swipl-win

:- use_module(library(pce)).
:- require([ append/3
	   ]).

illness(covid).

illness_type(covid,[regular,delta,omicron]).

variant(regular,[fever,cough,fatigue,'loss of taste',headache]).
variant(delta,[cough,fatigue,headache,'runny nose','sore throat','muscle pain','difficulty breathing']).
variant(omicron,[fatigue,headache,sneezing,'sore throat','runny nose','chest pain','burst of confusion','difficulty breathing','loss of speech or mobility']).

symptoms(mild,[fever,cough,fatigue,'loss of taste',headache,'runny nose', sneezing]).
symptoms(moderate,['sore throat','muscle pain']).
symptoms(severe,['difficulty breathing','loss of speech or mobility','chest pain','burst of confusion']).

underlying(omicron,[stroke,tuberulosis,'sickle cell','HIV','heart conditions',diabetes,alzheimers,dementia,'cystic fibrosis','lung disease','liver disease','kidney disease']).

patient(name('jane'),age('20'),gender('female'),temp('78'),dizzy('yes'),faint('no'),blurry('no'),systolic('135'),diastolic('79')).

menu:-new(M,dialog('COVID-19 Diagnosis System')),
    send(M,append,new(Title,label)),send(Title,append,''),
    new(H1, dialog_group('')),
    new(H2, dialog_group('')),
    send(M,append,H1),
    send(M,append,H2,below),

    send(H2,append,button(new_Variant, message(@prolog,new_variant))),

    %pushes next button into a new line.
    send(H2,append,new(Lbl1,label)),send(Lbl1,append,''),

    send(H2,append,button(underlying_Condition, message(@prolog,ucondition))),
    send(H2,append,new(Lbl2,label)),send(Lbl2,append,''),
    send(H2,append,button(patient_Diagnostic,message(@prolog,patient_diagnostic))),
    send(H2,append,new(Lbl3,label)),send(Lbl3,append,''),
    send(H2,append,button(covid_Statistics,message(@prolog,stat_display))),
    send(H1,append,new(NewV1,label)),send(NewV1,append,'Welcome to Covid-19 Diagnosis System of the Ministry of Health.'),

    send(M,open).


new_variant:-new(V,dialog('New Variant')),send(V,append,new(label)),
    new(V1,dialog_group('')),
    new(V2,dialog_group('')),

    send(V,append,V1),
    send(V,append,V2,below),

    send(V1,append,new(Vl,label)),send(Vl,append,'Enter new Varaint information'),
    send(V2,append,new(Name,text_item(variant_Name))),
    send(V2,append,new(Symptoms,text_item(symptoms))),
    send(V2,append,button(submit,message(@prolog,submit,Name?selection,Symptoms?selection))),

    send(V,open).


%update variant list
%submit(Name,Symptoms):- .


ucondition:- new(C,dialog('Underlying Condition')),send(C,append,new(label)),

    new(C1,dialog_group('')),send(C,append, C1),
    new(C2,dialog_group('')),send(C,append, C2,below),

    send(C2,append,button(new_Underlying_Conditions,message(@prolog,add_ucondition))),
    send(C2,append,new(Lbl1a,label)),send(Lbl1a,append,''),
    send(C2,append,button(view_Underlying_Conditons,message(@prolog,view_ucondition))),
    send(C1,append,new(NewCH,label)),send(NewCH,append,'This system allow you to add or view Underlying Conditions'),
    send(C1,append,new(NewCH1,label)),send(NewCH1,append,'associated with the Omicron Variant.'),

    send(C,open).

patient_diagnostic:- new(D,dialog('Covid-19 Diagnosis')),send(D,append,new(label)),
    new(DG1,dialog_group('')),
    new(DG2,dialog_group('')),
    new(DG3,dialog_group('')),
    new(DG4,dialog_group('')),


   send(D,append,new(Name,text_item(name))),
   send(D,append,new(Age, text_item(age))),
   send(D,append,new(Gender,menu(gender,marked))),
   send(D,append,new(Temperature,text_item(temperature))),
   send(D,append,new(D1,label)),send(D1,append,'Have you experienced any of the following symptoms?'),
   send(D,append,new(Dizzy,menu(dizziness,marked))),
   send(D,append,new(Faint,menu(fainting,marked))),
   send(D,append,new(Blur,menu(blurry_vision,marked))),
   send(D,append,new(SysR,text_item(systolic_Reading))),
   send(D,append,new(DiaR,text_item(diastolic_Reading))),
   send(D,append,new(D2,label)),send(D2,append,'Have you experienced any of the following symptoms lately?'),
   send(D,append,DG1),
   send(DG1,alignment,left),

   send(D,append,DG2,right),
   send(DG1,append,new(Fever,menu(fever,marked))),
   send(DG1,append,new(Fatigue,menu(fatigue,marked))),
   send(DG1,append,new(Head,menu(headache,marked))),
   send(DG1,append,new(Sore,menu(sore_Throat, marked))),
   send(DG1,append,new(DiffB,menu(difficulty_Breathing,marked))),
   send(DG1,append,new(Chest,menu(chest_Pain, marked))),
   send(DG1,append,new(Losm, menu(loss_of_Speech_or_Mobility, marked))),
   send(DG2,append,new(Cough,menu(cough, marked))),
   send(DG2,append,new(Lot, menu(loss_of_Taste, marked))),
   send(DG2,append,new(Run,menu(runny_Nose, marked))),
   send(DG2,append,new(Muscle,menu(muscle_Pain,marked))),
   send(DG2,append,new(Sneeze,menu(sneezing,marked))),
   send(DG2,append,new(Boc,menu(burst_of_Confusion, marked))),
   send(D,append,new(D3,label)),send(D3,append,'Do you or your family have a history of any of the following conditons?'),
   send(D,append,DG3),
   send(DG3,alignment,left),

   send(D,append,DG4,right),
   send(DG3,append,new(Cancer,menu(cancer,marked))),
 %  send(DG3,append,new(Tb,menu(tuberculosis,marked))),
  % send(DG3,append,new(HIV,menu(hIV,marked))),
   send(DG3,append,new(Dia,menu(diabetes,marked))),
  % send(DG3,append,new(Dem,menu(dementia,marked))),
   send(DG3,append,new(Lung,menu(lung_Disease,marked))),
   send(DG3,append,new(Kid,menu(kidney_Disease,marked))),
   send(DG4,append,new(Stroke,menu(stroke,marked))),
   send(DG4,append,new(Sick,menu(sickle_Cell,marked))),
   send(DG4,append,new(Heart,menu(heart_Conditions,marked))),
   send(DG4,append,new(Alz,menu(alzheimers,marked))),
   send(DG4,append,new(Cys,menu(cystic_Fibrosis,marked))),
   send(DG3,append,new(Liver,menu(liver_Disease,marked))),


   send(Gender,append,female), send(Gender,append,male),
   send(Dizzy,append,yes),     send(Dizzy,append,no),
   send(Faint,append,yes),     send(Faint,append,no),
   send(Blur,append,yes),      send(Blur,append,no),
   send(Fever,append,yes),     send(Fever,append,no),
   send(Fatigue,append,yes),   send(Fatigue,append,no),
   send(Head,append,yes),      send(Head,append,no),
   send(Sore,append,yes),      send(Sore,append, no),
   send(DiffB,append,yes),     send(DiffB,append,no),
   send(Chest,append,yes),     send(Chest,append,no),
   send(Losm, append,yes),     send(Losm,append,no),
   send(Cough,append,yes),     send(Cough,append,no),
   send(Lot,append,yes),       send(Lot,append,no),
   send(Run,append,yes),       send(Run,append,no),
   send(Muscle,append,yes),    send(Muscle,append,no),
   send(Sneeze,append,yes),    send(Sneeze,append,no),
   send(Boc,append,yes),       send(Boc,append,no),
   send(Cancer,append,yes),    send(Cancer,append,no),
  % send(Tb,append,yes),        send(Tb,append,no),
   %send(HIV,append,yes),       send(HIV,append,no),
   send(Dia,append,yes),       send(Dia,append,no),
  % send(Dem,append,yes),       send(Dem,append,no),
   send(Lung,append,yes),      send(Lung,append,no),
   send(Kid,append,yes),       send(Kid,append,no),
   send(Stroke,append,yes),    send(Stroke,append,no),
   send(Sick,append,yes),      send(Sick,append,no),
   send(Heart,append,yes),     send(Heart,append,no),
   send(Alz,append,yes),       send(Alz,append,no),
   send(Cys,append,yes),       send(Cys,append,no),
   send(Liver,append,yes),     send(Liver,append,no),

   send(Age,type,int),
   send(Temperature,type,int),
   send(SysR,type,int),
   send(DiaR,type,int),

  send(D,append,button(accept, message(@prolog,save_patient, Name?selection, Age?selection, Gender?selection, Temperature?selection,Dizzy?selection,Faint?selection,Blur?selection,SysR?selection,DiaR?selection,Fever?selection,Fatigue?selection,Head?selection,Sore?selection,DiffB?selection,Chest?selection,Losm?selection,Cough?selection,Lot?selection,Run?selection,Muscle?selection,Sneeze?selection,Boc?selection,Cancer?selection,Dia?selection,Lung?selection,Kid?selection,Stroke?selection,Sick?selection,Heart?selection,Alz?selection,Cys?selection,Liver?selection))),


    send(D,open).

add_ucondition:- new(U,dialog('New Condition')),send(U,append,new(label)),
    send(U,append,new(Uconditon,text_item(underlying_Condition))),
    send(U,append,button(add,message(@prolog,add,Uconditon?selection))),
    send(U,open).

%veiw_condition:-

add(Ucondition):- underlying(omicron,Old),append(Old,[Ucondition],New),
    retractall(underlying(_)),assert(underlying(omicron,New)),
    another_ucondition.


another_ucondition:- new(A,dialog('Add More')),send(A,append,new(label)),
     send(A,append,new(NewA1,label)),send(NewA1,append,'Would you like to add another'),
     send(A,append,button(yes,message(@prolog,add_ucondition))),
     send(A,append,button(no,message(@prolog,close/1))),
     send(A,open).


%displays patient's COVID-19 result
save_patient(Name,Age,Gender,Temperature,Dizzy,Faint,Blur,SysR,DiaR,Fever,Fatigue,Head,Sore,Diffb,Chest,Losm,Cough,Lot,Run,Muscle,Sneeze,Boc,Cancer,Dia,Lung,Kid,Stroke,Liver,Sick,Heart,Alz,Cys):-

    new(S,dialog('Patient Result')),send(S,append,new(label)),
    new(S1,dialog_group('')),
    new(S2,dialog_group('')),

    send(S,append,S1),
    send(S1,alignment,left),
    send(S,append,S2,right),
    send(S1,append,new(Lbl4,label)),send(Lbl4,append,'Name: '),
    send(S2,append,new(Lbl5,label)),send(Lbl5,append,Name),

    send(S1,append,new(Lbl6,label)),send(Lbl6,append,'Age: '),
    send(S2,append,new(Lbl7,label)),send(Lbl7,append,Age),

    send(S1,append,new(Lbl8,label)),send(Lbl8,append,'Gender: '),
    send(S2,append,new(Lbl9,label)),send(Lbl9,append,Gender),

    Temp is(((Temperature)*9)/5+ 32),
    send(S1,append,new(Lbl10,label)),send(Lbl10,append,'Temperature: '),
    send(S2,append,new(Lbl11,label)),send(Lbl11,append,'Patient temperature in Fahrenheit is',Temp),

    send(S1,append,new(Lbl20,label)),send(Lbl20,append,'Patient Systolic Reading:'),
    send(S1,append,new(Lbl21,label)),send(Lbl21,append,SysR),
    send(S1,append,new(Lbl22,label)),send(Lbl22,append,'Patient Diastolic Reading:'),
    send(S1,append,new(Lbl23,label)),send(Lbl23,append,DiaR),

    (SysR<90-> send(Lbl12,append,'Patient blood pressure is low');
    SysR>90,SysR<120-> send(Lbl12,append,'Patient blood pressure is normal');
    SysR>120,SysR<129-> send(Lbl12,append,'Patient blood pressure is elevated');
    SysR>=130-> send(Lbl12,append,'Patient blood pressure is high')),

    (DiaR<80->send(Lbl13,append,'Patient blood pressure is low');
    DiaR<80->send(Lbl13,append,'Patient blood pressure is normal');
    DiaR<80->send(Lbl13,append,'Patient blood pressure is elevated');
    DiaR<80->send(Lbl13,append,'Patient blood pressure is high')),


    (Dizzy =='yes'-> Dissval is 1; Dissval is 0),
    (Faint =='yes'-> Faintval is 1; Faintval is 0),
    (Blur  =='yes'-> Blurval is 1; Blurval is 0),
    (Fever=='yes'-> Feverval is 1; Feverval is 0),
    (Fatigue =='yes'-> Fatigueval is 1; Fatigueval is 0),
    (Head =='yes'-> Headval is 1; Headval is 0),
    (Sore =='yes'-> Soreval is 1;Soreval  is 0),
    (Diffb =='yes'-> Diffbval is 1; Diffbval is 0),
    (Chest =='yes'-> Chestval is 1; Chestval is 0),
    (Losm =='yes'-> Losmval is 1; Losmval is 0),
    (Cough =='yes'-> Coughval is 1; Coughval is 0),
    (Lot =='yes'-> Lotval is 1; Lotval is 0),
    (Run =='yes'-> Runval is 1; Runval is 0),
    (Muscle =='yes'-> Muscleval is 1; Muscleval is 0),
    (Sneeze =='yes'-> Sneezeval is 1; Sneezeval is 0),
    (Boc =='yes'-> Bocval is 1; Bocval is 0),

    Riskfactor is Dissval+Faintval+Blurval+Feverval+Fatigueval+Headval+Soreval+Diffbval+Chestval+Losmval+Coughval+Lotval+Runval+Muscleval+Sneezeval+Bocval,




    send(S,open).




%covid_stats:-



