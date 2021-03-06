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
            f = open(file_path, mode='r', encoding = 'utf-8')
            soup = BeautifulSoup(f, 'html.parser')
            # soupbar = soup.find("div", "sidebar-content")
            # sbar_menu = soupbar.findall("li", {"class": "li-content text-body"})
            # sbars = soup.find_all(text=re.compile('sidebar'))
            divs = soup.find(id="sidebar-content")
            sidediv = soup.find(id="sidebar")
            print('=====', file_path, '=====')

            # Replacing the State Info header
            target = soup.find(string="State Information")
            if target is not None:
                mycomment = Comment('former State Information')
                replacement = target.find_parent().replace_with(mycomment)

            # Replacing Impairment Issues
            target = soup.find("li", text="Impairment Issues")
            if target is not None:
                mycomment =  Comment('Replacement comment for Impairment Issues')
                replacement = target.replace_with(mycomment)

            # Replacing Conservation Priorities
            target = soup.find("li", text="Conservation Priorities")
            if target is not None:
                mycomment = Comment('Replacement comment for Conservation Priorities')
                replacement = target.replace_with(mycomment)

            # Replacing Critical Habitats
            target = soup.find("li", text="Critical Habitats")
            if target is not None:
                mycomment = Comment('Replacement comment for Critical Habitats')
                replacement = target.replace_with(mycomment)

            # Replacing Native Species
            target = soup.find("li", text="Native Species")
            if target is not None:
                mycomment = Comment('Replacement comment for Native Species')
                replacement = target.replace_with(mycomment)

            # Replacing Exotic Species
            target = soup.find("li", text="Exotic Species")
            if target is not None:
                mycomment = Comment('Replacement comment for Exotic Species')
                replacement = target.replace_with(mycomment)

            # Replacing Texas Conservation Action Plan
            target = soup.find("li", text="Texas Conservation Action Plan")
            if target is not None:
                mycomment = Comment('Replacement comment for Texas Conservation Action Plan')
                replacement = target.replace_with(mycomment)

            # Replacing Imperiled Species
            target = soup.find("li", text="Imperiled Species")
            if target is not None:
                mycomment = Comment('Replacement comment for Imperiled Species')
                replacement = target.replace_with(mycomment)

            sidediv = soup.find(id="sidebar")
            # print('===== - 2', file_path, '=====', sidediv)
            prettyHTML = soup.prettify()
            of = open(file_path, mode='w', encoding='utf-8')
            of.write(prettyHTML)
            of.close()
            f.close()
