import dash_bootstrap_components as dbc
def Navbar():
     navbar = dbc.NavbarSimple(
           children=[
              dbc.NavItem(dbc.NavLink("Home", href="apps/home.py")),
              dbc.NavItem(dbc.NavLink("Chatbox", href="apps/health.py")),
              dbc.NavItem(dbc.NavLink("About DV", href="apps/dem.py")),
              dbc.NavItem(dbc.NavLink("Emergency Help", href="apps/dash_version_dash_app.py")),
              dbc.NavItem(dbc.NavLink("Motivational", href="apps/dem.py")),

              
                    ],
          
          sticky="top",
        )
     return navbar
