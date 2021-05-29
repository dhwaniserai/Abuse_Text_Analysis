import dash
import dash_html_components as html
from app import app
import datetime
import json
from dash.dependencies import Input, Output


import dash_bootstrap_components as dbc
PLOTLY_LOGO = "https://cdn2.vectorstock.com/i/thumb-large/24/26/happy-business-friends-logo-vector-1662426.jpg"
s=0
search_bar = dbc.Row(
    [
        dbc.Col(dbc.Button("Home",href="/apps/home", color="warning", className="ml-2",outline=True),
            width="auto"),
        dbc.Col(
            dbc.Button("Help",href="/apps/mot", color="warning", className="ml-2",outline=True),
            width="auto"),
        dbc.Col(
            dbc.Button("Chat",href="/apps/chat", color="warning", className="ml-2"),
            width="auto"),
        dbc.Col(
            dbc.Button("Emergency",href="/apps/eme", color="warning", className="ml-2",outline=True),
            width="auto"),
    ],
    no_gutters=True,
    className="ml-auto flex-nowrap mt-3 mt-md-0",
    align="center",
)
form = dbc.Form(
    [
        dbc.FormGroup(
            [
                html.H5("Do you feel anxious or nervous when you are around your partner?", className="mr-2"),
             dbc.FormGroup(
    [
        dbc.Label("", html_for="radios-row1", width=0.5),
        dbc.Col(
            dbc.RadioItems(
                id="radios-row1",
                options=[
                    {"label": "Yes", "value": 2},
                    {"label": "No", "value":0},
                    {"label": "Sometimes","value": 1,
                        
                    },
                ],value=0,#defauly value
            ),
            width=100,
        ),
    ],
    
)

            ],
            className="mr-3",
        ),
        dbc.FormGroup(
            [
                html.H5("Do you watch what you are doing in order to avoid making your partner angry or upset?", className="mr-2"),
                dbc.FormGroup(
    [
        dbc.Label("", html_for="radios-row2", width=0.5),
        dbc.Col(
            dbc.RadioItems(
                id="radios-row2",
                options=[
                    {"label": "Yes", "value":2},
                    {"label": "No", "value":0},
                    {
                        "label": "Sometimes",
                        "value": 1,
                        
                    },
                ],value=0,
            ),
            width=100,
        ),
    ],
    
)
           ],className="mr-3",
        ),
        dbc.FormGroup(
            [
                html.H5("Do you feel obligated or coerced into having sex with your partner?", className="mr-2"),
                dbc.FormGroup(
    [
        dbc.Label("", html_for="radios-row3", width=0.5),
        dbc.Col(
            dbc.RadioItems(
                id="radios-row3",
                options=[
                    {"label": "Yes", "value": 2},
                    {"label": "No", "value": 0},
                    {
                        "label": "Sometimes",
                        "value": 1,
                        
                    },
                ],value=0,
            ),
            width=100,
        ),
    ],
    
)
           ],className="mr-3",
        ),
        dbc.FormGroup(
            [
                html.H5("Are you afraid of voicing a different opinion than your partner?", className="mr-2"),
            dbc.FormGroup(
    [
        dbc.Label("", html_for="radios-row4", width=0.5),
        dbc.Col(
            dbc.RadioItems(
                id="radios-row4",
                options=[
                    {"label": "Yes", "value": 2},
                    {"label": "No", "value": 0},
                    {
                        "label": "Sometimes",
                        "value": 1,
                        
                    },
                ],value=0
            ),
            width=100,
        ),
    ],
    
)
           ],className="mr-3",
        ),
        dbc.FormGroup(
            [
                html.H5("Does your partner criticize you or embarrass you in front of others?", className="mr-2"),
          dbc.FormGroup(
    [
        dbc.Label("", html_for="radios-row5", width=0.5),
        dbc.Col(
            dbc.RadioItems(
                id="radios-row5",
                options=[
                    {"label": "Yes", "value": 2},
                    {"label": "No", "value": 0},
                    {
                        "label": "Sometimes",
                        "value": 1,
                        
                    },
                ],value=0,
            ),
            width=100,
        ),
    ],
    
)
          ],className="mr-3",
        ),
        dbc.FormGroup(
            [
                html.H5("Does your partner check up on what you have been doing, and not believe your answers?", className="mr-2"),
           dbc.FormGroup(
    [
        dbc.Label("", html_for="radios-row6", width=0.5),
        dbc.Col(
            dbc.RadioItems(
                id="radios-row6",
                options=[
                    {"label": "Yes", "value": 2},
                    {"label": "No", "value": 0},
                    {
                        "label": "Sometimes",
                        "value": 1,
                        
                    },
                ],value=0,
            ),
            width=100,
        ),
    ],
    
)
           ],className="mr-3",
        ),
        dbc.FormGroup(
            [
                html.H5("Is your partner jealous, such as accusing you of having affairs?", className="mr-2"),
            dbc.FormGroup(
    [
        dbc.Label("", html_for="radios-row7", width=0.5),
        dbc.Col(
            dbc.RadioItems(
                id="radios-row7",
                options=[
                    {"label": "Yes", "value": 2},
                    {"label": "No", "value": 0},
                    {
                        "label": "Sometimes",
                        "value": 1,
                        
                    },
                ],value=0,
            ),
            width=100,
        ),
    ],
    
)
            ],className="mr-3",
        ),
        dbc.FormGroup(
            [
                html.H5("Does your partner tell you that he or she will stop beating you when you start behaving yourself?", className="mr-2"),
            dbc.FormGroup(
    [
        dbc.Label("", html_for="radios-row8", width=0.5),
        dbc.Col(
            dbc.RadioItems(
                id="radios-row8",
                options=[
                    {"label": "Yes", "value": 2},
                    {"label": "No", "value": 0},
                    {
                        "label": "Sometimes",
                        "value": 1,
                        
                    },
                ],value=0,
            ),
            width=100,
        ),
    ],
    
)
            ],className="mr-3",
        ),
        dbc.FormGroup(
            [
                html.H5("Have you stopped seeing your friends or family because of your partner's behavior?", className="mr-2"),
                dbc.FormGroup(
    [
        dbc.Label("", html_for="radios-row9", width=0.5),
        dbc.Col(
            dbc.RadioItems(
                id="radios-row9",
                options=[
                    {"label": "Yes", "value": 2},
                    {"label": "No", "value": 0},
                    {
                        "label": "Sometimes",
                        "value": 1,
                        
                    },
                ],value=0,
            ),
            width=100,
        ),
    ],
    
)
            ],className="mr-3",
        ),
        dbc.FormGroup(
            [
                html.H5("Does your partner's behavior make you feel as if you are wrong?", className="mr-2"),
                dbc.FormGroup(
    [
        dbc.Label("", html_for="radios-row10", width=0.5),
        dbc.Col(
            dbc.RadioItems(
                id="radios-row10",
                options=[
                    {"label": "Yes", "value": 2},
                    {"label": "No", "value": 0},
                    {
                        "label": "Sometimes",
                        "value": 1,
                        
                    },
                ],value=0,
            ),
            width=100,
        ),
    ],
    
)
           ],className="mr-3",
        ),
        dbc.FormGroup(
            [
                html.H5("Does your partner threaten to harm you?", className="mr-2"),
                dbc.FormGroup(
    [
        dbc.Label("", html_for="radios-row11", width=0.5),
        dbc.Col(
            dbc.RadioItems(
                id="radios-row11",
                options=[
                    {"label": "Yes", "value": 2},
                    {"label": "No", "value": 0},
                    {
                        "label": "Sometimes",
                        "value": 1,
                        
                    },
                ],value=0,
            ),
            width=100,
        ),
    ],
    
)
            ],className="mr-3",
        ),
        dbc.FormGroup(
            [
                html.H5("Do you try to please your partner rather than yourself in order to avoid being hurt?", className="mr-2"),
                dbc.FormGroup(
    [
        dbc.Label("", html_for="radios-row12", width=0.5),
        dbc.Col(
            dbc.RadioItems(
                id="radios-row12",
                options=[
                    {"label": "Yes", "value": 2},
                    {"label": "No", "value": 0},
                    {
                        "label": "Sometimes",
                        "value": 1,
                        
                    },
                ],value=0,
            ),
            width=100,
        ),
    ],
    
)
        ],className="mr-3",
        ),
        dbc.FormGroup(
            [
                html.H5("Does your partner keep you from going out or doing things that you want to do?", className="mr-2"),
                dbc.FormGroup(
    [
        dbc.Label("", html_for="radios-row13", width=0.5),
        dbc.Col(
            dbc.RadioItems(
                id="radios-row13",
                options=[
                    {"label": "Yes", "value": 2},
                    {"label": "No", "value": 0},
                    {
                        "label": "Sometimes",
                        "value": 1,
                        
                    },
                ],value=0,
            ),
            width=100,
        ),
    ],
    
)],className="mr-3",
        ),
        dbc.FormGroup(
            [
                html.H5("Do you feel that nothing you do is ever good enough for your partner?", className="mr-2"),
                dbc.FormGroup(
    [
        dbc.Label("", html_for="radios-row14", width=0.5),
        dbc.Col(
            dbc.RadioItems(
                id="radios-row14",
                options=[
                    {"label": "Yes", "value": 2},
                    {"label": "No", "value": 0},
                    {
                        "label": "Sometimes",
                        "value": 1,
                        
                    },
                ],value=0,
            ),
            width=100,
        ),
    ],
    
)
            ],className="mr-3",
        ),
        dbc.FormGroup(
            [
                html.H5("Does your partner say that if you try to leave him or her, you will never see your children again?", className="mr-2"),
                dbc.FormGroup(
    [
        dbc.Label("", html_for="radios-row15", width=0.5),
        dbc.Col(
            dbc.RadioItems(
                id="radios-row15",
                options=[
                    {"label": "Yes", "value": 2},
                    {"label": "No", "value": 0},
                    {
                        "label": "Sometimes",
                        "value": 1,
                        
                    },
                ],value=0,
            ),
            width=100,
        ),
    ],
    
)
                ],
            className="mr-3",
        ),
        dbc.FormGroup(
            [
                html.H5("Do you lie to your family, friends and doctor about your bruises, cuts and scratches?", className="mr-2"),
dbc.FormGroup(
    [
        dbc.Label("", html_for="radios-row16", width=0.5),
        dbc.Col(
            dbc.RadioItems(
                id="radios-row16",
                options=[
                    {"label": "Yes", "value": 2},
                    {"label": "No", "value": 0},
                    {
                        "label": "Sometimes",
                        "value": 1,
                        
                    },
                ],value=0,
            ),
            width=100,
        ),
    ],
    
)

            ],
            className="mr-3",
        ),
        dbc.Button("Submit",id="submit", color="success"),
        dbc.Alert("",id="exampleoutput1",className="m-5"),
    ],
    #inline=True,
)

layout = html.Div([ dbc.Row(dbc.Col(dbc.Navbar(
    [
        html.A(
            # Use row and col to control vertical alignment of logo / brand
            dbc.Row(
                [
                    dbc.Col(html.Img(src=PLOTLY_LOGO, height="50px",style={"border-radius":12})),
                    dbc.Col(dbc.NavbarBrand("SAKHI",style={"color":"orange"}, className="ml-2")),
                ],
                align="center",
                no_gutters=True,
            ),

        ),
        dbc.NavbarToggler(id="navbar-toggler"),
        dbc.Collapse(search_bar, id="navbar-collapse", navbar=True),
    ],
    color="dark",
    dark=False,
        ),
    )
    ),
    dbc.Alert(
    
    "Welcome to Sakhi!!", className="m-5"
),
html.B([dbc.Card([form],style={"margin-left":"50px"})])
#],style={"background-color":"lightblue",'background-size':'100% 100%'})
])

@app.callback(
    Output(component_id='exampleoutput1', component_property='children'),
    [Input(component_id='submit', component_property='n_clicks'),
     Input(component_id='radios-row1', component_property='value'),
     Input(component_id='radios-row2', component_property='value'),
     Input(component_id='radios-row3', component_property='value'),
     Input(component_id='radios-row4', component_property='value'),
     Input(component_id='radios-row5', component_property='value'),
     Input(component_id='radios-row6', component_property='value'),
     Input(component_id='radios-row7', component_property='value'),
     Input(component_id='radios-row8', component_property='value'),
     Input(component_id='radios-row9', component_property='value'),
     Input(component_id='radios-row10', component_property='value'),
     Input(component_id='radios-row11', component_property='value'),
     Input(component_id='radios-row12', component_property='value'),
     Input(component_id='radios-row13', component_property='value'),
     Input(component_id='radios-row14', component_property='value'),
     Input(component_id='radios-row15', component_property='value'),
     Input(component_id='radios-row16', component_property='value'),
     ]
)
def update_output_div(b,v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16):
    if b is not None:
        
        v=v1+v2+v3+v4+v5+v6+v7+v8+v9+v10+v11+v12+v13+v14+v15+v16
        if (b>0 and v>20):
            return "You are suffering from Domestic Violence.Please seek support"
        elif (b>0 and v>10):
            return "You may be suffering from Domestic Violence. Check out our home page"
        elif (b>0):
            return "You are not suffering from Domestic Violence"
    else:
        return ""
    
    #return 'Output: {}'.format((v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16))
