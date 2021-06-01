# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 20:56:44 2021

@author: Naima, Noémie
"""
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
from dash.dependencies import Input, Output
import dash_table
from datetime import datetime
import numpy as np
import dash_bootstrap_components as dbc
import plotly.express as px



app = dash.Dash(__name__,external_stylesheets=[dbc.themes.BOOTSTRAP])


#####################################DATA########################################

## Données monde général
covid_monde_url = ("https://covid19.who.int/WHO-COVID-19-global-data.csv")
df_monde = pd.read_csv(covid_monde_url, sep=",")
df_monde['Date_reported'] = pd.to_datetime(df_monde['Date_reported'], format='%Y-%m-%d')

## Données vaccination dans le monde
covid_monde_vaccination_url = ("https://covid19.who.int/who-data/vaccination-data.csv")
df_monde_vacc = pd.read_csv(covid_monde_vaccination_url, sep=",")
df_monde_vacc['DATE_UPDATED'] = pd.to_datetime(df_monde_vacc['DATE_UPDATED'],format='%Y-%m-%d')

covid_url = ("https://www.data.gouv.fr/fr/datasets/r/900da9b0-8987-4ba7-b117-7aea0e53f530")
df = pd.read_csv(covid_url, sep=";")

## Données hospitalières françaises
covid_france_hosp_url = ("https://www.data.gouv.fr/fr/datasets/r/6fadff46-9efd-4c53-942a-54aca783c30c")
covid_france_hosp = pd.read_csv(covid_france_hosp_url, sep=";")
covid_france_hosp['date_hosp'] = pd.to_datetime(covid_france_hosp['jour'])

## Données générales françaises
covid_france_general_url = ("https://www.data.gouv.fr/fr/datasets/r/63352e38-d353-4b54-bfd1-f1b3ee1cabd7")
covid_france_general = pd.read_csv(covid_france_general_url, sep=";")
covid_france_general['date_fr'] = pd.to_datetime(covid_france_general['jour'])
covid_france_general_tot = covid_france_general[covid_france_general.sexe == 0]

## Données de vaccination en France 
vaccination_fr_url =("https://www.data.gouv.fr/fr/datasets/r/b8d4eb4c-d0ae-4af6-bb23-0e39f70262bd")
vaccination_fr = pd.read_csv(vaccination_fr_url, sep=";")
vaccination_fr['date_vacc'] = pd.to_datetime(vaccination_fr['jour'])

## Données des graphiques de réanimation
# Graphique en fonction du temps, du sexe et du département

covid_france_rea_tps_sexe_url = (
        "https://www.data.gouv.fr/fr/datasets/r/63352e38-d353-4b54-bfd1-f1b3ee1cabd7"
        )
covid_france_rea_tps_sexe = pd.read_csv(covid_france_rea_tps_sexe_url, sep=";")
covid_france_rea_tps_sexe['date']=pd.to_datetime(covid_france_rea_tps_sexe['jour'])

# Graphique en fonction de l'âge et de la région

covid_france_rea_age_url = (
        "https://www.data.gouv.fr/fr/datasets/r/08c18e08-6780-452d-9b8c-ae244ad529b3"
        )
covid_france_rea_age = pd.read_csv(covid_france_rea_age_url, sep=";")
covid_france_rea_age['date']=pd.to_datetime(covid_france_rea_age['jour'])

## Données des graphiques de vaccination 
#Graph en fonction du temps
covid_france_vaccination_url = (
        "https://www.data.gouv.fr/fr/datasets/r/900da9b0-8987-4ba7-b117-7aea0e53f530"
        )
covid_france_vaccination = pd.read_csv(covid_france_vaccination_url, sep=";")
covid_france_vaccination['date'] = pd.to_datetime(covid_france_vaccination['jour'])

##Données des graphiques des décès  
# Graphique en fonction du temps, du sexe et du département 
covid_france_dc_tps_sexe_url = (    
        "https://www.data.gouv.fr/fr/datasets/r/63352e38-d353-4b54-bfd1-f1b3ee1cabd7"   
        )   
covid_france_dc_tps_sexe = pd.read_csv(covid_france_dc_tps_sexe_url, sep=";")   
covid_france_dc_tps_sexe['date']=pd.to_datetime(covid_france_dc_tps_sexe['jour'])   

# Graphique en fonction de la classe d'âge et de la région  
covid_france_dc_age_url = ( 
        "https://www.data.gouv.fr/fr/datasets/r/08c18e08-6780-452d-9b8c-ae244ad529b3"   
        )   
covid_france_dc_age = pd.read_csv(covid_france_dc_age_url, sep=";") 
covid_france_dc_age['date']=pd.to_datetime(covid_france_dc_age['jour'])

#Graph en fonction de la classe d'âge
covid_france_vacc_age_url = (
        "https://www.data.gouv.fr/fr/datasets/r/54dd5f8d-1e2e-4ccb-8fb8-eac68245befd"
        )
covid_france_vacc_age = pd.read_csv(covid_france_vacc_age_url, sep=";")
covid_france_vacc_age['clage_vacsi'] = covid_france_vacc_age['clage_vacsi'].astype(str)

#Graph en fonction de la région
covid_france_vacc_reg_url = (
        "https://www.data.gouv.fr/fr/datasets/r/735b0df8-51b4-4dd2-8a2d-8e46d77d60d8"
        )
covid_france_vacc_reg = pd.read_csv(covid_france_vacc_reg_url, sep=";")
covid_france_vacc_reg['reg'] = covid_france_vacc_reg['reg'].astype(str)



#####################################LAYOUT###############################################

# styling the tabs
tabs_styles = {
    'height': '44px'
}
tab_style = {
    'borderBottom': '1px solid #d6d6d6',
    'padding': '6px',
    'fontWeight': 'bold'
}

tab_selected_style = {
    'borderTop': '1px solid #d6d6d6',
    'borderBottom': '1px solid #d6d6d6',
    'backgroundColor': '#1175ff',
    'color': 'white',
    'padding': '6px'
}

# Creating the Cards
def create_card(title, content, date):
    card=[
        dbc.CardHeader([html.H2(title)]),
        dbc.CardBody(
            [   
                html.H3(content, className="card-title"),
                html.H5(date, className="card-text"),
            ]
        ),
        ]
    return(card)

#Données monde 
sum_cases_monde = df_monde['New_cases'].sum() 
sum_deaths = df_monde['New_deaths'].sum()
sum_vaccination = df_monde_vacc['TOTAL_VACCINATIONS'].sum()
date_recente = max(df_monde['Date_reported'])
covid_monde_last_day = df_monde[df_monde.Date_reported == date_recente]
sum_cases_last_day = covid_monde_last_day['New_cases'].sum()
sum_deaths_last_day = covid_monde_last_day['New_deaths'].sum()

date_recente_str = date_recente.strftime('%Y-%m-%d')

#Indicateurs du monde
card1=create_card("Nombre accumulé de cas", sum_cases_monde, date_recente_str)
card2=create_card("Nombre accumulé de décès", sum_deaths, date_recente_str)
card3=create_card("Nombre total de vaccinations", sum_vaccination,date_recente_str)
card4=create_card("Nombre total de nouveaux cas", sum_cases_last_day,date_recente_str)
card5=create_card("Nombre total de nouveaux décès", sum_deaths_last_day,date_recente_str)

cards = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(dbc.Card(card1, color="#AED6F1", inverse=True)),
                dbc.Col(dbc.Card(card2, color="#85C1E9", inverse=True)),
                dbc.Col(dbc.Card(card3, color="#5DADE2", inverse=True)),
                dbc.Col(dbc.Card(card4, color="#3498DB", inverse=True)),
                dbc.Col(dbc.Card(card5, color="#2874A6", inverse=True)),
            ],
            className="mb-2",
        ),
    ]
)

# Données France 

total_deces_hosp = covid_france_hosp['incid_dc'].sum()###
covid_france_general_total = covid_france_general[covid_france_general.jour == max(covid_france_general['jour'])]
total_deces_general = covid_france_general_total['dc'].sum()###
total_rea = covid_france_hosp['incid_rea'].sum()###
total_hosp = covid_france_hosp['incid_hosp'].sum()### 
dernier_jour_hosp = max(covid_france_hosp['date_hosp'])
dernier_jour_gen = max(covid_france_general['date_fr'])
covid_france_dernier_jour_hosp = covid_france_hosp[covid_france_hosp.date_hosp == dernier_jour_hosp]
nombre_deces_jour = covid_france_dernier_jour_hosp['incid_dc'].sum()
nombre_rea_jour = covid_france_dernier_jour_hosp['incid_rea'].sum()
nombre_hosp_jour = covid_france_dernier_jour_hosp['incid_hosp'].sum()

dernier_jour_hosp_str = dernier_jour_hosp.strftime('%Y-%m-%d')
dernier_jour_gen_str = dernier_jour_gen.strftime('%Y-%m-%d')

# Données réanimations 

bbd_homme = covid_france_general_total[covid_france_general_total.sexe == 1]
bbd_femme = covid_france_general_total[covid_france_general_total.sexe == 2]

rea_homme = bbd_homme['rea'].sum()
rea_femme = bbd_femme['rea'].sum()

# Données décès 

deces_homme = bbd_homme['dc'].sum()
deces_femme = bbd_femme['dc'].sum()

# Données vaccination 
tout_vaccin = vaccination_fr[vaccination_fr.vaccin == 0]
total_vaccination_fr = tout_vaccin['n_tot_dose2'].sum()

pfizer = vaccination_fr[vaccination_fr.vaccin == 1]
moderna = vaccination_fr[vaccination_fr.vaccin == 2]
astra = vaccination_fr[vaccination_fr.vaccin == 3]
janssen = vaccination_fr[vaccination_fr.vaccin == 4]

dose1_pfizer = pfizer['n_tot_dose1'].sum()
dose1_moderna = moderna['n_tot_dose1'].sum()
dose1_astra = astra['n_tot_dose1'].sum()
dose1_Janssen = janssen['n_tot_dose1'].sum()

dose2_pfizer = pfizer['n_tot_dose2'].sum()
dose2_moderna = moderna['n_tot_dose2'].sum()
dose2_astra = astra['n_tot_dose2'].sum()
dose2_Janssen = janssen['n_tot_dose2'].sum()

date_vacc = max(vaccination_fr['date_vacc'])
mise_a_jour_vacc = date_vacc.strftime('%Y-%m-%d')

# Indicateurs France

card_fr1=create_card("Nombre total de décès", f'{total_deces_general} dont {total_deces_hosp} en milieu hospitalier', dernier_jour_gen_str)
card_fr2=create_card("Nombre de réanimations", total_rea,dernier_jour_hosp_str)
card_fr3=create_card("Nombre des hospitalisations", total_hosp,dernier_jour_hosp_str)
card_fr4=create_card("Nombre de vaccinations complètes",total_vaccination_fr, mise_a_jour_vacc)

cards_fr = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(dbc.Card(card_fr1, color="#C39BD3", inverse=True)),
                dbc.Col(dbc.Card(card_fr2, color="#AF7AC5", inverse=True)),
                dbc.Col(dbc.Card(card_fr3, color="#9B59B6", inverse=True)),
                dbc.Col(dbc.Card(card_fr4, color="#7D3C98", inverse=True))
            ],
            className="mb-2",
        ),
    ]
)

# Indicateurs réanimations

card_rea1=create_card("Nombre de réanimations au total", total_rea, dernier_jour_hosp_str)
card_rea2=create_card("Nombre de réanimations actuelles chez les hommes", rea_homme,dernier_jour_gen_str)
card_rea3=create_card("Nombre de réanimations actuelles chez les femmes", rea_femme,dernier_jour_gen_str)
card_rea4=create_card("Nombre de nouvelles réanimations", nombre_rea_jour,dernier_jour_hosp_str)

cards_rea = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(dbc.Card(card_rea1, color="#ffb732", inverse=True)),
                dbc.Col(dbc.Card(card_rea2, color="#ffae19", inverse=True)),
                dbc.Col(dbc.Card(card_rea3, color="#ffa500", inverse=True)),
                dbc.Col(dbc.Card(card_rea4, color="#e59400", inverse=True)),

            ],
            className="mb-2",
        ),
    ]
)


# Indicateurs décès

card_dc1=create_card("Nombre de décès", f'{total_deces_general} dont {total_deces_hosp} en milieu hospitalier', dernier_jour_hosp_str)
card_dc2=create_card("Nombre de décès chez les hommes en milieu hospitalier", deces_homme,dernier_jour_gen_str)
card_dc3=create_card("Nombre de décès chez les femmes en milieu hospitalier", deces_femme,dernier_jour_gen_str)
card_dc4=create_card("Nombre de décès du jour", nombre_deces_jour,dernier_jour_hosp_str)

cards_dc = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(dbc.Card(card_dc1, color="#EC7063", inverse=True)),
                dbc.Col(dbc.Card(card_dc2, color="#E74C3C", inverse=True)),
                dbc.Col(dbc.Card(card_dc3, color="#CB4335", inverse=True)),
                dbc.Col(dbc.Card(card_dc4, color="#B03A2E", inverse=True)),
            ],
            className="mb-2",
        ),
    ]
)


#Indicateurs vaccination

card_vacc1=create_card("Nombre de premières doses du vaccin pfizer", dose1_pfizer, mise_a_jour_vacc)
card_vacc2=create_card("Nombre de premières doses du vaccin moderna", dose1_moderna,mise_a_jour_vacc)
card_vacc3=create_card("Nombre de premières doses du vaccin AstraZeneca", dose1_astra,mise_a_jour_vacc)
card_vacc4=create_card("Nombre de premières doses du vaccin Janssen", dose1_Janssen,mise_a_jour_vacc)
card_vacc5=create_card("Nombre de secondes doses du vaccin pfizer", dose2_pfizer, mise_a_jour_vacc)
card_vacc6=create_card("Nombre de secondes doses du vaccin moderna", dose2_moderna,mise_a_jour_vacc)
card_vacc7=create_card("Nombre de secondes doses du vaccin AstraZeneca", dose2_astra,mise_a_jour_vacc)
card_vacc8=create_card("Nombre de secondes doses du vaccin Janssen", dose2_Janssen,mise_a_jour_vacc)

cards_vacc = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(dbc.Card(card_vacc1, color="#ABEBC6", inverse=True)),
                dbc.Col(dbc.Card(card_vacc2, color="#58D68D", inverse=True)),
                dbc.Col(dbc.Card(card_vacc3, color="#82E0AA", inverse=True)),
                dbc.Col(dbc.Card(card_vacc4, color="#2ECC71", inverse=True)),
            ],
            className="mb-2",
        ),
        dbc.Row(
            [
                dbc.Col(dbc.Card(card_vacc5, color="#ABEBC6", inverse=True)),
                dbc.Col(dbc.Card(card_vacc6, color="#58D68D", inverse=True)),
                dbc.Col(dbc.Card(card_vacc7, color="#82E0AA", inverse=True)),
                dbc.Col(dbc.Card(card_vacc8, color="#2ECC71", inverse=True)),
            ],
            className="mb-2",
        ),
    ]
)


############################################## Visualisations####################################################################

# Monde visualisations:
## New cases graphique:
monde_cases_time = df_monde[['Date_reported','New_cases']].groupby('Date_reported', as_index=False).sum()
def update_graph_monde(title):
    fig_time = px.line(monde_cases_time, x=monde_cases_time['Date_reported'], y=monde_cases_time['New_cases'], labels={"Date_reported":"Date","New_cases":"Nombre de nouveaux cas"}, title=title)
    fig_time.update_xaxes(rangeslider_visible=True)
    return fig_time
    
card_graph_world_time = dbc.Card(
    dcc.Graph(id='my-graph-world_time', figure=update_graph_monde("Evolution du nombre de nouvaux cas dans le monde")), body=True, color ='#f2ffff',
    )
card_graph_world1 = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(card_graph_world_time),
            ],
            className='mb-6',
        ),
    ]
)
     
     
monde_cases = df_monde[['New_cases','WHO_region']].groupby('WHO_region', as_index=False).sum()
def update_graph_monde3(title):
    fig_time = px.bar(monde_cases, x=monde_cases['WHO_region'], y=monde_cases['New_cases'], color=monde_cases['WHO_region'],  labels={"WHO_region":"Region du monde","New_cases":"Nombre de nouveaux cas"},title=title)
    return fig_time
    
card_graph_world_time3 = dbc.Card(
    dcc.Graph(id='my-graph-world_time3', figure=update_graph_monde3("Nombre total de cas par région dans le monde")), body=True, color ='#f2ffff',
    )
card_graph_world3 = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(card_graph_world_time3),
            ],
            className='mb-6',
        ),
    ]
)
## New deaths graphics:
      
monde_deaths_time = df_monde[['Date_reported','New_deaths']].groupby('Date_reported', as_index=False).sum()
def update_graph_monde2(title):
    fig_time = px.line(monde_deaths_time, x=monde_deaths_time['Date_reported'], y=monde_deaths_time['New_deaths'],  labels={"Date_reported":"Date","New_Deaths":"Nombre de nouveaux décès"},title=title)
    fig_time.update_xaxes(rangeslider_visible=True)
    return fig_time
    
card_graph_world_time2 = dbc.Card(
    dcc.Graph(id='my-graph-world_time2', figure=update_graph_monde2("Evolution du nombre de décès dans le monde")), body=True, color ='#f2ffff',
    )
card_graph_world2 = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(card_graph_world_time2),
            ],
            className='mb-6',
        ),
    ]
)
   

monde_deaths = df_monde[['New_deaths','WHO_region']].groupby('WHO_region', as_index=False).sum()
def update_graph_monde5(title):
    fig_time = px.bar(monde_deaths, x=monde_deaths['WHO_region'], y=monde_deaths['New_deaths'], color=monde_deaths['WHO_region'],  labels={"WHO_region":"region du monde","New_deaths":"Nombre de nouveaux décès"}, title=title)
    return fig_time
    
card_graph_world_time5 = dbc.Card(
    dcc.Graph(id='my-graph-world_time5', figure=update_graph_monde5("Nombre total de décès par région dans le monde")), body=True, color ='#f2ffff',
    )
card_graph_world5 = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(card_graph_world_time5),
            ],
            className='mb-6',
        ),
    ]
)
  
# vaccination dans le monde:
        
def update_graph_monde4(title):
    fig_time = px.bar(df_monde_vacc, x='COUNTRY', y='TOTAL_VACCINATIONS', color='WHO_REGION',  labels={"COUNTRY":"Pays","TOTAL_VACCINATIONS":"Nombre total de personnes vaccinées"}, title=title)
    return fig_time
    
card_graph_world_time4 = dbc.Card(
    dcc.Graph(id='my-graph-world_time4', figure=update_graph_monde4("Population vaccinée dans le monde")), body=True, color ='#f2ffff',
    )

card_graph_world4 = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(card_graph_world_time4),
            ],
            className='mb-6',
        ),
    ]
)      


## Graphiques réanimations

# Graphique réanimation en fonction du temps
covid_france_dc_tot = covid_france_rea_tps_sexe[covid_france_rea_tps_sexe.sexe == 0]    
dernier_jour_rea_age = max(covid_france_rea_tps_sexe["date"])   
covid_france_dernier_jour_rea = covid_france_rea_tps_sexe[covid_france_rea_tps_sexe.date == dernier_jour_rea_age]
evol_rea = covid_france_rea_tps_sexe[['date','rea']].groupby('date', as_index=False).sum()

def update_graph_rea_tps(title):
    fig_tps = px.line(evol_rea, x=evol_rea['date'], y=evol_rea['rea'], title=title, labels={"date":"Date","rea":"Nombre de réanimations"})

    return fig_tps

card_graph_rea_tps = dbc.Card(
    dcc.Graph(id='my-graph-rea-tps', figure=update_graph_rea_tps("Evolution du nombre total de réanimations")), body=True, color ='#FDEBD0',
    )
card_graph_rea_tps1 = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(card_graph_rea_tps),
            ],
            className='mb-6',
        ),
    ]
)


# Graphique réanimation en fonction de la classe d'âge

age_rea = covid_france_rea_age[['cl_age90','rea']].groupby('cl_age90', as_index=False).sum()
age_rea['cl_age90_str'] = ["Toutes","9-19","19-29","29-39","39-49","49-59","59-69","69-79","79-89","89-90","+ de 90"]

def update_graph_rea_age(title):
    fig_age = px.bar(age_rea, x=age_rea['cl_age90_str'], y=age_rea['rea'], title=title, text=age_rea['rea'],labels={"cl_age90_str":"Classe d'âge","rea":"Nombre de réanimations"})
    fig_age.update_traces(textposition='outside')
    return fig_age

card_graph_rea_age = dbc.Card(
    dcc.Graph(id='my-graph-rea-age', figure=update_graph_rea_age("Nombre total de réanimation en fonction de la classe d'âge")), body=True, color ='#FAD7A0',
    )

# Graphique réanimation en fonction du sexe
dernier_jour_rea = max(covid_france_rea_age["date"])
covid_france_dernier_jour_age_rea = covid_france_rea_age[covid_france_rea_age.date == dernier_jour_rea] 

age_rea = covid_france_dernier_jour_age_rea[['cl_age90','rea']].groupby('cl_age90', as_index=False).sum()
sexe_rea = covid_france_rea_tps_sexe[['sexe','rea']].groupby('sexe', as_index=False).sum()
sexe_rea['sexe_str'] = ["Les deux","Hommes","Femmes"]

def update_graph_rea_sexe(title):
    fig_sexe = px.bar(sexe_rea, x=sexe_rea['sexe_str'], y=sexe_rea['rea'], title=title, text=sexe_rea['rea'],labels={"sexe_str":"Sexe","rea":"Nombre de réanimations"})
    fig_sexe.update_traces(textposition='outside')
    return fig_sexe

card_graph_rea_sexe = dbc.Card(
    dcc.Graph(id='my-graph-rea-sexe', figure=update_graph_rea_sexe("Nombre total de réanimation en fonction du sexe")), body=True, color ='#FAD7A0',
    )
card_graph_rea_sexe1 = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(card_graph_rea_sexe),
                dbc.Col(card_graph_rea_age)
            ],
            className='mb-6',
        ),
    ]
)


# Graphique réanimation en fonction de la région

reg_rea = covid_france_dernier_jour_age_rea[['reg','rea']].groupby('reg', as_index=False).sum()
reg_rea['reg_str']= ["Guadeloupe","Martinique","Guyane","Reunion","Mayotte","Île-de-France",
"Centre-Val de Loire","Bourgogne","Normandie","Hauts-de-France","Grand-Est","Pays de la Loire",
"Bretagne","Nouvelle Aquitaine","Occitanie","Auvergne","PACA","Corse"]

def update_graph_rea_reg(title):
    fig_reg = px.bar(reg_rea, x=reg_rea['reg_str'], y=reg_rea['rea'], title=title, text=reg_rea['rea'],labels={"reg_str":"Régions","rea":"Nombre de réanimations"})
    fig_reg.update_traces(textposition='outside')
    return fig_reg

card_graph_rea_reg = dbc.Card(
    dcc.Graph(id='my-graph-rea-reg', figure=update_graph_rea_reg("Nombre total de réanimation en fonction de la région")), body=True, color ='#F8C471',
    )
card_graph_rea_reg1 = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(card_graph_rea_reg),
            ],
            className='mb-6',
        ),
    ]
)
# Graphique réanimation en fonction du département

dep_rea = covid_france_dernier_jour_rea[['dep','rea']].groupby('dep', as_index=False).sum()
dep_rea_new = dep_rea.drop(dep_rea.index[96:101])
dep_rea_new['dep_str'] = ["01","02","03","04","05","06","07","08","09","10","11","12","13",
"14","15","16","17","18","19","21","22","23","24","25","26","27","28","29","2A","2B","30","31",
"32","33","34","35","36","37","38","39","40","41","42","43","44","45","46","47","48","49",
"50","51","52","53","54","55","56","57","58","59","60","61","62","63","64","65","66","67",
"68","69","70","71","72","73","74","75","76","77","78","79","80","81","82","83","84","85",
"86","87","88","89","90","91","92","93","94","95"]

def update_graph_rea_dep(title):
    fig_dep = px.bar(dep_rea_new, x=dep_rea_new['dep_str'], y=dep_rea_new['rea'], title=title, text=dep_rea_new['rea'], labels={"dep_str":"Départements","rea":"Nombre de réanimations"})
    fig_dep.update_traces(textposition='outside')
    return fig_dep

card_graph_rea_dep = dbc.Card(
    dcc.Graph(id='my-graph-rea-dep', figure=update_graph_rea_dep("Nombre total de réanimation en fonction du département")), body=True, color ='#F5B041',
    )
card_graph_rea_dep1 = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(card_graph_rea_dep),
            ],
            className='mb-6',
        ),
    ]
)

## Graphique des décès  
# Graphique des décès en fonction du temps  
covid_france_dc_tot = covid_france_dc_tps_sexe[covid_france_dc_tps_sexe.sexe == 0]  
dernier_jour_dc1 = max(covid_france_dc_tps_sexe["date"])    
covid_france_dernier_jour_dc1 = covid_france_dc_tps_sexe[covid_france_dc_tps_sexe.date == dernier_jour_dc1] 

evol_dc = covid_france_dc_tot[['date','dc']].groupby('date', as_index=False).sum()  
def update_graph_dc_tps(title): 
    fig_tps_dc = px.line(evol_dc, x=evol_dc['date'], y=evol_dc['dc'], title=title, labels={"date":"Date","dc":"Nombre de décès"})   

    return fig_tps_dc   

card_graph_dc_tps = dbc.Card(   
    dcc.Graph(id='my-graph-dc-tps', figure=update_graph_dc_tps("Evolution du nombre total de décès")), body=True, color ='#EC7063', 
    )   
card_graph_dc_tps1 = html.Div(  
    [   
        dbc.Row(    
            [   
                dbc.Col(card_graph_dc_tps), 
            ],  
            className='mb-6',   
        ),  
    ]   
)   

# Graphique des décès en fonction de la classe d'âge    
dernier_jour_dc = max(covid_france_dc_age["date"])  
covid_france_dernier_jour_dc = covid_france_dc_age[covid_france_dc_age.date == dernier_jour_dc] 

age_dc = covid_france_dernier_jour_dc[['cl_age90','dc']].groupby('cl_age90', as_index=False).sum()  
age_dc['cl_age90'] = age_dc['cl_age90'].astype(str) 
age_dc['cl_age90_str'] = ["Toutes","9-19","19-29","29-39","39-49","49-59","59-69","69-79","79-89","89-90","+ de 90"]    

def update_graph_dc_age(title): 
    fig_age_dc = px.bar(age_dc, x=age_dc['cl_age90_str'], y=age_dc['dc'], title=title, text=age_dc['dc'], labels={"cl_age90_str":"Classe d'âge","dc":"Nombre de décès"})    
    fig_age_dc.update_traces(textposition='outside')    
    return fig_age_dc   

card_graph_dc_age = dbc.Card(   
    dcc.Graph(id='my-graph-dc-age', figure=update_graph_dc_age("Nombre total de décès en fonction de la classe d'âge")), body=True, color ='#E74C3C',   
    )   

# Graphique des décès en fonction du sexe   
sexe_dc = covid_france_dernier_jour_dc1[['sexe','dc']].groupby('sexe', as_index=False).sum()    
sexe_dc['sexe_str'] = ["Les deux","Hommes","Femmes"]    

def update_graph_dc_sexe(title):    
    fig_dc_sexe = px.bar(sexe_dc, x=sexe_dc['sexe_str'], y=sexe_dc['dc'], title=title, text=sexe_dc['dc'], labels={"sexe_str":"Sexe","dc":"Nombre de décès"})   
    fig_dc_sexe.update_traces(textposition='outside')   
    return fig_dc_sexe  

card_graph_dc_sexe = dbc.Card(  
    dcc.Graph(id='my-graph-dc-sexe', figure=update_graph_dc_sexe("Nombre total de décès en fonction du sexe")), body=True, color ='#E74C3C',
    )
card_graph_dc_sexe1 = html.Div( 
    [   
        dbc.Row(    
            [   
                dbc.Col(card_graph_dc_sexe),    
                dbc.Col(card_graph_dc_age)  
            ],  
            className='mb-6',   
        ),  
    ]   
)   

# Graphique des décès en fonction de la région  
reg_dc = covid_france_dernier_jour_dc[['reg','dc']].groupby('reg', as_index=False).sum()    
reg_dc['reg_str']= ["Guadeloupe","Martinique","Guyane","Reunion","Mayotte","Île-de-France", 
"Centre-Val de Loire","Bourgogne","Normandie","Hauts-de-France","Grand-Est","Pays de la Loire", 
"Bretagne","Nouvelle Aquitaine","Occitanie","Auvergne","PACA","Corse"]  

def update_graph_dc_reg(title): 
    fig_dc_reg = px.bar(reg_dc, x=reg_dc['reg_str'], y=reg_dc['dc'], title=title, text=reg_dc['dc'],labels={"reg_str":"Régions","dc":"Nombre de décès"})    
    fig_dc_reg.update_traces(textposition='outside')    
    return fig_dc_reg   

card_graph_dc_reg = dbc.Card(   
    dcc.Graph(id='my-graph-dc-reg', figure=update_graph_dc_reg("Nombre total de décès en fonction de la région")), body=True, color ='#CB4335', 
    )   
card_graph_dc_reg1 = html.Div(  
    [   
        dbc.Row(    
            [   
                dbc.Col(card_graph_dc_reg), 
            ],  
            className='mb-6',   
        ),  
    ]   
)   

# Graphique des décès en fonction du département    
dep_dc = covid_france_dernier_jour_dc1[['dep','dc']].groupby('dep', as_index=False).sum()   
dep_dc_new = dep_dc.drop(dep_dc.index[96:101])  
dep_dc_new['dep_str'] = ["01","02","03","04","05","06","07","08","09","10","11","12","13",  
"14","15","16","17","18","19","21","22","23","24","25","26","27","28","29","2A","2B","30","31", 
"32","33","34","35","36","37","38","39","40","41","42","43","44","45","46","47","48","49",  
"50","51","52","53","54","55","56","57","58","59","60","61","62","63","64","65","66","67",  
"68","69","70","71","72","73","74","75","76","77","78","79","80","81","82","83","84","85",  
"86","87","88","89","90","91","92","93","94","95"]  

def update_graph_dc_dep(title): 
    fig_dep_dc = px.bar(dep_dc_new, x=dep_dc_new['dep_str'], y=dep_dc_new['dc'], title=title, text=dep_dc_new['dc'],labels={"dep_str":"Départements","dc":"Nombre de décès"})   
    fig_dep_dc.update_traces(textposition='outside')    
    return fig_dep_dc   

card_graph_dc_dep = dbc.Card(   
    dcc.Graph(id='my-graph-dc-dep', figure=update_graph_dc_dep("Nombre total de décès en fonction du département")), body=True, color ='#B03A2E',   
    )   
card_graph_dc_dep1 = html.Div(  
    [   
        dbc.Row(    
            [   
                dbc.Col(card_graph_dc_dep), 
            ],  
            className='mb-6',   
        ),  
    ]   
)


#Graphiques vaccinations dose
evol = covid_france_vaccination[['date','n_dose1']].groupby('date', as_index=False).sum()

def update_graph_dose1(title):
    fig1 = px.line(evol, x=evol['date'], y=evol['n_dose1'], title=title,labels={"date":"Date","n_dose1":"Nombre de vaccinations Dose1"})

    return fig1

card_graph_dose = dbc.Card(
    dcc.Graph(id='my-graph-dose', figure=update_graph_dose1("Nombre de vaccinations par la dose 1 chaque jour")), body=True, color="#ABEBC6",
    )

evol2 = covid_france_vaccination[['date','n_dose2']].groupby('date', as_index=False).sum()

def update_graph_dose2(title):
    fig2 = px.line(evol2, x=evol2['date'], y=evol2['n_dose2'],title=title,labels={"date":"Date","n_dose2":"Nombre de vaccinations Dose 2"})

    return fig2

card_graph_dose2 = dbc.Card(
    dcc.Graph(id='my-graph-dose2', figure=update_graph_dose2("Nombre de vaccinations par la dose 2 chaque jour")), body=True, color="#58D68D",
    )

card_graph_dose1 = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(card_graph_dose),
                dbc.Col(card_graph_dose2),
            ],
            className='mb-6',
        ),
    ]
)

#Graphique vaccinations doses cumulées

evol_cum = covid_france_vaccination[['date','n_cum_dose1']].groupby('date', as_index=False).sum()

def update_graph_dose_cum1(title):
    fig3 = px.line(evol_cum, x=evol_cum['date'], y=evol_cum['n_cum_dose1'], title=title, labels={"date":"Date","n_cum_dose1":"Nombre de vaccinations Dose1"})

    return fig3

card_graph_dose_cum1 = dbc.Card(
    dcc.Graph(id='my-graph-dose-cum-1', figure=update_graph_dose_cum1("Evolution du nombre de vaccinations par la dose 1")), body=True, color="#ABEBC6")

evol_cum2 = covid_france_vaccination[['date','n_cum_dose2']].groupby('date', as_index=False).sum()

def update_graph_dose_cum1(title):
    fig4 = px.line(evol_cum2, x=evol_cum2['date'], y=evol_cum2['n_cum_dose2'], title=title,labels={"date":"Date","n_cum_dose2":"Nombre de vaccinations Dose 2"})

    return fig4

card_graph_dose_cum2 = dbc.Card(
    dcc.Graph(id='my-graph-dose-cum-2', figure=update_graph_dose_cum1("Evolution du nombre de vaccinations par la dose 2")), body=True, color="#58D68D")    

card_graph_dose_cum = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(card_graph_dose_cum1),
                dbc.Col(card_graph_dose_cum2),
            ],
            className='mb-6',
        ),
    ]
)

# Graphique vaccinations classe d'âge
evol_age = covid_france_vacc_age[['clage_vacsi','n_complet']].groupby('clage_vacsi', as_index=False).sum()
evol_age['classe_age'] = ['Toutes','24-29','29-39','39-49','49-59','59-64','64-69','69-74','74-79','79-80','+ de 80']

def update_graph_age(title):
    fig = px.bar(evol_age, x=evol_age['classe_age'], y=evol_age['n_complet'], title=title, labels={"classe_age":"Classe d'âge","n_complet":"Nombre de vaccinations complètes"})

    return fig

card_graph_age = dbc.Card(
        dcc.Graph(id='my-graph',figure=update_graph_age("Nombre de vaccinations en fonction des classes d'âge")), body=True, color="#82E0AA",
        )

card_graph_age1 = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(card_graph_age),
            ],
            className='mb-6',
        ),
    ]
)

# Graphique régions

evol_reg = covid_france_vacc_reg[['reg','n_complet']].groupby('reg', as_index=False).sum()
evol_reg['region'] = ['Guadeloupe','Île-de-France','Martinique','Centre-Val de Loire','Bourgogne',
'Normandie','Guyane','Hauts-de-France','Réunion','Grand-Est','Saint-Pierre et Miquelon','Pays de la Loire',
'Bretagne','Mayotte','Saint-Barthélemy','Nouvelle Aquitaine','Occitanie','Saint-Martin','Auvergne','PACA','Corse']

def update_graph_reg(title):
    fig5 = px.bar(evol_reg, x=evol_reg['region'],y=evol_reg['n_complet'], title=title, text=evol_reg['n_complet'], labels={"region":"Région","n_complet":"Nombre de vaccinations complètes"})
    fig5.update_traces(textposition='outside')

    return fig5

card_graph_reg = dbc.Card(
    dcc.Graph(id='my-graph-reg', figure=update_graph_reg("Nombre de vaccinations en fonctions des régions")), body=True, color="#2ECC71")

card_graph_reg1 = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(card_graph_reg),
            ],
            className='mb-6',
        ),
    ]
)

all_dep = covid_france_general.dep.unique()
all_sexe = covid_france_general.sexe.unique()
all_reg = covid_france_dc_age.reg.unique()
all_pays = df_monde.Country.unique()



########################################### Data Table################################################

# conditions on the world data table:      
style_dataconditional=[
                   {
                       'if': {
                           'column_id': 'WHO_region',
                           'filter_query': 'WHO_region eq "EURO"'
                           },                        
                       'backgroundColor': '#3D9970', # mettre les lignes EURO en bleu
                       'color': 'white',
                       },
                    {
                      'if': {
                           'column_id': 'Country',
                           'filter_query': 'Country eq "France"'
                           },                        
                       'backgroundColor': '#3D9970', # mettr eles lignes france en bleu
                       'color': 'white',
                           },
                   {
                       'if': {
                           'column_id': 'New_cases',
                           'filter_query': 'New_cases > 100'
                           },
                       'backgroundColor': 'yellow', 
                       'color': 'black',
                       },
                    {
                       'if': {
                           'column_id': 'New_cases',
                           'filter_query': 'New_cases < 50'
                           },
                       'backgroundColor': 'white',
                       'color': 'green',
                       },
                    {
                       'if': {
                           'column_id': 'New_cases',
                           'filter_query': 'New_cases > 1000'
                           },
                       'backgroundColor': 'orange',
                       'color': 'white',
                       },
                    {
                        'if': {
                            'column_id': 'New_deaths',
                            'filter_query': 'New_deaths > 100'
                            },
                        'backgroundColor': 'red',
                        'color': 'white',
                        },
                    {
                        'if': {
                            'column_id': 'New_deaths',
                            'filter_query': 'New_deaths > 1000'
                            },
                        'backgroundColor': '#7f0000',
                        'color': 'white',
                        },
                    {
                        'if': {
                            'column_id': 'New_deaths',
                            'filter_query': 'New_deaths < 50'
                            },
                        'backgroundColor': 'white',
                        'color': 'green',
                        }
            ]



##############################################APP Layout##################################################################

app.layout = html.Div([
    html.H1(children='Covid-19 Dashboard',
        style={
            'textAlign': 'center',
            'color': '#101b32'
            }
        ),
    dcc.Tabs(id='tabs-world', value='world-data', children=[ 
        dcc.Tab(label='Monde', value='world-data', style=tab_style, selected_style=tab_selected_style,children=[
           
            dbc.Row([
                dbc.Col(html.Div([
                html.Br(),
                cards,
                html.Br(),
                html.Br()])),
                ],style={"margin":"auto"}),

            html.Div(id='tabs-content-inline'),
            
            html.H5(children='The WHO regions for which the data were used are: AMRO: The Americas, EMRO: Eastern Mediterrane, EURO: Europe, AFRO: Africa, SEARO: South-East Asia',
        style={
            'textAlign': 'left',
            'color': '#101b32'
            }
        ),   dbc.Row(dbc.Card(html.Div([
                dcc.Dropdown(
                    id="dropdown5",
                    options=[{"label": x, "value": x} for x in all_pays],
                    value=all_pays[0],
                    clearable=False,
             ),
                dcc.Graph(id="line-chart8"),
                dcc.Dropdown(
                    id="dropdown6",
                    options=[{"label": x, "value": x} for x in all_pays],
                    value=all_pays[0],
                    clearable=False,
             ),
                dcc.Graph(id="line-chart9"),
        ]), body=True, color="#AED6F1")),

            dbc.Row(dbc.Card(html.Div([
                dcc.Dropdown(
                    id="dropdown7",
                    options=[{"label": x, "value": x} for x in all_pays],
                    value=all_pays[0],
                    clearable=False,
             ),
                dcc.Graph(id="line-chart10"),
                dcc.Dropdown(
                    id="dropdown8",
                    options=[{"label": x, "value": x} for x in all_pays],
                    value=all_pays[0],
                    clearable=False,
             ),
                dcc.Graph(id="line-chart11"),
        ]), body=True, color="#AED6F1")),
            dbc.Row([
                dbc.Col(html.Div([
                html.Br(),
                card_graph_world1,
                html.Br(),
                html.Br()])),
                ],style={"margin":"auto"}),
            dbc.Row([
                dbc.Col(html.Div([
                html.Br(),
                card_graph_world3,
                html.Br(),
                html.Br()])),
                ],style={"margin":"auto"}),
            dbc.Row([
                dbc.Col(html.Div([
                html.Br(),
                card_graph_world2,
                html.Br(),
                html.Br()])),
                ],style={"margin":"auto"}),
            dbc.Row([
                dbc.Col(html.Div([
                html.Br(),
                card_graph_world5,
                html.Br(),
                html.Br()])),
                ],style={"margin":"auto"}),
            dbc.Row([
                dbc.Col(html.Div([
                html.Br(),
                card_graph_world4,
                html.Br(),
                html.Br()])),
                ],style={"margin":"auto"}),
        
           dash_table.DataTable(
            columns=[
                    {'name': 'Date', 'id': 'Date_reported', 'type': 'datetime'},
                    {'name': 'Country', 'id': 'Country', 'type': 'text'},
                    {'name': 'Continent', 'id': 'WHO_region', 'type': 'text'},
                    {'name': 'New cases', 'id': 'New_cases', 'type': 'numeric'},
                    {'name': 'New deaths', 'id': 'New_deaths', 'type': 'numeric'},
                    {'name': 'Cumulative cases', 'id': 'Cumulative_cases', 'type': 'numeric'},
                    {'name': 'Cumulative deaths', 'id': 'Cumulative_deaths', 'type': 'numeric'}
                    ],
               data=df_monde.to_dict('records'),
               sort_action='native',
               sort_mode="multi",
               column_selectable="single",
               row_selectable="multi",
               style_data_conditional= style_dataconditional,
               fixed_rows={'headers': True, 'data': 1},
               filter_action='native',
               selected_columns=[],
               selected_rows=[],
               page_action="native",
               page_current= 0,
               page_size=10,
               css=[{
                   'selector': '.dash-spreadsheet td div',
                   'rule': '''
                   line-height: 15px;
                   max-height: 30px; min-height: 30px; height: 30px;
                   display: block;
                   overflow-y: hidden;
                   '''
            }],
              tooltip_data=[
                {
                column: {'value': str(value), 'type': 'markdown'}
                for column, value in row.items()
            }   for row in df_monde.to_dict('records')
            ],
            tooltip_duration=None,

            style_cell={'textAlign': 'left'}
    ),  
        ]),
        dcc.Tab(label='France', value='France-data', style=tab_style, selected_style=tab_selected_style,children=[
             dbc.Row([
                dbc.Col(html.Div([
                html.Br(),
                cards_fr,
                html.Br(),
                html.Br()])),
                ],style={"margin":"auto"}),
             dbc.Row(dbc.Card(html.Div([    
                dcc.Checklist(  
                    id="checklist", 
                    value=all_dep[3:],  
                    labelStyle={'display': 'inline-block'}  
                ),  
                dcc.Graph(id="line-chart"), 
            ]), body=True, color="#C39BD3")),   

             dbc.Row(dbc.Card(html.Div([    
                dcc.Checklist(  
                    id="checklist1",    
                    value=all_dep[3:],  
                    labelStyle={'display': 'inline-block'}  
                ),  
                dcc.Graph(id="line-chart1"),    
            ]),body=True, color="#AF7AC5")),    

             dbc.Row(dbc.Card(html.Div([    
                dcc.Dropdown(   
                    id="dropdown",  
                    options=[{"label":"Les deux","value":0}, {"label":"Hommes","value":1}, {"label":"Femmes","value":2}],   
                    value=0,    
                    clearable=False,    
             ), 
                dcc.Graph(id="line-chart2"),    
                dcc.Graph(id="line-chart3"),    
        ]), body=True, color="#9B59B6")),   

            dbc.Row(dbc.Card(html.Div([ 
                dcc.Dropdown(   
                    id="dropdown1", 
                    options=[{"label":"Guadeloupe","value":1},{"label":"Martinique","value":2},{"label":"Guyane","value":3},    
                    {"label":"Reunion","value":4},{"label":"Mayotte","value":6},{"label":"Île-de-France","value":11},   
                    {"label":"Centre-Val de Loire","value":24},{"label":"Bourgogne","value":27},{"label":"Normandie","value":28},   
                    {"label":"Hauts-de-France","value":32},{"label":"Grand-Est","value":44},{"label":"Pays de la Loire","value":52},    
                    {"label":"Bretagne","value":53},{"label":"Nouvelle Aquitaine","value":75},{"label":"Occitanie","value":76}, 
                    {"label":"Auvergne","value":84},{"label":"PACA","value":93},{"label":"Corse","value":94}],  
                    value=all_reg[0],   
                    clearable=False,    
             ), 
                dcc.Graph(id="line-chart4"),    
                dcc.Dropdown(   
                    id="dropdown2", 
                    options=[{"label":"Guadeloupe","value":1},{"label":"Martinique","value":2},{"label":"Guyane","value":3},    
                    {"label":"Reunion","value":4},{"label":"Mayotte","value":6},{"label":"Île-de-France","value":11},   
                    {"label":"Centre-Val de Loire","value":24},{"label":"Bourgogne","value":27},{"label":"Normandie","value":28},   
                    {"label":"Hauts-de-France","value":32},{"label":"Grand-Est","value":44},{"label":"Pays de la Loire","value":52},    
                    {"label":"Bretagne","value":53},{"label":"Nouvelle Aquitaine","value":75},{"label":"Occitanie","value":76}, 
                    {"label":"Auvergne","value":84},{"label":"PACA","value":93},{"label":"Corse","value":94}],  
                    value=all_reg[0],   
                    clearable=False,    
             ), 
                dcc.Graph(id="line-chart5"),    
        ]), body=True, color="#7D3C98")),   

            dbc.Row(dbc.Card(html.Div([ 
                dcc.Dropdown(   
                    id="dropdown3", 
                    options=[{"label":"Guadeloupe","value":1},{"label":"Martinique","value":2},{"label":"Guyane","value":3},    
                    {"label":"Reunion","value":4},{"label":"Mayotte","value":6},{"label":"Île-de-France","value":11},   
                    {"label":"Centre-Val de Loire","value":24},{"label":"Bourgogne","value":27},{"label":"Normandie","value":28},   
                    {"label":"Hauts-de-France","value":32},{"label":"Grand-Est","value":44},{"label":"Pays de la Loire","value":52},    
                    {"label":"Bretagne","value":53},{"label":"Nouvelle Aquitaine","value":75},{"label":"Occitanie","value":76}, 
                    {"label":"Auvergne","value":84},{"label":"PACA","value":93},{"label":"Corse","value":94}],  
                    value=all_reg[0],   
                    clearable=False,    
             ), 
                dcc.Graph(id="line-chart6"),    
                dcc.Dropdown(   
                    id="dropdown4", 
                    options=[{"label":"Guadeloupe","value":1},{"label":"Martinique","value":2},{"label":"Guyane","value":3},    
                    {"label":"Reunion","value":4},{"label":"Mayotte","value":6},{"label":"Île-de-France","value":11},   
                    {"label":"Centre-Val de Loire","value":24},{"label":"Bourgogne","value":27},{"label":"Normandie","value":28},   
                    {"label":"Hauts-de-France","value":32},{"label":"Grand-Est","value":44},{"label":"Pays de la Loire","value":52},    
                    {"label":"Bretagne","value":53},{"label":"Nouvelle Aquitaine","value":75},{"label":"Occitanie","value":76}, 
                    {"label":"Auvergne","value":84},{"label":"PACA","value":93},{"label":"Corse","value":94}],  
                    value=all_reg[0],   
                    clearable=False,    
             ), 
                dcc.Graph(id="line-chart7"),    
        ]), body=True, color="#C39BD3")),
            ]),
        dcc.Tab(label='France: Réanimation', value='tab-1', style=tab_style, selected_style=tab_selected_style, children=[
             dbc.Row([
                dbc.Col(html.Div([
                html.Br(),
                cards_rea,
                html.Br(),
                html.Br()])),
                ],style={"margin":"auto"}),

             dbc.Row([
                dbc.Col(html.Div([
                html.Br(),
                card_graph_rea_tps1,
                html.Br(),
                html.Br()])),
                ],style={"margin":"auto"}),

             dbc.Row([
                dbc.Col(html.Div([
                html.Br(),
                card_graph_rea_sexe1,
                html.Br(),
                html.Br()])),
                ],style={"margin":"auto"}),

             dbc.Row([
                dbc.Col(html.Div([
                html.Br(),
                card_graph_rea_reg1,
                html.Br(),
                html.Br()])),
                ],style={"margin":"auto"}),

             dbc.Row([
                dbc.Col(html.Div([
                html.Br(),
                card_graph_rea_dep1,
                html.Br(),
                html.Br()])),
                ],style={"margin":"auto"}),
            ]),
        dcc.Tab(label='France: Décès', value='tab-2', style=tab_style, selected_style=tab_selected_style,children=[
             dbc.Row([
                dbc.Col(html.Div([
                html.Br(),
                cards_dc,
                html.Br(),
                html.Br()])),
                ],style={"margin":"auto"}),
            dbc.Row([   
                dbc.Col(html.Div([  
                html.Br(),  
                card_graph_dc_tps1, 
                html.Br(),  
                html.Br()])),   
                ],style={"margin":"auto"}), 

             dbc.Row([  
                dbc.Col(html.Div([  
                html.Br(),  
                card_graph_dc_sexe1,    
                html.Br(),  
                html.Br()])),   
                ],style={"margin":"auto"}), 

             dbc.Row([  
                dbc.Col(html.Div([  
                html.Br(),  
                card_graph_dc_reg1, 
                html.Br(),  
                html.Br()])),   
                ],style={"margin":"auto"}), 

             dbc.Row([  
                dbc.Col(html.Div([  
                html.Br(),  
                card_graph_dc_dep1, 
                html.Br(),  
                html.Br()])),   
                ],style={"margin":"auto"}),
            ]),
        dcc.Tab(label='France: Vaccination', value='tab-3', style=tab_style, selected_style=tab_selected_style,children=[
            dbc.Row([
                dbc.Col(html.Div([
                html.Br(),
                cards_vacc,
                html.Br(),
                html.Br()])),
                ],style={"margin":"auto"}),

            dbc.Row([
                dbc.Col(html.Div([
                html.Br(),
                card_graph_dose1,
                html.Br(),
                html.Br()])),
                ],style={"margin":"auto"}),  

             dbc.Row([
                dbc.Col(html.Div([
                html.Br(),
                card_graph_dose_cum,
                html.Br(),
                html.Br()])),
                ],style={"margin":"auto"}),

            dbc.Row([
                dbc.Col(html.Div([
                html.Br(),
                card_graph_age1,
                html.Br(),
                html.Br()])),
                ],style={"margin":"auto"}),

            dbc.Row([
                dbc.Col(html.Div([
                html.Br(),
                card_graph_reg1,
                html.Br(),
                html.Br()])),
                ],style={"margin":"auto"}),

                    ]),
        ], style=tabs_styles),
    

])

@app.callback(Output('tabs-content-inline', 'children'),
              Input('tabs-world', 'value'))

def render_content(tab):
    if tab == 'world-data':
        return html.Div([
            html.H3('Données mondiales')
        ])
    elif tab == 'France-data':
        return html.Div([
            html.H3('Données de la France')
        ])
    elif tab == 'tab-1':
        return html.Div([
            html.H3('Données réanimation')
        ])
    elif tab == 'tab-2':
        return html.Div([
            html.H3('Données décès')
        ])
    elif tab == 'tab-3':
        return html.Div([
            html.H3('Données vaccination')
        ])



############################################################## Callbacks##############################################################

@app.callback(  
    Output("line-chart", "figure"),     
    [Input("checklist", "value")])  

def update_line_chart(continents):  
    mask = covid_france_general.dep.isin(continents)    
    fig = px.line(covid_france_general[mask],   
        x="jour", y="rea", color='dep',title="Nombre de réanimations en fonction du temps suivant les départements choisis",    
        labels={"jour":"Date", "rea": "Nombre de réanimations"})    
    return fig  

@app.callback(  
    Output("line-chart1", "figure"),    
    [Input("checklist1", "value")]) 

def update_line_chart(departements):    
    mask = covid_france_general.dep.isin(departements)  
    fig = px.line(covid_france_general[mask],   
        x="jour", y="dc", color='dep',title='Nombre de décès en fonction du temps suivant les départements choisis',    
        labels={"jour":"Date","dc":"Nombre de décès"})  
    return fig  

@app.callback(  
    Output("line-chart2", "figure"),    
    [Input("dropdown","value")])    
def update_bar_chart(sex):  
    mask = covid_france_general["sexe"] == sex  
    fig = px.line(covid_france_general[mask], x="jour", y="rea", title="Nombre de réanimations en fonction du temps suivant le sexe sélectionné",   
        labels={"jour":"Date", "rea":"Nombre de réanimations"}) 
    return fig  

@app.callback(  
    Output("line-chart3", "figure"),    
    [Input("dropdown","value")])    

def update_bar_chart2(sex): 
    mask = covid_france_general["sexe"] == sex  
    fig = px.line(covid_france_general[mask], x="jour", y="dc", title="Nombre de décès en fonction du temps suivant le sexe sélectionné",   
        labels={"jour":"Date","dc":"Nombre de décès"})  
    return fig  

@app.callback(  
    Output("line-chart4", "figure"),    
    [Input("dropdown1","value")])   
def update_bar_chart(region):   
    mask = covid_france_dc_age["reg"] == region 
    fig = px.line(covid_france_dc_age[mask], x="jour", y="rea", title="Nombre de réanimations en fonction du temps dans la région sélectionnée",    
        labels={"jour":"Date","rea":"Nombre de réanimations"})  
    return fig  

@app.callback(  
    Output("line-chart5", "figure"),    
    [Input("dropdown2","value")])   

def update_bar_chart2(region):  
    mask = covid_france_dc_age["reg"] == region 
    fig = px.line(covid_france_dc_age[mask], x="jour", y="rea", title="Nombre de réanimations en fonction du temps dans la région sélectionnée",    
        labels={"jour":"Date","rea":"Nombre de réanimations"})  
    return fig  

@app.callback(  
    Output("line-chart6", "figure"),    
    [Input("dropdown3","value")])   
def update_bar_chart(region):   
    mask = covid_france_dc_age["reg"] == region 
    fig = px.line(covid_france_dc_age[mask], x="jour", y="dc", title="Nombre de décès en fonction du temps dans la région sélectionnée",    
        labels={"jour":"Date","dc":"Nombre de décès"})  
    return fig  

@app.callback(  
    Output("line-chart7", "figure"),    
    [Input("dropdown4","value")])   

def update_bar_chart2(region):  
    mask = covid_france_dc_age["reg"] == region 
    fig = px.line(covid_france_dc_age[mask], x="jour", y="dc", title="Nombre de décès en fonction du temps dans la région sélectionnée",    
        labels={"jour":"Date","dc":"Nombre de décès"})  
    return fig  

@app.callback(  
    Output("line-chart8", "figure"),    
    [Input("dropdown5","value")])   
def update_bar_chart(pays): 
    mask = df_monde["Country"] == pays  
    fig = px.line(df_monde[mask], x="Date_reported", y="New_cases", title="Nombre de nouveaux cas au cours du temps dans le pays sélectionné",  
        labels={"Date_reported":"Date","New_cases":"Nombre de nouveaux cas"})    
    return fig  

@app.callback(  
    Output("line-chart9", "figure"),    
    [Input("dropdown6","value")])   

def update_bar_chart2(pays):    
    mask = df_monde["Country"] == pays  
    fig = px.line(df_monde[mask], x="Date_reported", y="New_cases", title="Nombre de nouveaux cas au cours du temps dans le pays sélectionné",  
        labels={"Date_reported":"Date","New_cases":"Nombre de nouveaux cas"})    
    return fig  

@app.callback(  
    Output("line-chart10", "figure"),   
    [Input("dropdown7","value")])   
def update_bar_chart(pays): 
    mask = df_monde["Country"] == pays  
    fig = px.line(df_monde[mask], x="Date_reported", y="New_deaths", title="Nombre de nouveaux décès au cours du temps dans le pays sélectionné",   
        labels={"Date_reported":"Date","New_deaths":"Nombre de nouveaux décès"}) 
    return fig  

@app.callback(  
    Output("line-chart11", "figure"),   
    [Input("dropdown8","value")])   

def update_bar_chart2(pays):    
    mask = df_monde["Country"] == pays  
    fig = px.line(df_monde[mask], x="Date_reported", y="New_deaths", title="Nombre de nouveaux décès au cours du temps dans le pays sélectionné",   
        labels={"Date_reported":"Date","New_deaths":"Nombre de nouveaux décès"}) 
    return fig  


if __name__ == '__main__':
    app.run_server(debug=True,host='localhost',port=8080)
