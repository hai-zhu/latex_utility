# Original by Daniel L. Greenwald and Garrett Dash Nelson
# http://dlgreenwald.weebly.com/blog/capitalizing-titles-in-bibtex
# https://gist.github.com/garrettdashnelson/af0f8307393da37c6f94eda8c4613a4f
# Modified by Hai Zhu
# Date: 2018-10-26


"""This script replaces lowercase titles in BibTeX entries with titlecase
e.g., 'The greatest title of the all time' to 'The Greatest Title of All Time'."""


import re
from titlecase import titlecase

# Set path and name of bib files
directory = './'
my_file = 'ref.bib'
new_file = 'ref_title_all_cap.bib' # in case you don't want to overwrite

# Match title segment
pattern = re.compile(r'(\W*)(title={)(.*)(},)')

# Read in old file
with open(directory + my_file, 'r') as fid:
    lines = fid.readlines()

# Search for title strings and replace with titlecase
newlines = []
for line in lines:
    # Check if line contains title
    match_obj = pattern.match(line)
    if match_obj is not None:
        # Need to "escape" any special chars to avoid misinterpreting them in the regular expression.
        oldtitle = re.escape(match_obj.group(3))

        # Apply titlecase to get the correct title.
        newtitle = titlecase(match_obj.group(3))

        # Replace and add to list
        p_title = re.compile(oldtitle)
        newline = p_title.sub(newtitle, line)
        newlines.append(newline)
    else:
        # If not title, add as is.
        newlines.append(line)

# Print output to new file
with open (directory + new_file, 'w') as fid:
    fid.writelines(newlines)

