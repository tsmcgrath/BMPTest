# Replaces local pdf URL's with an external reference.
# Here's the logic:
# 1) open the replacement csv
# 2) read each line.
# 2a) while the html file is the same, perform all the replacements on identified on subsequent lines.
# 3) when html file is different, swap variable to new file, open, and replace. Loop to 2a.
# 4) close all files.
import os
import csv
from bs4 import BeautifulSoup
from bs4 import Comment

def replaceURL(html_file, orig_url, replace_url):
    # open the html file
    f = open(html_file, mode='r', encoding = 'utf-8')
    soup = BeautifulSoup(f, 'html.parser')
    # Replacing Impairment Issues
    target = soup.find("a", text= orig_url)
    if target is not None:
        mycomment =  Comment('Replacement comment for Impairment Issues')
        replacement = target.replace_with(replace_url)
    prettyHTML = soup.prettify()
    of = open(html_file, mode='w', encoding='utf-8')
    of.write(prettyHTML)
    of.close()
    f.close()

# 1) open the csv with replacement URL's
infile_path = '/Users/Tim/Code/Github/BMPTest/URLReplaceTest.csv'
with open(infile_path) as rf:
    for line in rf:
        elements = line.split()
        html_file = elements[0]
        orig_url = elements[1]
        replace_url = elements[2]
        replaceURL(html_file, orig_url, replace_url)
rf.close()
