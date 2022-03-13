%C:\Program Files\swipl\bin\swipl-win

:- use_module(library(pce)).

illness(covid).

illness_type(covid,regular).
illness_type(covid,delta).
illnes_type(covid,omicron).

covid_symptoms(regular,fever).
covid_symptoms(regular,cough).
covid_symptoms(regular,fatigue).
covid_symptoms(regular,'loss of taste').
covid_symptoms(regular,headache).

covid_symptoms(delta,cough).
covid_symptoms(delta,fatigue).
covid_symptoms(delta,headache).
covid_symptoms(delta,'runny nose').
covid_symptoms(delta,'sore throat').

covid_symptoms(omicron,fatigue).
covid_symptoms(omicron,headache).
covid_symptoms(omicron,sneezing).
covid_symptoms(omicron,'sore throat').
covid_symptoms(omicron,'runny nose').

underlying(omicron,cancer).
underlying(omicron,'chronic kidney disease').
underlying(omicron,'chronic liver disease').
underlying(omicron,'chronic lung disease').
underlying(omicron,'cystic fibrosis').
underlying(omicron,dementia).
underlying(omicron,alzheimers).
underlying(omicron,diabetes).
underlying(omicron,'heart conditions').
underlying(omicron,'HIV').
underlying(omicron,'sickle cell').
underlying(omicron,stroke).
underlying(omicron,tuberculosis).


menu:-new(M,dialog('COVID-19 Diagnosis System - Main Menu')),
    send(M,append,new(Lblfill,label)),send(Lblfill,append,''),
    new(H1, dialog_group('')),
    new(H2, dialog_group('')),
    send(M,append,H1),
    send(M,append,H2,below),

    send(H2,append,button(more_symptoms, message(@prolog,addfact))),
    send(H1,append,new(Label1,label)),send(Label1,append,'Welcome to Covid-19 Diagnosis System of the Ministry of Health.'),

    send(M,open).




