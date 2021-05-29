import speech_recognition as sr
import pyttsx3 

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
UPLOAD_DIRECTORY = "project/app_uploaded_files/"
file = "Recording_62.m4a"
file_path = UPLOAD_DIRECTORY + file
text = speech_to_text(file_path)
print(text)
