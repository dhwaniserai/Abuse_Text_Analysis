import dash
import dash_html_components as html

import dash_bootstrap_components as dbc
PLOTLY_LOGO = "https://cdn2.vectorstock.com/i/thumb-large/24/26/happy-business-friends-logo-vector-1662426.jpg"

search_bar = dbc.Row(
    [
        dbc.Col(dbc.Button("Home",href="/apps/home", color="warning", className="ml-2",outline=True),
            width="auto"),
        dbc.Col(
            dbc.Button("Help",href="/apps/mot", color="warning", className="ml-2"),
            width="auto"),
        dbc.Col(
            dbc.Button("Chat",href="/apps/chat", color="warning", className="ml-2",outline=True),
            width="auto"),
        dbc.Col(
            dbc.Button("Emergency ",href="/apps/eme", color="warning", className="ml-2",outline=True),
            width="auto"),
    ],
    no_gutters=True,
    className="ml-auto flex-nowrap mt-3 mt-md-0",
    align="center",
)
card_content1 = [
    dbc.CardHeader("Protection of Women against Domestic Violence Act, 2005"),
    dbc.CardBody(
        [
            #html.H5("Card title", className="card-title"),
            html.P("This is an act of the Indian Parliament enacted to protect women from Domestic Violence. It prohibits a wide range of Physical, Sexual, Emotional & Economical abuse against women and all these are broadly defined under the Act. It provides security to women in a family from men in a family. The extent of the Act covers not only the protection of women who are married to men but also women who are in Live-in-relationship, just as family members including Grandmothers, Mothers, etc. A women has right to be liberated from any type of violence under this Act. Under this law, women can look for security against Domestic Violence, Financial Compensation, Right to live in their mutual house and they can get maintenance from their abuser in case they are living separated.This law is to guarantee that women don’t get kicked out of their own house and can support themselves if they have been abused. It also ensure the protection of women from their abusers.",
                className="card-text",
            ),
        ]
    ),
]
card_content2 = [
    dbc.CardHeader("Section 498A of the IPC (Indian Penal Code)"),
    dbc.CardBody(
        [
           # html.H5("Card title", className="card-title"),
			html.P("This is a Criminal Law, which applies to husbands or family members of husband who are merciless to women. Under Section 498A of the IPC, harassment for Dowry by the family members of the husband or by husband is recognized as a Crime. This harassment can be of any type either Physical or Mental. Despite the fact that Marital Rape isn’t considered as a Crime in India, forced sex with one’s wife can be viewed as Cruelty under this Section. Section 498A has a vast scope. It also includes any and all intentional behaviours against a women which force the women to attempt suicide or risk to life or grave injury or risk to limb or overall health. Here, health incorporates the physical and mental health of the women.",className="card-text"),
        ]
    ),
]
card_content3= [
    dbc.CardHeader("Dowry Prohibition Act, 1961"),
    dbc.CardBody(
        [
           # html.H5("Card title", className="card-title"),
			html.P("This is a Criminal Law that punishes the giving and taking of Dowry. The tradition of dowry itself is banned under the Dowry Prohibition Act, 1961. According to this law, gives, takes or even demands dowry, they can be imprisoned for a half year (i.e. for 6 months) or they can be fined upto Five Thousand Rupees.",    			className="card-text",
            ),
        ]
    ),
]
card_content4 = [
    dbc.CardHeader("Azad foundation"),
    dbc.CardBody(
        [
            #html.H5("Card title", className="card-title"),
            html.P(["Set up in May 2008, the foundation has expanded its reach from New Delhi, and opened offices in Jaipur, Indore, and Kolkata.",html.Br(),"Contact Tel: +91 11 4060 1878",html.Br(), "Email: azadfoundation@gmail.com",html.Br()," Website: http://www.azadfoundation.com/",
                ],className="card-text",
            ),
        ]
    ),
]
card_content5= [
    dbc.CardHeader("Angala"),
    dbc.CardBody(
        [
            #html.H5("Card title", className="card-title"),
            html.P(["Angala (meaning the courtyard) is the women’s crisis intervention centre of Bengaluru-based women’s organisation, Vimochana. The centre was set up in 1993 Intervention Centre:",html.Br()," Tel: +91-80-25492781 / 25494266",html.Br()," Email:  angala1@vsnl.net",]
                ,className="card-text",
            ),
        ]
    ),
]
card_content6 = [
    dbc.CardHeader("Urja Trust Foundation"),
    dbc.CardBody(
        [
            #html.H5("Card title", className="card-title"),
            html.P(["The Urja Trust was founded in 2012 by Deepali Vandana and Altaf Shaikh, Mumbai-based social workers. Urja opened its first centre at Dadar, Mumbai. It is a non-government organisation that provides shelter to women who are homeless or have run away due to domestic violence.",html.Br(),"Contact Number: 022 2412 4397 ",
                ],className="card-text",
            ),
        ]
    ),
]
card_content7 = [
    dbc.CardHeader("Protection of Women against Domestic Violence Act, 2005"),
    dbc.CardBody(
        [
            #html.H5("Card title", className="card-title"),
            html.P("This is an act of the Indian Parliament enacted to protect women from Domestic Violence. It prohibits a wide range of Physical, Sexual, Emotional & Economical abuse against women and all these are broadly defined under the Act. It provides security to women in a family from men in a family. The extent of the Act covers not only the protection of women who are married to men but also women who are in Live-in-relationship, just as family members including Grandmothers, Mothers, etc. A women has right to be liberated from any type of violence under this Act. Under this law, women can look for security against Domestic Violence, Financial Compensation, Right to live in their mutual house and they can get maintenance from their abuser in case they are living separated.This law is to guarantee that women don’t get kicked out of their own house and can support themselves if they have been abused. It also ensure the protection of women from their abusers.Contact Tel: +91 11 4060 1878 Email: azadfoundation@gmail.com Website: http://www.azadfoundation.com/",
                className="card-text",
            ),
        ]
    ),
]
row_1 = dbc.Row(
    [
        dbc.Col(dbc.Card(card_content1, color="success", outline=True)),
        dbc.Col(dbc.Card(card_content2, color="success", outline=True)),
    ],
    style={"margin-left":"50px","margin-right":"50px","margin-bottom":"20px"},
)
row_2 = dbc.Row(
    [
        dbc.Col(dbc.Card(card_content3, color="success", outline=True)),
        #dbc.Col(dbc.Card(card_content4, color="danger", outline=True)),
    ],
    style={"margin-left":"50px","margin-right":"50px"},
)
row_3 =dbc.Row([
dbc.Alert([
    
    html.H4("NGOS IN INDIA YOU CAN APPROACH FOR HELP"),
    #html.P("Domestic violence means that in a relationship or marriage, one or both of the partners uses physical, sexual or psychological violence to try to get power or control over the other or due to losing their temper.Domestic violence can take many forms, including physical, emotional, sexual and financial abuse. ")
    ],color="success", className="m-5"),
])
row_4 = dbc.Row(
    [
        dbc.Col(dbc.Card(card_content4, color="success", outline=True)),
        dbc.Col(dbc.Card(card_content5, color="success", outline=True)),
    ],
    style={"margin-left":"50px","margin-right":"50px","margin-bottom":"20px"},
)
row_5 = dbc.Row(
    [
        dbc.Col(dbc.Card(card_content6, color="success", outline=True)),
        #dbc.Col(dbc.Card(card_content4, color="danger", outline=True)),
    ],
    style={"margin-left":"50px","margin-right":"50px"},
)
row_6 =dbc.Row([
dbc.Alert([
    
    html.H4("MOTIVATIONAL VIDEOS"),
    #html.P("Domestic violence means that in a relationship or marriage, one or both of the partners uses physical, sexual or psychological violence to try to get power or control over the other or due to losing their temper.Domestic violence can take many forms, including physical, emotional, sexual and financial abuse. ")
    ],color="success", className="m-5"),
])
row_7=dbc.Row([
dbc.Col(html.Iframe(src="https://www.youtube.com/embed/7PpEuG7YfeE",style={"width":"853px","height":"480px","margin-left":"200px"})),
dbc.Col(html.Iframe(src="https://www.youtube.com/embed/iCwKM6uB71I",style={"width":"853px","height":"480px","margin-left":"200px"})),
])
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
    
    html.H4("LEGAL SUPPORT:LAWS ON DOMESTIC VIOLENCE"),
    #html.P("Domestic violence means that in a relationship or marriage, one or both of the partners uses physical, sexual or psychological violence to try to get power or control over the other or due to losing their temper.Domestic violence can take many forms, including physical, emotional, sexual and financial abuse. ")
    ],color="success", className="m-5"),
    html.B([row_1,row_2,row_3,row_4,row_5,row_6,row_7])
])
