# Sklearn running in pycharm virtual environment

# NLTK library of language resources
import nltk, re 
nltk.download('omw-1.4')
from nltk import pos_tag, word_tokenize # Part of speech tagging and tokenisation
from nltk.stem import wordnet, WordNetLemmatizer # to perform lemmatisation

# ML tools
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer # to perform bow and tfidf
from sklearn.metrics import pairwise_distances # For cosine similarity

# Data processing and visualisation
import numpy as np
import pandas as pd
from IPython.display import Image

from nltk_utils import clean_input, normalise_text

# Read in data
df = pd.read_excel("data/dialog_talk_agent.xlsx")
df.ffill(axis = 0, inplace = True) # Replace null values with previous value
df["lemmatised_text"] = df["Context"].apply(normalise_text) # apply the normalise_text function to each entry in the context column

tfidf = TfidfVectorizer() # Initialise sklearn tfidf
x_tfidf = tfidf.fit_transform(df["lemmatised_text"]).toarray()
df_tfidf = pd.DataFrame(x_tfidf, columns = tfidf.get_feature_names_out())

# count vectoriser can be used instead of tfidf 
# cv = CountVectorizer()
# X = cv.fit_transform(df["lemmatised_text"]).toarray()
# features = cv.get_feature_names_out()
# df_bow = pd.DataFrame(X, columns = features)

def chat_response(text): # chat_tfidf
    # Lemmatised utterance
    text = normalise_text(text)
    text_tfidf = tfidf.transform([text]).toarray()
    # cos calculates similarity between utterance and each entry in the dataset
    cos = 1 - pairwise_distances(df_tfidf, text_tfidf, metric = "cosine")
    index_value = cos.argmax()

    # Get the response of the most similar entry 
    return df["Text Response"].loc[index_value] 


#input = "Help me!"
#input = "It's quite easy to improve that, isn't it!"
#print(response(input))
#print(chat_tfidf(input))