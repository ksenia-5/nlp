# NLTK library of language resources
import nltk, re 
nltk.download('omw-1.4')
from nltk import pos_tag, word_tokenize # Part of speech tagging and tokenisation
from nltk.stem import wordnet, WordNetLemmatizer # to perform lemmatisation
from nltk.corpus import stopwords # stopwords

# Define function to normalise text input
def normalise_text(text):
    '''
    Function takes a text string (utterance) as input, 
    converts to lowercase, 
    removes special characters and punctuation, 
    tokenises, POS-tags and lemmatises each token..
    Joins lemmatised tokens, and returns lemmatised string.
    '''
    text = str(text).lower() # convert to lowercase
    text = re.sub(r'[^a-z0-9]', " ",text) # remove special characters
    tokens = word_tokenize(text) # tokenise
    
    # Initialise lemmatiser
    lemmatiser = wordnet.WordNetLemmatizer()
    
    # Part of speech (POS) tagging, tagset set to default
    tagged_tokens =  pos_tag(tokens, tagset = None)
    
    #-------- Can split here

    # Empty list
    token_lemmas = []
    for (token, pos_token) in tagged_tokens:
        if pos_token.startswith("V"): # verb
            pos_val = "v"
        elif pos_token.startswith("J"): # adjective
            pos_val = "a"
        elif pos_token.startswith("R"): # adverb
            pos_val = "r"
        else:
            pos_val = 'n' # noun
        # lemmatise and append to list of lemmatised tokens
        token_lemmas.append(lemmatiser.lemmatize(token, pos_val))
    
    return " ".join(token_lemmas)


# Define function to remove stopwords
def remove_stopwords(text):
    
    # stopwords
    stop = stopwords.words("english")
    
    #if token not in stop
    text = [word for word in text.split() if word not in stop]
    return " ".join(text)


def clean_input(raw_input):
    text = remove_stopwords(raw_input)
    clean_text = normalise_text(text)
    return clean_text