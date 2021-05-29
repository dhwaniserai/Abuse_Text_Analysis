import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash
from app import app
from apps import home,mot,eme,chat
import sys
sys.path.append('apps/dash_version')
sys.path.append('apps/dash_version/datasets')
sys.path.append('assets/samples')

import dash_app
#from apps/dash_version import dash_app
# Normally, Dash creates its own Flask server internally. By creating our own,
# we can create a route for downloading files directly:


app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

 
@app.callback(Output('page-content', 'children'),
              Input('url', 'pathname'))
def display_page(pathname):
    if pathname == '/apps/home':
        return home.layout
    elif pathname == '/apps/mot':
        return mot.layout
    elif pathname == '/apps/chat':
        return chat.layout
    elif pathname == '/apps/eme':
        
        return dash_app.layout
    else:
        return home.layout

if __name__ == '__main__':
    app.run_server(debug=True,port=8051)
