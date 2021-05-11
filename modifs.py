t dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
from dash.dependencies import Input, Output
import dash_table
from datetime import datetime
import numpy as np
import dash_bootstrap_components as dbc

#import warnings
#from six import PY3
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
dash_colors = {
    'background': '#f2ffff',
    'text': '#101b32',
    'grid': '#333333',
    'red': '#BF0010',
    'blue': '#809cd5',
    'green': '#46c299'
}

covid_monde_url = ("https://covid19.who.int/WHO-COVID-19-global-data.csv")
df_monde = pd.read_csv(covid_monde_url, sep=",")

covid_monde_vaccination_url = ("https://covid19.who.int/who-data/vaccination-data.csv")
df_monde_vacc = pd.read_csv(covid_monde_vaccination_url, sep=",")

covid_url = ("https://www.data.gouv.fr/fr/datasets/r/900da9b0-8987-4ba7-b117-7aea0e53f530")
df = pd.read_csv(covid_url, sep=";")

#warnings.filterwarnings("ignore")

#données OMS

df_monde['date'] = pd.to_datetime(df_monde['Date_reported'])
#données france: vaccins


#df_fr= pd.DataFrame(data_fr, columns =data_fr_columns)

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

sum_cases_monde = df_monde['New_cases'].sum() 
sum_deaths = df_monde['New_deaths'].sum()
sum_vaccination = df_monde_vacc['TOTAL_VACCINATIONS'].sum()

#il s'agit de la dernière date renseignées dans la base de données
#date_recente = max(df['Date_reported'])

#nouvelle base de données contenant uniquement les données de la dernière date
#covid_monde_last_day = df[df.Date_reported == date_recente]

# somme des cas pour le dernier jour renseigné dans la base
#sum_cases_last_day = covid_monde_last_day['New_cases'].sum()

# somme des décès pour le dernier jour renseigné dans la base
#sum_deaths_last_day = covid_monde_last_day['New_deaths'].sum()

def create_card(title, content, color):
    card=dbc.Card(
        dbc.CardBody(
            [html.H4(title, className="card-title"),
            html.Br(),
            html.H2(content, className="card-subtitle"),
            html.Br(),
            ]),
        color=color, inverse=True
        )
    return(card)

card1=create_card("Nombre de cas", sum_cases_monde, "red")
card2=create_card("Nombre de décès", sum_deaths, "blue")
card3=create_card("Nombre de vaccinations", sum_vaccination, "green")

card = dbc.Row([dbc.Col(id='card1', children=[card1]),
                         dbc.Col(id='card2', children=[card2]),
                         dbc.Col(id='card3', children=[card3])],
                    style={"margin-left":"0px","margin-right":'0px'})

app.layout = html.Div([
    html.H1('Covid-19 Dasboard'),
    dcc.Tabs(id='tabs-world', value='world-data', children=[ 
        dcc.Tab(label='Monde', value='world-data', style=tab_style, selected_style=tab_selected_style,children=[
            dbc.Row([
                dbc.Col(html.Div([
                html.Br(),
                card,
                html.Br(),
                html.Br()]))
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
            ]),
        dcc.Tab(label='France Réanimation', value='tab-1', style=tab_style, selected_style=tab_selected_style, children=[
            ]),
        dcc.Tab(label='France Décès', value='tab-2', style=tab_style, selected_style=tab_selected_style,children=[
            ]),
        dcc.Tab(label='France Vaccination', value='tab-3', style=tab_style, selected_style=tab_selected_style,children=[
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
