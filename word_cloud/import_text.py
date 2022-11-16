# #!/usr/bin/env python

import urllib.request, urllib.response, urllib.parse, urllib.error
#url = "http://www.gutenberg.org/files/2554/2554-0.txt"
def read_text_url(url = "https://www.gutenberg.org/cache/epub/21339/pg21339.txt", encoding = 'utf8'):
    '''Function reads in raw text file from specified URL, and default encoding = UTF8'''
    response = urllib.request.urlopen(url)
    raw = response.read().decode(encoding)
    print("Read file from {}.".format(url))
    print(raw[:100])
    print("Length of raw file is {} characters.".format(len(raw)))
    return raw
read_text_url(url = "https://www.gutenberg.org/cache/epub/21339/pg21339.txt")