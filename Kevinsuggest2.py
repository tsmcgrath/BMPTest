import os
import json
from bs4 import BeautifulSoup
html = None
with open('links_to_change.json') as f:
    links_to_change = json.load(f)
with os.scandir('.') as it:
    for entry in it:
        if entry.name.endswith('html') and entry.is_file():
            print('Prcoessing', entry.path)
            with open(entry.path) as f:
                html = f.read()
                soup = BeautifulSoup(html)
                changed = False
                for a in soup.find_all('a'):
                    if a['href'] in links_to_change:
                        print('  Changing link "{:s}" to "{:s}"'.format(a['href'], links_to_change[a['href']]))
                        a['href'] = links_to_change[a['href']]
                        changed = True
                if changed:
                    print(str(soup))