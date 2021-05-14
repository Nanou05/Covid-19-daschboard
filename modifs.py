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

#import warnings
#from six import PY3
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__,external_stylesheets=[dbc.themes.BOOTSTRAP])
dash_colors = {
    'background': '#f2ffff',
    'text': '#101b32',
    'grid': '#333333',
    'red': '#BF0010',
    'blue': '#809cd5',
    'green': '#46c299'
}

## Données monde général
covid_monde_url = ("https://covid19.who.int/WHO-COVID-19-global-data.csv")
df_monde = pd.read_csv(covid_monde_url, sep=",")
df_monde['date'] = pd.to_datetime(df_monde['Date_reported'])

## Données vaccination dans le monde
covid_monde_vaccination_url = ("https://covid19.who.int/who-data/vaccination-data.csv")
df_monde_vacc = pd.read_csv(covid_monde_vaccination_url, sep=",")

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

#warnings.filterwarnings("ignore")

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
date_recente = max(df_monde['date'])
covid_monde_last_day = df_monde[df_monde.date == date_recente]
sum_cases_last_day = covid_monde_last_day['New_cases'].sum()
sum_deaths_last_day = covid_monde_last_day['New_deaths'].sum()

date_recente_str = date_recente.strftime('%Y-%m-%d')

#Indicateurs du monde
card1=create_card("Nombre de cas", sum_cases_monde, date_recente_str)
card2=create_card("Nombre de décès", sum_deaths, date_recente_str)
card3=create_card("Nombre de vaccinations", sum_vaccination,date_recente_str)
card4=create_card("Nombre de cas du jour", sum_cases_last_day,date_recente_str)
card5=create_card("Nombre de décès du jour", sum_deaths_last_day,date_recente_str)

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

card_fr1=create_card("Nombre de décès", f'{total_deces_general} dont {total_deces_hosp} en milieu hospitalier', dernier_jour_gen_str)
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

card_rea1=create_card("Nombre de réanimations", total_rea, dernier_jour_hosp_str)
card_rea2=create_card("Nombre de réanimations chez les hommes en milieu hospitalier", rea_homme,dernier_jour_gen_str)
card_rea3=create_card("Nombre de réanimations chez les femmes en milieu hospitalier", rea_femme,dernier_jour_gen_str)
card_rea4=create_card("Nombre de réanimations du jour", nombre_rea_jour,dernier_jour_hosp_str)

cards_rea = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(dbc.Card(card_rea1, color="#FDEBD0", inverse=True)),
                dbc.Col(dbc.Card(card_rea2, color="#FAD7A0", inverse=True)),
                dbc.Col(dbc.Card(card_rea3, color="#F8C471", inverse=True)),
                dbc.Col(dbc.Card(card_rea4, color="#F5B041", inverse=True)),

            ],
            className="mb-2",
        ),
    ]
)


# Indicateurs décès

card_dc1=create_card("Nombre de décès", f'{total_deces_general} dont {total_deces_hosp} en milieu hospitalier', dernier_jour_hosp_str)
card_dc2=create_card("Nombre de décès chez les hommes", deces_homme,dernier_jour_gen_str)
card_dc3=create_card("Nombre de décès chez les femmes", deces_femme,dernier_jour_gen_str)
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

## Graphiques réanimations

# Graphique réanimation en fonction du temps

evol_rea = covid_france_rea_tps_sexe[['date','rea']].groupby('date', as_index=False).sum()

def update_graph_rea_tps(title):
    fig_tps = px.line(evol_rea, x=evol_rea['date'], y=evol_rea['rea'], title=title)

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
    fig_age = px.bar(age_rea, x=age_rea['cl_age90_str'], y=age_rea['rea'], title=title, text=age_rea['rea'])
    fig_age.update_traces(textposition='outside')
    return fig_age

card_graph_rea_age = dbc.Card(
    dcc.Graph(id='my-graph-rea-age', figure=update_graph_rea_age("Nombre total de réanimation en fonction de la classe d'âge")), body=True, color ='#FAD7A0',
    )

# Graphique réanimation en fonction du sexe

sexe_rea = covid_france_rea_tps_sexe[['sexe','rea']].groupby('sexe', as_index=False).sum()
sexe_rea['sexe_str'] = ["Les deux","Hommes","Femmes"]

def update_graph_rea_sexe(title):
    fig_sexe = px.bar(sexe_rea, x=sexe_rea['sexe_str'], y=sexe_rea['rea'], title=title, text=sexe_rea['rea'])
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

reg_rea = covid_france_rea_age[['reg','rea']].groupby('reg', as_index=False).sum()
reg_rea['reg_str']= ["Guadeloupe","Martinique","Guyane","Reunion","Mayotte","Île-de-France",
"Centre-Val de Loire","Bourgogne","Normandie","Hauts-de-France","Grand-Est","Pays de la Loire",
"Bretagne","Nouvelle Aquitaine","Occitanie","Auvergne","PACA","Corse"]

def update_graph_rea_reg(title):
    fig_reg = px.bar(reg_rea, x=reg_rea['reg_str'], y=reg_rea['rea'], title=title, text=reg_rea['rea'])
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

dep_rea = covid_france_rea_tps_sexe[['dep','rea']].groupby('dep', as_index=False).sum()
dep_rea_new = dep_rea.drop(dep_rea.index[96:101])
dep_rea_new['dep_str'] = ["01","02","03","04","05","06","07","08","09","10","11","12","13",
"14","15","16","17","18","19","21","22","23","24","25","26","27","28","29","2A","2B","30","31",
"32","33","34","35","36","37","38","39","40","41","42","43","44","45","46","47","48","49",
"50","51","52","53","54","55","56","57","58","59","60","61","62","63","64","65","66","67",
"68","69","70","71","72","73","74","75","76","77","78","79","80","81","82","83","84","85",
"86","87","88","89","90","91","92","93","94","95"]

def update_graph_rea_dep(title):
    fig_dep = px.bar(dep_rea_new, x=dep_rea_new['dep_str'], y=dep_rea_new['rea'], title=title, text=dep_rea_new['rea'])
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

#Graphiques vaccinations dose
evol = covid_france_vaccination[['date','n_dose1']].groupby('date', as_index=False).sum()

def update_graph_dose1(title):
    fig1 = px.line(evol, x=evol['date'], y=evol['n_dose1'], title=title)

    return fig1

card_graph_dose = dbc.Card(
    dcc.Graph(id='my-graph-dose', figure=update_graph_dose1("Nombre de vaccinations par la dose 1 chaque jour")), body=True, color="#ABEBC6",
    )

evol2 = covid_france_vaccination[['date','n_dose2']].groupby('date', as_index=False).sum()

def update_graph_dose2(title):
    fig2 = px.line(evol2, x=evol2['date'], y=evol2['n_dose2'],title=title)

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
    fig3 = px.line(evol_cum, x=evol_cum['date'], y=evol_cum['n_cum_dose1'], title=title)

    return fig3

card_graph_dose_cum1 = dbc.Card(
    dcc.Graph(id='my-graph-dose-cum-1', figure=update_graph_dose_cum1("Evolution du nombre de vaccinations par la dose 1")), body=True, color="#ABEBC6")

evol_cum2 = covid_france_vaccination[['date','n_cum_dose2']].groupby('date', as_index=False).sum()

def update_graph_dose_cum1(title):
    fig4 = px.line(evol_cum2, x=evol_cum2['date'], y=evol_cum2['n_cum_dose2'], title=title)

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
    fig = px.bar(evol_age, x=evol_age['classe_age'], y=evol_age['n_complet'], title=title)

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
    fig5 = px.bar(evol_reg, x=evol_reg['region'],y=evol_reg['n_complet'], title=title, text=evol_reg['n_complet'])
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

app.layout = html.Div([
    html.H1('Covid-19 Dasboard'),
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

           dash_table.DataTable(# voir pourquoi les données ne s'affichent pas
               data=df_monde.to_dict('records'),
               sort_action='native',
               sort_mode="multi",
               column_selectable="single",
               row_selectable="multi",
               columns=[{'id': c, 'name': c} for c in df_monde.columns],
               fixed_rows={'headers': True, 'data': 1},
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
            ]),
        dcc.Tab(label='France Réanimation', value='tab-1', style=tab_style, selected_style=tab_selected_style, children=[
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
        dcc.Tab(label='France Décès', value='tab-2', style=tab_style, selected_style=tab_selected_style,children=[
             dbc.Row([
                dbc.Col(html.Div([
                html.Br(),
                cards_dc,
                html.Br(),
                html.Br()])),
                ],style={"margin":"auto"}),
            ]),
        dcc.Tab(label='France Vaccination', value='tab-3', style=tab_style, selected_style=tab_selected_style,children=[
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

if __name__ == '__main__':
    app.run_server(debug=True,host='localhost',port=8080)
