%C:\Program Files\swipl\bin\swipl-win

:- use_module(library(pce)).



illness(covid).

illness_type(covid,[regular,delta,omicron]).

variant(regular,[fever,cough,fatigue,'loss of taste',headache]).
variant(delta,[cough,fatigue,headache,'runny nose','sore throat']).
variant(omicron,[fatigue,headache,sneezing,'sore throat','runny nose']).

%enter symptom severity


underlying(omicron,[stroke,tuberulosis,'sickle cell','HIV','heart conditions',diabetes,alzheimers,dementia,'cystic fibrosis','lung disease','liver disease','kidney disease']).

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
    send(V2,append,button(submit,message(@prolog,submit))),

    send(V,open).


ucondition:- new(C,dialog('Underlying Condition')),send(C,append,new(label)),

    new(C1,dialog_group('')),send(C,append, C1),
    new(C2,dialog_group('')),send(C,append, C2,below),

    send(C2,append,button(new_Underlying_Conditions,message(@prolog,add_ucondition))),
    send(C2,append,new(Lbl1a,label)),send(Lbl1a,append,''),
    send(C2,append,button(view_Underlying_Conditons,message(@prolog,add))),
    send(C1,append,new(NewCH,label)),send(NewCH,append,'This system allow you to add or view Underlying Conditions'),
    send(C1,append,new(NewCH1,label)),send(NewCH1,append,'associated with the Omicron Variant.'),

    send(C,open).

patient_diagnostic:-
    new(D,dialog('Covid-19 Diagnosis')),send(D,append,new(label)),
    send(D,append,new(Name,text_item(name))),
    send(D,append,new(Age, text_item(age))),
    send(D,append,new(Gender,text_item(gender))),

    send(D,open).

add_ucondition:- new(U,dialog('New Condition')),send(U,append,new(label)),
    send(U,append,new(Uconditon,text_item(underlying_Condition))),
    send(U,append,button(add,message(@prolog,add,Uconditon))),
    send(U,open).


add(Ucondition):- underlying(Old),append(Old,[Ucondition],New),
    retractall(underlying(_)),assert(underlying(New)),
    another_ucondition.


another_ucondition:- new(A,dialog('Add More')),send(A,append,new(label)),
     send(A,append,new(NewA1,label)),send(NewA1,append,'Would you like to add another'),
     send(A,append,button(yes,message(@prolog,add_ucondition))),
     send(A,append,button(no,message(@prolog,close/1))),
     send(A,open).




