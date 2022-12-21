#importing libraries
import snscrape.modules.twitter as sntwitter
import pandas as pd
import nltk
from nltk.corpus import stopwords
import string 
import re


nltk.download('punkt')
nltk.download('stopwords')


def sentence_cleaning(df,other_words):
    stop = stopwords.words('english') #get all stop words
    df= df.str.lower() #converting all text to lowercase
    new_df = df.apply(lambda x: ' '.join([word for word in x.split() if word
                                          not in (stop)]))
    #removing all the stop words
    other_stopwords = set(other_words)
    #removing other words that has been defined like keywords
    f = lambda x: ' '.join(w for w in x.split() if not w in other_stopwords)
    new_df = new_df.apply(f)
    #removing punctuation marks
    new_df = new_df.str.replace('[^\w\s]','')
    #removing emojis
    new_df = new_df.str.replace('[^A-Za-z0-9]', ' ', flags=re.UNICODE)
    return new_df