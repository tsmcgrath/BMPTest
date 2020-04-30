# what are the links to internal pdf's for each HTML file?
# python script to list the contents of sidebars on static html pages
import os
import csv
# The top argument for the directory walk
topdir = '/Users/Tim/Code/Github/BMPStaging'

# The extension to search for
exten = '.html'
rows = []
fields = ['File', 'URL']
rows.append(fields)

# Name of output csv file
intelfile = "html-pdf_intel.csv"

for dirpath, dirnames, files in os.walk(topdir):
    for name in files:
        if name.lower().endswith(exten):
            # print(os.path.join(dirpath, name))
            file_path = os.path.join(dirpath, name)
            with open(file_path) as openfile:
               for line in openfile:
                   if "../BMPpdfs/" in line:
                       row = [file_path, line.strip()]
                       rows.append(row)
            openfile.close()

 # writing to the csv file
    with open(intelfile, 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerows(rows)
        csvfile.close()
