#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""Wordcount exercise
Google's Python class

The main() below is already defined and complete. It calls print_words()
and print_top() functions which you write.

1. For the --count flag, implement a print_words(filename) function that counts
how often each word appears in the text and prints:
word1 count1
word2 count2
...

Print the above list in order sorted by word (python will sort punctuation to
come before letters -- that's fine). Store all the words as lowercase,
so 'The' and 'the' count as the same word.

2. For the --topcount flag, implement a print_top(filename) which is similar
to print_words() but which prints just the top 20 most common words sorted
so the most common word is first, then the next most common, and so on.

Use str.split() (no arguments) to split on all whitespace.

Workflow: don't build the whole program at once. Get it to an intermediate
milestone and print your data structure and sys.exit(0).
When that's working, try for the next milestone.

Optional: define a helper function to avoid code duplication inside
print_words() and print_top().

"""

import sys
from bs4 import BeautifulSoup
import urllib

# +++your code here+++
# Define print_words(filename) and print_top(filename) functions.
# You could write a helper utility function that reads a file
# and builds and returns a word/count dict for it.
# Then print_words() and print_top() can just call the utility function.

#


def file_open(filename):
    f = open(filename, 'rU')
    filetext = {}
    for line in f:
        row = line.lower()
        row = row.split()
        for word in row:
            if word in filetext.keys():
                val = filetext.get(word)
                val += 1
                filetext[word] = val
            else:
                filetext[word] = 1
    return filetext


def url_open(url):
    """

    """
    soup = BeautifulSoup(urllib.urlopen(url))   #Creates unicode from page
    new_soup = soup.get_text()      #Unicode var type
    soup_words = new_soup.split()   #list var type
    word_dict = {}

    for item in soup_words:
        word = item.encode('utf-8').lower()
        if word in word_dict.keys():
            val = word_dict.get(word)
            val += 1
            word_dict[word] = val
        else:
            word_dict[word] = 1
    return word_dict


def print_words(filename):
    filetext = file_open(filename)
    for item in sorted(filetext.keys()):
        print item, ':', filetext[item]


def get_count(word_count):
    return word_count[1]


def print_top(filename):
    filetext = file_open(filename)
    items = sorted(filetext.items(), key=get_count, reverse=True)

    for items in items[:20]:
        print items[0], items[1]


def print_web(url):
    word_dict = url_open(url)
    for item in sorted(word_dict.keys()):
        print item, ':', word_dict[item]


# This basic command line argument parsing code is provided and
# calls the print_words() and print_top() functions which you must define.


def main():
    if len(sys.argv) != 3:
        print 'usage: ./wordcount.py {--count | --topcount | --url} file'
        sys.exit(1)

    option = sys.argv[1]
    source = sys.argv[2]
    if option == '--count':
        print_words(source)
    elif option == '--topcount':
        print_top(source)
    elif option == '--url':
        print_web(source)
    else:
        print 'unknown option: ' + option
        sys.exit(1)

if __name__ == '__main__':
    main()
