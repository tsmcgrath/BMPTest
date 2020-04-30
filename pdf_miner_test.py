from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument

# Open a PDF document.
fp = open('./test.pdf', 'rb')
parser = PDFParser(fp)
document = PDFDocument(parser)
if not document.is_extractable:
    raise PDFTextExtractionNotAllowed

# Get the outlines of the document.
outlines = document.get_outlines()
for (level,title,dest,a,se) in outlines:
    print (level, title)
