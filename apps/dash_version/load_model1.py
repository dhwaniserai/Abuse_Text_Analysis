import pandas as pd
import numpy as np
import nltk
from tensorflow import keras
from tensorflow.keras.preprocessing.text import Tokenizer
from sklearn.model_selection import train_test_split
import os
import warnings
warnings.filterwarnings("ignore")

own_path = str(os.path.abspath(os.path.dirname(__file__)))
data_path  = "datasets/OLIDv1.0/olid-training-v1.0.tsv"
file_path = own_path+'/'+data_path
twitter_data={}
twitter_data["train"] = pd.read_csv(file_path, encoding = "ISO-8859-1", sep='\t')


twitter_data['train']['subtask_a'][twitter_data['train']['subtask_a']== 'NOT']=0
twitter_data['train']['subtask_a'][twitter_data['train']['subtask_a']== 'OFF']=1

X=np.asarray(twitter_data['train']['tweet'])
Y=np.asarray(twitter_data['train']['subtask_a']).astype(np.int)
sent=['I will kill you if you do this again. Stop threatening']
def text_abuse_check(text):
    ## Less than 0.4 is abusive else no abusive = True
    sent = [text]
    X_trial = np.array(sent)

    max_vocab=30000
    tokenizer = Tokenizer(num_words=max_vocab,filters='@')
    tokenizer.fit_on_texts(X)
    max_length=20
    X_vectorized=tokenizer.texts_to_sequences(X)

    X_trial_vectorized = tokenizer.texts_to_sequences(X_trial)

    X_pad = keras.preprocessing.sequence.pad_sequences(X_vectorized,max_length,padding='post',
                                                       truncating='post')
    X_trial_pad = keras.preprocessing.sequence.pad_sequences(X_trial_vectorized,max_length,padding='post',
                                                       truncating='post')

    model_1 = keras.models.load_model(own_path+"/"+"deep_abuse_model1_20")
    prediction = model_1.predict(X_trial_pad)[0][0]
    print(model_1.predict(X_trial_pad))
    return prediction < 0.45

print(text_abuse_check('I will kill you if you do this again. Stop threatening'))
