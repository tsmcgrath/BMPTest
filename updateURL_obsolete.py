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

count = 0

# 1) open the csv with replacement URL's
infile_path = '/Users/Tim/Code/Github/BMPTest/URLReplaceTest.csv'
with open(infile_path) as rf:
    reader = csv.DictReader(rf)
    for row in reader:
        line = str(row)
        elements = line.split(',')
        html_file = elements[0] # .strip('"')
        # orig_url = elements[1] # .strip('"')
        orig_url = elements[1]
        replace_url = elements[2] # .strip()
        # replace_url = replace_url.strip('"') # make sure all double quotes are stripped.
        replace_url = replace_url.replace('"', "")
        f = open(html_file, mode='r', encoding = 'utf-8')
        soup = BeautifulSoup(f, 'html.parser')
        f.close()
        # Replacing URL
        target = soup.find('a', href = orig_url)
        if target is not None:
            count += 1
            print('replacing', count)
            replacement = target.replace_with(replace_url)
        prettyHTML = soup.prettify()
        of = open(html_file, mode='w', encoding='utf-8')
        of.write(prettyHTML)
        of.close()
rf.close()
