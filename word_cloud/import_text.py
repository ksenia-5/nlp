#!/usr/bin/env python

import urllib.request, urllib.response, urllib.parse, urllib.error
#url = "http://www.gutenberg.org/files/2554/2554-0.txt"
def read_text_url(url = "https://www.gutenberg.org/cache/epub/21339/pg21339.txt", encoding = 'utf8',n_char_display=15):
    
    '''
    Function reads in raw text file from specified URL, 
    with default encoding = UTF8.
    The first 100 characters are printed, along with character length of file.
    
    example use:
    
    read_text_url(url = "https://www.gutenberg.org/cache/epub/21339/pg21339.txt")
    
    '''
    response = urllib.request.urlopen(url)
    raw = response.read().decode(encoding)
    print("Read file from {}.".format(url))
    print(raw[:n_char_display])
    print("Length of raw file is {} characters.".format(len(raw)))
    return raw
