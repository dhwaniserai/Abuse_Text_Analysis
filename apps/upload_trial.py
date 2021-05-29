##import base64
##import os
##from urllib.parse import quote as urlquote
##
##from flask import Flask, send_from_directory
##import dash
##import dash_core_components as dcc
##import dash_html_components as html
##from dash.dependencies import Input, Output
##
##import speech_recognition as sr
##import pyttsx3
##from pydub import AudioSegment
##
##def speech_to_text(audio_file):
##    # Initialize the recognizer 
##    r = sr.Recognizer()
##    try:
##        audio = sr.AudioFile(audio_file)
##        with sr.AudioFile(audio_file) as source:
##            audio = r.record(source)
##        text = r.recognize_google(audio)
##    
##    except sr.RequestError as e:
##        print("Could not request results; {0}".format(e))
##          
##    except sr.UnknownValueError:
##        print("unknown error occured")
##    return text
##
##    
##UPLOAD_DIRECTORY = "project/app_uploaded_files"
##
##if not os.path.exists(UPLOAD_DIRECTORY):
##    os.makedirs(UPLOAD_DIRECTORY)
##
##
### Normally, Dash creates its own Flask server internally. By creating our own,
### we can create a route for downloading files directly:
##server = Flask(__name__)
##app = dash.Dash(server=server)
##
##
##@server.route("/download/<path:path>")
##def download(path):
##    """Serve a file from the upload directory."""
##    return send_from_directory(UPLOAD_DIRECTORY, path, as_attachment=True)
##
##
##app.layout = html.Div(
##    [
##        html.H1("File Browser"),
##        html.H2("Upload"),
##        dcc.Upload(
##            id="upload-data",
##            children=html.Div(
##                ["Drag and drop or click to select a file to upload."]
##            ),
##            style={
##                "width": "100%",
##                "height": "60px",
##                "lineHeight": "60px",
##                "borderWidth": "1px",
##                "borderStyle": "dashed",
##                "borderRadius": "5px",
##                "textAlign": "center",
##                "margin": "10px",
##            },
##            multiple=True,
##        ),
##        html.H2("File List"),
##        html.Ul(id="file-list"),
##    ],
##    style={"max-width": "500px"},
##)
##
##
##def save_file(name, content):
##    """Decode and store a file uploaded with Plotly Dash."""
##    data = content.encode("utf8").split(b";base64,")[1]
##    with open(os.path.join(UPLOAD_DIRECTORY, name), "wb") as fp:
##        fp.write(base64.decodebytes(data))
##
##
##def uploaded_files():
##    """List the files in the upload directory."""
##    files = []
##    for filename in os.listdir(UPLOAD_DIRECTORY):
##        path = os.path.join(UPLOAD_DIRECTORY, filename)
##        if os.path.isfile(path):
##            files.append(filename)
##        
##    return files
##
##
##def file_download_link(filename):
##    """Create a Plotly Dash 'A' element that downloads a file from the app."""
##    location = "/download/{}".format(urlquote(filename))
##    return html.A(filename, href=location)
##
##
##@app.callback(
##    Output("file-list", "children"),
##    [Input("upload-data", "filename"), Input("upload-data", "contents")],
##)
##def update_output(uploaded_filenames, uploaded_file_contents):
##    """Save uploaded files and regenerate the file list."""
##    text=""
##    if uploaded_filenames is not None and uploaded_file_contents is not None:
##        for name, data in zip(uploaded_filenames, uploaded_file_contents):
##            save_file(name, data)
##            if 'm4a' in name:
##                print(type(data))
##                path = os.path.join(UPLOAD_DIRECTORY, name)
##                m4a_version = AudioSegment.from_file(path)
##                data = m4a_version.export("abc.wav",format = "wav")
##                text = speech_to_text(data)
##                print(text)
##            if 'wav' in name:
##                #print(type(data))
##                path = os.path.join(UPLOAD_DIRECTORY, name)
##
##                text = speech_to_text(path)
##                print(text)
##
##    files = uploaded_files()
##    if len(files) == 0:
##        return [html.Li("No files yet!")]
##    else:
##        return [html.Li(file_download_link(filename)) for filename in files]#,html.A(text)
##if __name__ == '__main__':
##    app.run_server(debug=True,port=8053)
##
import dash
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc

import plotly.graph_objects as go
import numpy as np
import librosa
import base64
import datetime
import io
import itertools
from dash.dependencies import Input, Output, State
from pathlib import Path
import os
from flask import Flask, send_from_directory
import dash

server = Flask(__name__)
app = dash.Dash(server=server,external_stylesheets=[dbc.themes.BOOTSTRAP])

import dash_bootstrap_components as dbc
PLOTLY_LOGO = "https://cdn2.vectorstock.com/i/thumb-large/24/26/happy-business-friends-logo-vector-1662426.jpg"


search_bar = dbc.Row(
    [
        dbc.Col(dbc.Button("Home",href="", color="warning", className="ml-2",outline=True),
            width="auto"),
        dbc.Col(
            dbc.Button("Help",href="", color="warning", className="ml-2",outline=True),
            width="auto"),
        dbc.Col(
            dbc.Button("Chat",href="", color="warning", className="ml-2",outline=True),
            width="auto"),
        dbc.Col(
            dbc.Button("Emergency",href="", color="warning", className="ml-2"),
            width="auto"),
    ],
    no_gutters=True,
    className="ml-auto flex-nowrap mt-3 mt-md-0",
    align="center",
)
row_1=html.Iframe(src=app.get_asset_url("audio_record.html"),style={"height":"500px","width":"500px"})

import base64
import os
from urllib.parse import quote as urlquote

from flask import Flask, send_from_directory
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import speech_recognition as sr
import pyttsx3
from pydub import AudioSegment

def speech_to_text(audio_file):
    # Initialize the recognizer 
    r = sr.Recognizer()
    try:
        audio = sr.AudioFile(audio_file)
        with sr.AudioFile(audio_file) as source:
            audio = r.record(source)
        text = r.recognize_google(audio)
    
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
          
    except sr.UnknownValueError:
        print("unknown error occured")
    return text

    
UPLOAD_DIRECTORY = "project/app_uploaded_files"

if not os.path.exists(UPLOAD_DIRECTORY):
    os.makedirs(UPLOAD_DIRECTORY)


# Normally, Dash creates its own Flask server internally. By creating our own,
# we can create a route for downloading files directly:
server = Flask(__name__)
app = dash.Dash(server=server)


@server.route("/download/<path:path>")
def download(path):
    """Serve a file from the upload directory."""
    return send_from_directory(UPLOAD_DIRECTORY, path, as_attachment=True)


audio_layout = dbc.Jumbotron(
    [
        #html.H1("File Browser"),
        html.H2("Upload"),
        dcc.Upload(
            id="upload-data",
            children=html.Div(
                ["Drag and drop or click to select a file to upload."]
            ),
            style={
                "width": "100%",
                "height": "60px",
                "lineHeight": "60px",
                "borderWidth": "1px",
                "borderStyle": "dashed",
                "borderRadius": "5px",
                "textAlign": "center",
                "margin": "10px",
            },
            multiple=True,
        ),
        html.H2("File List"),
        html.Ul(id="file-list"),
    ],
    style={"max-width": "500px"},
)


def save_file(name, content):
    """Decode and store a file uploaded with Plotly Dash."""
    data = content.encode("utf8").split(b";base64,")[1]
    with open(os.path.join(UPLOAD_DIRECTORY, name), "wb") as fp:
        fp.write(base64.decodebytes(data))


def uploaded_files():
    """List the files in the upload directory."""
    files = []
    for filename in os.listdir(UPLOAD_DIRECTORY):
        path = os.path.join(UPLOAD_DIRECTORY, filename)
        if os.path.isfile(path):
            files.append(filename)
        
    return files


def file_download_link(filename):
    """Create a Plotly Dash 'A' element that downloads a file from the app."""
    location = "/download/{}".format(urlquote(filename))
    return html.A(filename, href=location)


@app.callback(
    Output("file-list", "children"),
    [Input("upload-data", "filename"), Input("upload-data", "contents")],
)
def update_output(uploaded_filenames, uploaded_file_contents):
    """Save uploaded files and regenerate the file list."""
    text="abc"
    if uploaded_filenames is not None and uploaded_file_contents is not None:
        for name, data in zip(uploaded_filenames, uploaded_file_contents):
            save_file(name, data)
            if 'wav' in name:
                #print(type(data))
                path = os.path.join(UPLOAD_DIRECTORY, name)

                text = speech_to_text(path)
                print(text)

    files = uploaded_files()
    if len(files) == 0:
        return [html.Li("No files yet!")]
    else:
        #return html.A(text)
        return [html.Li(file_download_link(filename)) for filename in files]#,html.A(text)



app.layout = html.Div([ dbc.Row(dbc.Col(dbc.Navbar(
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
    ],color="dark",dark=False,),
    )
    ),
    dbc.Row(dbc.Col(html.B([row_1]))),
    dbc.Row(dbc.Col([audio_layout])),
    dbc.Row(dbc.Col(html.Img(src="waveform.png",height="100px",alt="waveform")))
    
],style={"background-color":"lightblue",'background-size':'100% 100%'})
#])
if __name__ == '__main__':
    app.run_server(debug=True,port=8051)
