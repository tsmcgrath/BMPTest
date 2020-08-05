# Replaces local pdf URL's with an external reference.
import os
import sys
import csv
from bs4 import BeautifulSoup
count = 0
script_path = os.path.abspath(os.path.dirname(sys.argv[0]))
infile_path = os.path.join(script_path, './Update BMP URL Target_v2.csv')
with open(infile_path) as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        html_file = row[0]
        orig_url = row[1]
        replace_url = row[2]
        html_file_path = os.path.abspath(os.path.join(script_path, *html_file.split('/')))
        prettyHTML = None
        with open(html_file_path, mode='r', encoding = 'utf-8') as f:
            soup = BeautifulSoup(f, 'html.parser')
            # Replacing URL
            target = soup.find('a', href = orig_url)
            if target:
                count += 1
                print('replacing', count)
                target['href'] = replace_url
                # replacement = target.replace_with(replace_url)
            prettyHTML = soup.prettify()
        if prettyHTML:
            with open(html_file_path, mode='w', encoding='utf-8') as of:
                of.write(prettyHTML)
