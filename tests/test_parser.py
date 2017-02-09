"""Test Parser"""

import pytest
from StringIO import StringIO
from pdf2text import parser

from pdfminer.pdfparser import PDFSyntaxError

def test_not_parsable():
    """Test if parser raises exception on invalid file"""
    with pytest.raises(PDFSyntaxError):
        parser.parse(StringIO('Contents'))


def test_parser():
    """Test if parser parses a simple pdf"""
    with open('tests/pdfs/hello.pdf', 'rb') as f:
        text = parser.parse(f)
    assert text.strip() == 'hello world', text.strip()
