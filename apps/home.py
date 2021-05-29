import dash
import dash_html_components as html

import dash_bootstrap_components as dbc
PLOTLY_LOGO = "https://cdn2.vectorstock.com/i/thumb-large/24/26/happy-business-friends-logo-vector-1662426.jpg"

search_bar = dbc.Row(
    [
        dbc.Col(dbc.Button("Home",href="/apps/home", color="warning", className="ml-2"),
            width="auto"),
        dbc.Col(
            dbc.Button("Help",href="/apps/mot", color="warning", className="ml-2",outline=True),
            width="auto"),
        dbc.Col(
            dbc.Button("Chat",href="/apps/chat", color="warning", className="ml-2",outline=True),
            width="auto"),
        dbc.Col(
            dbc.Button("Emergency",href="/apps/eme", color="warning", className="ml-2",outline=True),
            width="auto"),
    ],
    no_gutters=True,
    className="ml-auto flex-nowrap mt-3 mt-md-0",
    align="center",
)
top_card = dbc.Card(
    [
        dbc.CardImg(src="https://bespokehr.com.au/wp-content/uploads/bfi_thumb/blue-dynamic-fitness-youtube-thumbnail-oodeowpdf33uwrjas2zmu6mi3keiunphvagqo212n4.png", top=True),
        
    ],
    style={"width": "30rem"},
)
card_content1 = [
    dbc.CardHeader("SIGNS OF PHYSICAL ABUSE"),
    dbc.CardBody(
        [
            #html.H5("Card title", className="card-title"),
            html.P(
                "Physical abuse is intentional bodily injury. Some examples include slapping, pinching, choking, kicking, shoving, or inappropriately using drugs or physical restraints. Signs of physical abuse. Sexual abuse is nonconsensual sexual contact (any unwanted sexual contact).",
                className="card-text",
            ),
        ]
    ),
]
card_content2 = [
    dbc.CardHeader("SIGNS OF EMOTIONAL ABUSE"),
    dbc.CardBody(
        [
           # html.H5("Card title", className="card-title"),
            html.P("Indicators of emotional abuse are Humiliation, negating, and criticizing,Control and shame,Accusing, blaming, and denial,Emotional neglect and isolation,Codependence,What to do.",
                className="card-text",
            ),
        ]
    ),
]
card_content3= [
    dbc.CardHeader("SIGNS OF FINANCIAL ABUSE"),
    dbc.CardBody(
        [
           # html.H5("Card title", className="card-title"),
            html.P("Unexplained withdrawals from the bank,Unusual activity in the bank accounts,Unpaid bills,Unexplained shortage of money,Reluctance on the part of the person with responsibility for the funds to provide basic food and clothes ,Fraud.Theft.",
                className="card-text",
            ),
        ]
    ),
]
row_0=dbc.Row([

    dbc.Col(dbc.Card(top_card)),
],
style={"margin-left":"550px","margin-right":"250px","margin-bottom":"20px","width":"300px"},
)
row_1 = dbc.Row(
    [
        dbc.Col(dbc.Card(card_content1, color="danger", outline=True)),
        dbc.Col(dbc.Card(card_content2, color="danger", outline=True)),
    ],
    style={"margin-left":"50px","margin-bottom":"20px"},
)
row_2 = dbc.Row(
    [
        dbc.Col(dbc.Card(card_content3, color="danger", outline=True)),
        #dbc.Col(dbc.Card(card_content4, color="danger", outline=True)),
    ],
    style={"margin-left":"50px","margin-right":"50px"},
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
    dbc.Alert([
    
    html.H4("WHAT IS DOMESTIC VIOLENCE AND HOW TO IDENTIFY IT?"),
    html.P("Domestic violence means that in a relationship or marriage, one or both of the partners uses physical, sexual or psychological violence to try to get power or control over the other or due to losing their temper.Domestic violence can take many forms, including physical, emotional, sexual and financial abuse. ")
    ],color="danger", className="m-5"),
    html.B([row_0,row_1,row_2])
])
