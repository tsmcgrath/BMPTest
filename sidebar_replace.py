# python script to list the contents of sidebars on static html pages
from bs4 import BeautifulSoup
from bs4 import Comment
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
            divs = soup.find(id="sidebar-content")
            sidediv = soup.find(id="sidebar")
            print('=====', file_path, '=====', sidediv)

            # Replacing State Info header 2 - haven't got this working yet.
            # target = soup.find('h2', text="State Information")
            # mycomment =  Comment('Replacement comment for State Information Header 2')
            # replacement = target.replace_with(mycomment)

            # Replacing Impairment Issues
            target = soup.find("li", text="Impairment Issues")
            mycomment =  Comment('Replacement comment for Impairment Issues')
            replacement = target.replace_with(mycomment)

            # Replacing Conservation Priorities
            target = soup.find("li", text="Conservation Priorities")
            mycomment =  Comment('Replacement comment for Conservation Priorities')
            replacement = target.replace_with(mycomment)

            # Replacing Critical Habitats
            target = soup.find("li", text="Critical Habitats")
            mycomment =  Comment('Replacement comment for Critical Habitats')
            replacement = target.replace_with(mycomment)

            # Replacing Native Species
            target = soup.find("li", text="Native Species")
            mycomment =  Comment('Replacement comment for Native Species')
            replacement = target.replace_with(mycomment)

            # Replacing Exotic Species
            target = soup.find("li", text="Exotic Species")
            mycomment =  Comment('Replacement comment for Exotic Species')
            replacement = target.replace_with(mycomment)

            # Replacing Texas Conservation Action Plan
            target = soup.find("li", text="Texas Conservation Action Plan")
            mycomment =  Comment('Replacement comment for Texas Conservation Action Plan')
            replacement = target.replace_with(mycomment)

            # Replacing Imperiled Species
            target = soup.find("li", text="Imperiled Species")
            mycomment =  Comment('Replacement comment for Imperiled Species')
            replacement = target.replace_with(mycomment)
            sidediv = soup.find(id="sidebar")
            print('===== - 2', file_path, '=====', sidediv)
