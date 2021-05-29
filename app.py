import dash
import dash_bootstrap_components as dbc

#external_stylesheets = [dbc.themes.BOOTSTRAP]
external_stylesheets = ['https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css','https://rawgit.com/jimmybow/CSS/master/visdcc/DataTable/Filter.css',' https://cdnjs.cloudflare.com/ajax/libs/vis/4.20.1/vis.min.css','https://cdnjs.cloudflare.com/ajax/libs/bootstrap-tour/0.12.0/js/bootstrap-tour.min.js']

DBC_DOCS = "https://dash-bootstrap-components.opensource.faculty.ai/"
DBC_GITHUB = "https://github.com/facultyai/dash-bootstrap-components"

#app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

app = dash.Dash(__name__,external_stylesheets=external_stylesheets, suppress_callback_exceptions=True)
app.title='SAKHI'
server = app.server
