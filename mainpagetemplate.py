import dash                              
import dash_html_components as html
#import dash_core_components as dcc
#from dash.dependencies import Output, Input
#from dash_extensions import Lottie
import dash_bootstrap_components as dbc  
#import plotly.express as px
#import pandas as pd

# Bootstrap themes by Ann: https://hellodash.pythonanywhere.com/theme_explorer
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.LUX])
server=app.server()



app.layout = dbc.Container([
    html.Hr(),
    dbc.Row(dbc.Col(html.H1("Social Panda Dashboard",
                            style={"textAlign": "center"}), width=12)),
    html.Hr(),
    dbc.Row([
        dbc.Col(html.H4("Social Media Scheduling",
                            style={"textAlign": "center"}), width=6),
        dbc.Col(html.H4("Social Media Analytics",
                            style={"textAlign": "center"}), width=6)
        
    ]),        
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    dbc.CardImg(src='/assets/whatsapp-logo.gif'), # 150px by 45px
                    dbc.CardLink("WhatsApp Scheduling", target="_blank",href="https://google.com")
                ], style={'textAlign':'center'})
            ]),
        ], width=2),
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    dbc.CardImg(src='/assets/twitter-logo1.gif'), # 150px by 45px
                    dbc.CardLink("Twitter Scheduling", target="_blank",href="https://google.com")

                ], style={'textAlign':'center'})
            ]),
        ], width=2),
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    dbc.CardImg(src='/assets/instagram-logo2.gif'), # 150px by 45px
                    dbc.CardLink("Instagram Scheduling", target="_blank",href="https://socialpanda.herokuapp.com/")
                ], style={'textAlign':'center'})
            ]),
        ], width=2),
       
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    dbc.CardImg(src='/assets/twitter-logo.gif'), # 150px by 45px
                    dbc.CardLink("Twitter Analytics", target="_blank",href="/pages/index.py")
                ], style={'textAlign':'center'})
            ]),
        ], width=2),
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    dbc.CardImg(src='/assets/linkedin-logo1.gif'), # 150px by 45px
                    dbc.CardLink("LinkedIn Analytics", target="_blank",href='https://linkedin-analysis.herokuapp.com/'),
                    #dcc.Location(id='url', refresh=False)
                ], style={'textAlign':'center'})
            ]),
        ], width=2),
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    dbc.CardImg(src='/assets/whatsapp-logo.gif'), # 150px by 45px
                    dbc.CardLink("WhatsApp Analytics", target="_blank",href='https://whatsappanalysis-sp.herokuapp.com/'),
                    #dcc.Location(id='url', refresh=False)
                ], style={'textAlign':'center'})
            ]),
        ], width=2),
    ],className='mb-2'),
    dbc.Row(
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                   dbc.CardImg(src='/assets/panda-hi.gif', style={"height":"300px", "width":"300px"}), # 150px by 45px
                ], style={'textAlign':'center', "height":"300px"}),
              ]),
            
                      
            ]),
        ),
    html.Hr(),
    html.Footer([
    html.Div("Created by Neha and Parth",style={'textAlign':'center'}),
    
    html.Div([
        
        html.P('©SocialPanda 2022', style={'textAlign':'center'}),
    ]),
    html.Hr(),
])

], #fluid=True
)

if __name__=='__main__':
    app.run_server(debug=False, port=8002)

