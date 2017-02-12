# -*- coding: utf8 -*-

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


def test_parse_unicode():
    """Test if unicode is parsed correctly"""
    with open('tests/pdfs/unicode.pdf', 'rb') as f:
        text = parser.parse(f)
    assert "unicode čćç" in text, text


def test_parse_newlines():
    """Test if newlines are parsed correctly"""
    with open('tests/pdfs/newline.pdf', 'rb') as f:
        text = parser.parse(f)
    assert "\n" in text, text
