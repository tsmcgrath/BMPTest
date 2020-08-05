# Replaces footer copyright notice.
import os
import sys
import csv
from bs4 import BeautifulSoup
count = 0
# The top argument for the directory walk
topdir = '/Users/Tim/Code/Github/BMPTest'
# The extension to search for
exten = '.html'
copyrightstring = '© TPWD 2020. All Rights Reserved.'
for dirpath, dirnames, files in os.walk(topdir):
    for name in files:
        if name.lower().endswith(exten):
            print(os.path.join(dirpath, name))
            file_path = os.path.join(dirpath, name)
            with open(file_path, mode='r', encoding = 'utf-8') as f:
                soup = BeautifulSoup(f, 'html.parser')
               # Replacing Copyright
                footer = soup.find("div", {"id": "footer"})

                footer.insert(0, soup.new_tag('style', type='text/css'))
                footer.style.insert(0, soup.new_tag('font', color="red"))
                if footer:
                    para = footer.find("p")
                    para.clear()
                    print(para)
                    # set the footer font color
                    para['style'] = "color:white"
                    para.insert(0, copyrightstring)
                    print(para)
                    prettyHTML = soup.prettify()
                    of = open(file_path, mode='w', encoding='utf-8')
                    of.write(prettyHTML)
                    of.close()
                    f.close()
