# python script to list the contents of sidebars on static html pages
from bs4 import BeautifulSoup
from bs4 import Comment
import os
# The top argument for the directory walk
topdir = '.'

# The extension to search for
exten = '.test'

for dirpath, dirnames, files in os.walk(topdir):
    for name in files:
        if name.lower().endswith(exten):
            # print(os.path.join(dirpath, name))
            file_path = os.path.join(dirpath, name)
            f = open(file_path, mode='r', encoding = 'utf-8')
            soup = BeautifulSoup(f, 'html.parser')
            # soupbar = soup.find("div", "sidebar-content")
            # sbar_menu = soupbar.findall("li", {"class": "li-content text-body"})
            # sbars = soup.find_all(text=re.compile('sidebar'))
            divs = soup.find(id="sidebar-content")
            sidediv = soup.find(id="sidebar")
            # print('=====', file_path, '=====')
            # print('===== - 2', file_path, '=====', sidediv)
            target = soup.find(string="State Information")
            if target is not None:
                mycomment = Comment('former State Information')
                replacement = target.find_parent().replace_with(mycomment)
            print('=====', file_path, '=====',)

            prettyHTML = soup.prettify()
            f.close()
            of = open(file_path, mode='w', encoding='utf-8')
            of.write(prettyHTML)
            of.close()

