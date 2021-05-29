"""
    Dash implementation of the dashboard showing YAMNet inference results
"""

"""
    Dash implementation of the dashboard showing YAMNet inference results
"""

from pathlib import Path
import os
from load_model1 import text_abuse_check

from yamnet_wrap import YamnetWrap
from yamnet_wrap.samples import samples
from app import app
from dash import Dash
from dash.exceptions import PreventUpdate
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
import numpy as np
import librosa
import speech_recognition as sr
import pyttsx3
#from pydub import AudioSegment
import smtplib
from email.mime.text import MIMEText
import warnings
warnings.filterwarnings("ignore")

own_path = Path(os.path.abspath(os.path.dirname(__file__)))
data_path = Path('assets/samples')

##import dash
##app = dash.Dash(__name__)
##server = app.server
## Dash application
##app = Dash(__name__,
##           external_stylesheets=[dbc.themes.BOOTSTRAP])


#def main():
""" Setup the layout of the Dash application """
select_file_options = [{'value': s['file'], 'label': s['title']} for s in samples]
PLOTLY_LOGO = "https://cdn2.vectorstock.com/i/thumb-large/24/26/happy-business-friends-logo-vector-1662426.jpg"
search_bar = dbc.Row(
    [
        dbc.Col(dbc.Button("Home",href="/apps/home", color="warning", className="ml-2",outline=True),
            width="auto"),
        dbc.Col(
            dbc.Button("Help",href="/apps/mot", color="warning", className="ml-2",outline=True),
            width="auto"),
        dbc.Col(
            dbc.Button("Chat",href="/apps/chat", color="warning", className="ml-2",outline=True),
            width="auto"),
        dbc.Col(
            dbc.Button("Emergency",href="/apps/eme", color="warning", className="ml-2"),
            width="auto"),
    ],
    no_gutters=True,
    className="ml-auto flex-nowrap mt-3 mt-md-0",
    align="center",
    )
layout = dbc.Container([
        dbc.Row(dbc.Col(dbc.Navbar(
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
        dbc.Jumbotron([
            html.H1('Sound Abuse recognition', className='mb-3'),
            dbc.Row([dbc.Col(dcc.Dropdown(id='select-file', options=select_file_options, value='',
                                          persistence=True, persistence_type='session'), width='md-6'),
                     dbc.Col(html.Audio(id='listen', controls=True), width='md-6')],
                    className='align-items-center mb-3'),
            html.H3(id='subtitle'),
            html.H5('',id='text-result'),
            html.H5('',id='abuse-result',style={'color':'red'}),
            dcc.Input(id='input-name',type='text',placeholder="Enter Your Name"),
            dcc.Input(id='input-email',type='text',placeholder="Enter Email id of friend"),
            html.A(id='mail-sent'),
            dcc.Loading(
                html.Div(id='graph_wrapper',
                         children=[dcc.Graph(id='waveform'),
                                   dcc.Graph(id='scores')])
            )
        ])
    ])
#    return app.server


@app.callback(Output('listen', 'src'),
              [Input('select-file', 'value')])
def select_audio(file_name):
    """ Set the URL of the audio player """
    if file_name is None or file_name == '':
        raise PreventUpdate

    file_url = str(own_path / data_path / file_name)
    return file_url


@app.callback(Output('graph_wrapper', 'hidden'),
              [Input('select-file', 'value')])
def show_graphs(file_name):
    """ Hide the plots when no file is selected """
    return file_name is None or file_name == ''


@app.callback([Output('subtitle', 'children'),
               Output('waveform', 'figure'),
               Output('scores', 'figure')],
              [Input('select-file', 'value')])
def select_file(file_name):
    """ Select a file => set subtitle and plots """
    if file_name is None or file_name == '':
        raise PreventUpdate

    file_path = str(own_path / data_path / file_name)

    # Read MP3 as mono at 16kHz
    waveform, sampling_rate = librosa.load(file_path, mono=True, sr=YamnetWrap.target_sampling_rate, duration=10)
    duration = len(waveform) / sampling_rate

    # Run the model, check the output.
    model = YamnetWrap.get_model()
    scores, embeddings, log_mel_spectrogram = model(waveform)

    topn = 20
    classes_top, scores_top = YamnetWrap.get_top_scores(topn, scores)

    figure_margins = dict(l=10, r=10, b=30, t=40)
    fig_time = go.Figure(layout=dict(title='Waveform', margin=figure_margins, height=300, xaxis=dict(title='Time [s]')))
    fig_time.add_scatter(x=np.arange(0, duration, 1 / sampling_rate), y=waveform)
    fig_score = go.Figure(layout=dict(title=f'Scores: top-{topn}', margin=figure_margins, height=300))
    fig_score.add_scatter(x=classes_top, y=scores_top)

    subtitle = f'Best average score: {classes_top[0]}'
    return subtitle, fig_time, fig_score

@app.callback(Output('text-result', 'children'),
              [Input('select-file', 'value')])
def speech_to_text(file_name):
    # Initialize the recognizer
    """ Set the URL of the audio player """
    if file_name is None or file_name == '':
        raise PreventUpdate

    audio_file_url = str(data_path / file_name)
    text = ""
    r = sr.Recognizer()
    try:
        audio = sr.AudioFile(audio_file_url)
        with sr.AudioFile(audio_file_url) as source:
            r.adjust_for_ambient_noise(source, duration=1)
            audio = r.record(source)
        text = r.recognize_google(audio)
    
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
          
    except sr.UnknownValueError:
        print("unknown error occured")
    return text
@app.callback(Output('abuse-result', 'children'),
              [Input('text-result', 'children')])
def abuse_text(text):
    result = text_abuse_check(text)
    if result:
        return "You are Suffering from abuse"
    else:
        return "You are not Suffering from abuse"

@app.callback(Output('mail-sent', 'children'),
              [Input('input-name', 'value'),
               Input('input-email', 'value')])
def abuse_text(name,email):
    if name is not None and email is not None:
        body="Your friend "+name+" is suffering from Abuse"
        msg=MIMEText(body)
        fromaddr = "Your Email"
        toaddr=email
        msg['From']=fromaddr
        msg['To']=toaddr
        msg['subject']="Help Against Abuse"
        serv=smtplib.SMTP('smtp-mail.outlook.com',587)
        serv.starttls()
        serv.login(fromaddr,"Your Password")
        serv.send_message(msg)
        serv.quit()
        return "mail sent"
    else:
        return ""

#if __name__ == '__main__':
 #   main()
  #  app.run_server(debug=True,port=8050)
