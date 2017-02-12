"""PDF parser"""

import pdfminer.high_level
from tempfile import TemporaryFile


def parse(f):
    """Parse the input file f and return plain text"""
    with TemporaryFile() as out:
        laparams = pdfminer.layout.LAParams()
        pdfminer.high_level.extract_text_to_fp(f, out, laparams=laparams)
        out.seek(0)
        lines = out.read()
        return lines
