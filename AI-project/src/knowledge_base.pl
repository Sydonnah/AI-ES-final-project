%C:\Program Files\swipl\bin\swipl-win

:- use_module(library(pce)).
:- require([ append/3
	   ]).
:- dynamic underlying/1.
:-dynamic variants/1.

illness(covid).

illness_type(covid,[regular,delta,omicron]).

variants(regular,[fever,cough,fatigue,'loss of taste',headache]).

variants(delta,[cough,fatigue,headache,'runny nose','sore throat','muscle pain','difficulty breathing']).
variants(omicron,[cough,fatigue,headache,sneezing,'sore throat','runny nose','chest pain','burst of confusion','difficulty breathing','loss of speech or mobility']).

symptoms(mild,[fever,cough,fatigue,'loss of taste',headache,'runny nose', sneezing]).
symptoms(moderate,['sore throat','muscle pain']).
symptoms(severe,['difficulty breathing','loss of speech or mobility','chest pain','burst of confusion']).

 underlying(omicron,[stroke,tuberulosis,'sickle cell','HIV','heart
 conditions',diabetes,alzheimers,dementia,'cystic fibrosis','lung
 disease','liver disease','kidney disease']).

%underlying(omicron,[stroke,tuberulosis,'sickle cell','HIV']).

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
submit(Name,Symptoms):-
       variants(Name,Old),append(Old,[Symptoms],New),
       redefine_system_predicate('variants'(_,_)),
       retractall(variants(_)),
    assertz(variants(Name,(New))),
    nl,write(Symptoms), write(' added to '),write(Name), write(' variant').


ucondition:- new(C,dialog('Underlying Condition')),send(C,append,new(label)),

    new(C1,dialog_group('')),send(C,append, C1),
    new(C2,dialog_group('')),send(C,append, C2,below),

    send(C2,append,button(new_Underlying_Conditions,message(@prolog,add_ucondition))),
    send(C2,append,new(CLbl1,label)),send(CLbl1,append,''),
    send(C2,append,button(view_Underlying_Conditons,message(@prolog,view_ucondition))),
    send(C1,append,new(NewCH,label)),send(NewCH,append,'This system allow you to add or view Underlying Conditions'),
    send(C1,append,new(NewCH1,label)),send(NewCH1,append,'associated with the Omicron Variant.'),

    send(C,open).

patient_diagnostic:- new(D,dialog('Covid-19 Diagnosis Form' )),send(D,append,new(label)),
    new(DG1,dialog_group('')),
    new(DG2,dialog_group('')),
    new(DG3,dialog_group('')),
    new(DG4,dialog_group('')),


   send(D,append,new(Name,text_item(name))),
   send(D,append,new(Age, text_item(age))),
   send(D,append,new(Gender,menu(gender,marked))),
   send(D,append,new(Temperature,text_item('temperature(C)'))),
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
   send(DG3,append,new(Tb,menu(tuberculosis,marked))),
   send(DG3,append,new(HIV,menu(hIV,marked))),
   send(DG3,append,new(Dia,menu(diabetes,marked))),
   send(DG3,append,new(Dem,menu(dementia,marked))),
   send(DG3,append,new(Lung,menu(lung_Disease,marked))),
   send(DG3,append,new(Kid,menu(kidney_Disease,marked))),
   send(DG4,append,new(Stroke,menu(stroke,marked))),
   send(DG4,append,new(Sick,menu(sickle_Cell,marked))),
   send(DG4,append,new(Heart,menu(heart_Conditions,marked))),
   send(DG4,append,new(Alz,menu(alzheimers,marked))),
   send(DG4,append,new(Cys,menu(cystic_Fibrosis,marked))),
   send(DG4,append,new(Liver,menu(liver_Disease,marked))),


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
   send(Tb,append,yes),        send(Tb,append,no),
   send(HIV,append,yes),       send(HIV,append,no),
   send(Dia,append,yes),       send(Dia,append,no),
   send(Dem,append,yes),       send(Dem,append,no),
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

   send(D,append,button(accept, message(@prolog,save_diagnosis_prolog, Name?selection, Age?selection, Gender?selection, Temperature?selection,
                                        Dizzy?selection, Faint?selection, Blur?selection, SysR?selection, DiaR?selection, Fever?selection,
                                       Fatigue?selection, Head?selection, Sore?selection, DiffB?selection, Chest?selection, Losm?selection,
                                       Cough?selection, Lot?selection, Run?selection, Muscle?selection, Sneeze?selection, Boc?selection,
                                       Cancer?selection, Tb?selection, HIV?selection, Dia?selection, Dem?selection, Lung?selection,
                                       Kid?selection, Stroke?selection, Sick?selection, Heart?selection, Alz?selection, Cys?selection,
                                       Liver?selection))),


    send(D,open).

save_diagnosis_prolog(Name,Age,Gender,Temperature,Dizzy,Faint,Blur,SysR,DiaR,Fever,Fatigue,Head,Sore,
                      DiffB,Chest,Losm,Cough,Lot,Run,Muscle,Sneeze,Boc,Cancer,Tb,HIV,Dia,Dem,Lung,Kid,
                      Stroke,Sick,Heart,Alz,Cys,Liver):-

    new(SDP,dialog('Diagnosis Information')),send(SDP,append,new(label)),
    send(SDP,append,new(SDP1,label)),send(SDP1,append,'Name :'),
    send(SDP,append,new(SDP1A,label)),send(SDP1A,append,Name),
    send(SDP1A,alignment, left),
    send(SDP,append,new(SDP2,label)),send(SDP2,append,'Age :'),
    send(SDP,append,new(SDP2A,label)),send(SDP2A,append,Age),
    send(SDP,append,new(SDP3,label)),send(SDP3,append,'Gender :'),
    send(SDP,append,new(SDP3A,label)),send(SDP3A,append,Gender),

    Ftemp is ((Temperature*1.8)+32),

    send(SDP,append,new(SDP4,label)),send(SDP4,append,'Temperature(F) :'),
    send(SDP,append,new(SDP4A,label)),send(SDP4A,append, Ftemp),

    (Dizzy == 'yes' -> Dizzyval is 1; Dizzyval is 0),
    (Faint == 'yes' -> Faintval is 1; Faintval is 0),
    (Blur == 'yes' -> Blurval is 1; Blurval is 0),

    Hyper is Dizzyval + Faintval + Blurval,

    send(SDP,append,new(SDP5,label)),send(SDP5,append,'Systolic Reading :'),
    send(SDP,append,new(SDP5A,label)),send(SDP5A,append,SysR),

    send(SDP,append,new(SDP6,label)),send(SDP6,append,'Diastolic Reading :'),
    send(SDP,append,new(SDP6A,label)),send(SDP6A,append,DiaR),

    send(SDP,append,new(HyperLbl,label)),


    ((Hyper = 3,SysR >= 140, DiaR >= 90 )->
    send(HyperLbl,append,'You have High Blood Pressure');

    ((Hyper >0, Hyper < 3), Faintval = 1, (SysR < 140, SysR >= 120), (DiaR > 80,DiaR =< 89) )->
    send(HyperLbl, append,'You are at risk of High Blood Pressure');

    (Hyper = 0, SysR < 120, DiaR <80) ->
    send(HyperLbl,append,'You have Normal Blood Pressure')),

    (Fever == 'yes' -> Feverval is 1; Feverval is 0),
    (Fatigue == 'yes' -> Fatigueval is 1; Fatigueval is 0),
    (Head == 'yes' -> Headval is 1; Headval is 0),
    (Sore == 'yes' -> Soreval is 1; Soreval is 0),
    (DiffB == 'yes' -> DiffBval is 1; DiffBval is 0),
    (Chest == 'yes' -> Chestval is 1; Chestval is 0),
    (Losm == 'yes' -> Losmval is 1; Losmval is 0),
    (Cough == 'yes' -> Coughval is 1; Coughval is 0),
    (Lot == 'yes' -> Lotval is 1; Lotval is 0),
    (Run == 'yes' -> Runval is 1; Runval is 0),
    (Muscle == 'yes' -> Muscleval is 1; Muscleval is 0),
    (Sneeze == 'yes' -> Sneezeval is 1; Sneezeval is 0),
    (Boc == 'yes' -> Bocval is 1; Bocval is 0),

    (Cancer == 'yes' -> Cancerval is 1; Cancerval is 0),
    (Kid == 'yes' -> Kidval is 1; Kidval is 0),
    (Tb == 'yes' -> Tbval is 1; Tbval is 0),
    (HIV == 'yes' -> HIVval is 1; HIVval is 0),
    (Dia == 'yes' -> Diaval is 1; Diaval is 0),
    (Dem == 'yes' -> Demval is 1; Demval is 0),
    (Lung == 'yes' -> Lungval is 1; Lungval is 0),
    (Stroke == 'yes' -> Strokeval is 1; Strokeval is 0),
    (Sick == 'yes' -> Sickval is 1; Sickval is 0),
    (Heart == 'yes' -> Heartval is 1; Heartval is 0),
    (Alz == 'yes' -> Alzval is 1; Alzval is 0),
    (Cys == 'yes' -> Cysval is 1; Cysval is 0),
    (Liver == 'yes' -> Liverval is 1; Liverval is 0),

    Covid_common is Feverval + Fatigueval + Coughval + Headval + Lotval,

    Underlyingval is Cancerval + Kidval + Tbval + HIVval +Diaval + Demval
    + Lungval + Strokeval + Sickval + Heartval + Alzval + Cysval + Liverval,

    % might add high temperature as a condition for not statement for regualar covid

    send(SDP,append,new(InfectionLbl,label)),
    ((Covid_common = 5, Ftemp > 100, Runval = 1,Soreval = 1, Muscleval = 1, DiffBval = 1)->
    send(InfectionLbl, append, 'You have the Delta Variant of Covid-19');

    (Covid_common = 5,Ftemp > 100, Sneezeval = 1, Soreval = 1, Runval = 1, Chestval = 1, Bocval =1,
     DiffBval = 1, Losmval = 1, Underlyingval > 0 ) ->
    send(InfectionLbl, append, 'You have the Omicron Variant of Covid-19');

    (Covid_common = 5,Ftemp > 100) ->
    send(InfectionLbl, append,'You have Covid-19');

    (Covid_common = 0,Ftemp < 100) ->
    send(InfectionLbl,append, 'You do not have Covid-19')),

    %assert to update datbase

    send(SDP,open).


save_diagnosis_python(Name,Age,Gender,Temperature,Dizzy,Faint,Blur,SysR,DiaR,Fever,Fatigue,Head,Sore,DiffB,Chest,Losm,Cough,Lot,Run,Muscle,Sneeze,Boc,Cancer,Tb,HIV,Dia,Dem,Lung,Kid,
                      Stroke,Sick,Heart,Alz,Cys,Liver):-

    nl,write('Name: '),write(Name),
    nl,write('Age: '),write(Age),
    nl,write('Gender: '),write(Gender),
    Ftemp is ((Temperature*1.8)+32),

    nl,write('Temperature(F): '), write(Ftemp),

     (Dizzy == 'yes' -> Dizzyval is 1; Dizzyval is 0),
    (Faint == 'yes' -> Faintval is 1; Faintval is 0),
    (Blur == 'yes' -> Blurval is 1; Blurval is 0),

    Hyper is Dizzyval + Faintval + Blurval,
    (   (Hyper = 3,SysR >= 140, DiaR >= 90 )->
    nl,write(Name),write(' has High Blood Pressure');

    ((Hyper >0, Hyper < 3), Faintval = 1, (SysR < 140, SysR >= 120), (DiaR > 80,DiaR =< 89))->
    nl,write(Name),write(' is risk of High Blood Pressure');

     (Hyper = 0, SysR < 120, DiaR <80) ->
    nl,write(Name),write(' has a normal Blood Pressure')),

     (Fever == 'yes' -> Feverval is 1; Feverval is 0),
    (Fatigue == 'yes' -> Fatigueval is 1; Fatigueval is 0),
    (Head == 'yes' -> Headval is 1; Headval is 0),
    (Sore == 'yes' -> Soreval is 1; Soreval is 0),
    (DiffB == 'yes' -> DiffBval is 1; DiffBval is 0),
    (Chest == 'yes' -> Chestval is 1; Chestval is 0),
    (Losm == 'yes' -> Losmval is 1; Losmval is 0),
    (Cough == 'yes' -> Coughval is 1; Coughval is 0),
    (Lot == 'yes' -> Lotval is 1; Lotval is 0),
    (Run == 'yes' -> Runval is 1; Runval is 0),
    (Muscle == 'yes' -> Muscleval is 1; Muscleval is 0),
    (Sneeze == 'yes' -> Sneezeval is 1; Sneezeval is 0),
    (Boc == 'yes' -> Bocval is 1; Bocval is 0),

    (Cancer == 'yes' -> Cancerval is 1; Cancerval is 0),
    (Kid == 'yes' -> Kidval is 1; Kidval is 0),
    (Tb == 'yes' -> Tbval is 1; Tbval is 0),
    (HIV == 'yes' -> HIVval is 1; HIVval is 0),
    (Dia == 'yes' -> Diaval is 1; Diaval is 0),
    (Dem == 'yes' -> Demval is 1; Demval is 0),
    (Lung == 'yes' -> Lungval is 1; Lungval is 0),
    (Stroke == 'yes' -> Strokeval is 1; Strokeval is 0),
    (Sick == 'yes' -> Sickval is 1; Sickval is 0),
    (Heart == 'yes' -> Heartval is 1; Heartval is 0),
    (Alz == 'yes' -> Alzval is 1; Alzval is 0),
    (Cys == 'yes' -> Cysval is 1; Cysval is 0),
    (Liver == 'yes' -> Liverval is 1; Liverval is 0),

    Covid_common is Feverval + Fatigueval + Coughval + Headval + Lotval,

    Underlyingval is Cancerval + Kidval + Tbval + HIVval +Diaval + Demval
    + Lungval + Strokeval + Sickval + Heartval + Alzval + Cysval + Liverval,

    ((Covid_common = 5, Ftemp > 100, Runval = 1,Soreval = 1, Muscleval = 1, DiffBval = 1)->
     nl,write(Name),write(' has the Delta Variant of Covid-19');

    (Covid_common = 5,Ftemp > 100, Sneezeval = 1, Soreval = 1, Runval = 1, Chestval = 1, Bocval =1,
     DiffBval = 1, Losmval = 1, Underlyingval > 0 ) ->
    nl,write(Name), write( ' has the Omicron Variant of Covid-19');

    (Covid_common = 5,Ftemp > 100) ->
     nl,write(Name),write(' has Covid-19');

    (Covid_common = 0,Ftemp < 100) ->
     nl,write(Name), write(' does not have Covid-19')).
%assert to update datbase





add_ucondition:- new(U,dialog('New Condition')),send(U,append,new(label)),
    send(U,append,new(Uconditon,text_item(underlying_Condition))),
    send(U,append,button(add,message(@prolog,add,Uconditon?selection))),
    send(U,open).

view_condition:-
       underlying(omicron,X) = write([Condition1|Condition2]).



%adds another condition to database
add(Ucondition):- underlying(omicron,Old),append(Old,[Ucondition],New),
     redefine_system_predicate('underlying'(_,_)),
       retractall(underlying(_)),
    asserta(underlying(omicron,(New))),
    another_ucondition.


another_ucondition:- new(A,dialog('Add More')),send(A,append,new(label)),
     send(A,append,new(NewA1,label)),send(NewA1,append,'Would you like to add another'),
     send(A,append,button(yes,message(@prolog,add_ucondition))),
     send(A,append,button(no,message(@prolog,close/1))),
     send(A,open).

%covid_stats:-



