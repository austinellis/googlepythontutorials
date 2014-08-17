#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import csv

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""


def file_open(filename):
    """
    Opens a file and returns the entire contents of that file in a
    single string
    """
    f = open(filename, 'rwU')
    filecontents = f.read()
    f.close()
    return filecontents


def extract_names(filename):
    """
    Given a file name for baby.html, returns a list starting with the year string
    followed by the name-rank strings in alphabetical order.
    ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
    """
    # +++your code here+++
    filecontents = file_open(filename)
    output_names = []
    match_year = re.search(r'Popularity in (\d\d\d\d)', filecontents)
    #match_names is a list of tuples
    tpl_match_names = re.findall(r'<td>(\d+)</td><td>(\w+)</td>''<td>(\w+)</td>', filecontents)
    output_names.append(match_year.group(1))
    dict_names = {}
    for rank, boy_name, girl_name in tpl_match_names:
        if boy_name not in dict_names:
            dict_names[boy_name] = rank
        if girl_name not in dict_names:
            dict_names[girl_name] = rank
    sorted_dict_names = sorted(dict_names.keys())
    for name in sorted_dict_names:
        output_names.append(name + ' ' + dict_names[name])
    #print type(output_names)
    #print type(output_names[20])
    return output_names


def write_file(filename, filecontents):
    """
    This function takes a filename and file contents and writes them to a text file
    """

def main():
    # This command-line parsing code is provided.
    # Make a list of command line arguments, omitting the [0] element
    # which is the script itself.
    args = sys.argv[1:]

    if not args:
        print 'usage: [--summaryfile] file [file ...]'
        sys.exit(1)

    # Notice the summary flag and remove it from args if it is present.
    summary = False
    if args[0] == '--summaryfile':
        summary = True
        del args[0]
    if args[0] == '--summarycsv':
        summary_csv = True
        del args[0]

    # +++your code here+++
    # For each filename, get the names, then either print the text output
    # or write it to a summary file
    #if summary == True:
    #    pass

    for arg in args:
        names_list = extract_names(arg)
        print type(names_list)
        text = '\n'.join(names_list)

        if summary == True:
            summary_output_file = open(arg + '.summary', 'w')
            summary_output_file.write(text + '\n')
            summary_output_file.close()
        elif summary_csv == True:
            summary_output_csv = open(arg + '.csv', 'wb')
            writer = csv.writer(summary_output_csv, delimiter=' ', quotechar=' ', quoting=csv.QUOTE_ALL)
            writer.writerows(names_list)

        else:
            print text


if __name__ == '__main__':
    main()
