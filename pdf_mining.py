# Python code to extract intel from the BMP pdf's to analyze how we're going to classify and
# handle converting the links from internal pdf's to external links that point to the
# source of the information.
import os
import csv
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument


def extract_information(pdf_path):
    with open(pdf_path, 'rb') as f:
        try:
            parser = PDFParser(f)
            document = PDFDocument(parser)
            outlines = document.get_outlines()
            for (level, title, dest, a, se) in outlines:
                 info = [pdf_path, level, title, ""]
        except:
            info = [pdf_path, "", "",  "An exception occured"]
        return info


if __name__ == '__main__':
    # The top argument for the directory walk
    topdir = '/Users/Tim/Code/Github/BMPTest'

    # The extension to search for
    exten = '.pdf'
    rows = []
    fields = ['File', 'Level', 'Title', 'Comment']
    rows.append(fields)


    for dirpath, dirnames, files in os.walk(topdir):
        for name in files:
            if name.lower().endswith(exten):
                # print(os.path.join(dirpath, name))
                file_path = os.path.join(dirpath, name)
                row = extract_information(file_path)
                rows.append(row)
    # Name of output csv file
    intelfile = "pdf_tocs.csv"

    #writing to the csv file
    with open(intelfile, 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerows(rows)
        csvfile.close()
