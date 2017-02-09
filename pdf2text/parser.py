"""PDF parser"""

from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfpage import PDFTextExtractionNotAllowed
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.converter import TextConverter
from StringIO import StringIO


def parse(f):
    parser = PDFParser(f)
    document = PDFDocument(parser)
    rsrcmgr = PDFResourceManager()
    out = StringIO()
    device = TextConverter(rsrcmgr, out)
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    for page in PDFPage.create_pages(document):
        interpreter.process_page(page)
    return out.getvalue()[1:]
