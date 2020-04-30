# extract_doc_info.py
import os
from PyPDF2 import PdfFileReader


def extract_information(pdf_path):
    with open(pdf_path, 'rb') as f:
        pdf = PdfFileReader(f)
        information = pdf.getDocumentInfo()
        number_of_pages = pdf.getNumPages()

    txt = f"""
    Information about {pdf_path}:

    Author: {information.author}
    Creator: {information.creator}
    Producer: {information.producer}
    Subject: {information.subject}
    Title: {information.title}
    Number of pages: {number_of_pages}
    """

    print(txt)
    return information


if __name__ == '__main__':
    # The top argument for the directory walk
    topdir = '/Users/Tim/Code/Github/BMPStaging'

    # The extension to search for
    exten = '.pdf'

    for dirpath, dirnames, files in os.walk(topdir):
        for name in files:
            if name.lower().endswith(exten):
                # print(os.path.join(dirpath, name))
                file_path = os.path.join(dirpath, name)
                extract_information("/Users/Tim/Code/Github/BMPStaging/BMPpdfs/01995_WashingtonFishCulverts.pdf")
