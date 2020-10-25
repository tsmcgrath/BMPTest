# python script to list the contents of sidebars on static html pages
from bs4 import BeautifulSoup
import os
# The top argument for the directory walk
topdir = '.'

# The extension to search for
exten = '.html'

for dirpath, dirnames, files in os.walk(topdir):
    for name in files:
        if name.lower().endswith(exten):
            # print(os.path.join(dirpath, name))
            file_path = os.path.join(dirpath, name)
            f = open(file_path, "r+")
            soup = BeautifulSoup(f, 'html.parser')
            # soupbar = soup.find("div", "sidebar-content")
            # sbar_menu = soupbar.findall("li", {"class": "li-content text-body"})
            # sbars = soup.find_all(text=re.compile('sidebar'))
            mydivs = soup.find_all("div", class_= "post")
            for div in mydivs:
                ref = div.find('li', href=False)
                print(file_path)
                print("==========================")
                print(div)
