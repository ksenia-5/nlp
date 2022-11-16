#!/usr/bin/env python

from import_text import*
import nltk, re, pprint
from nltk import word_tokenize

# Read in raw text from url
raw = read_text_url(n_char_display=22)

# Use the find and rfind (reverse find) statements to find
# where the text starts and finishes.
# print(raw.find("PART I"))
# 1937
# print(raw.rfind("End of Project Gutenberg"))
# -1

# To display the table of contents and identify which parts of text is wanted
# print(raw[:1937+1])

# Find where the second play starts
# print(raw.rfind("The Dutch Lover"))
# 692593

# Slice the raw text to remove unwanted text at the start
raw = raw[1937:692593]
print("After slicing the raw text is {} characters.".format(len(raw)))

# to check raw text starts with "PART I"
# print(raw.find('PART I'))

# Tokenise raw text, making a list of words and punctuation
tokens = word_tokenize(raw)
n_tokens = len(tokens)
print("the number of tokens is {}.".format(n_tokens))

# Create a text object to give access to nltk.Text methods
text = nltk.Text(tokens)
