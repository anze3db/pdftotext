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


@pytest.mark.parametrize("strings,count,expected", (
    ("", 7, "First,Second,Third,Fourth,Fifth,Sixth,Seventh"),
    ("1", 1, "First"),
    ("1-5", 5, "First,Second,Third,Fourth,Fifth"),
    ("1-3, 3, 6", 4, "First,Second,Third,Sixth")
))
def test_multipage_filtering(strings, count, expected):
    """Test page filtering"""
    with open('tests/pdfs/multipage.pdf', 'rb') as f:
        text = parser.parse(f, strings)
    actual = len(text.split())
    expected = expected.split(',')
    assert actual == count, "Parsed pages {}, but should be {}".format(
        actual, expected)
    for i, t in enumerate(text.split()):
        print(expected[i], t)
        assert expected[i] in t


@pytest.mark.parametrize("strings,expected", (
    ("", None),
    ("1", [0]),
    ("1,2,3", [0, 1, 2]),
    ("1, 3 , 3 , 7 ", [0, 2, 6]),
    ("1-5", [0, 1, 2, 3, 4]),
    ("4-6, 1,2,5-7", [0, 1, 3, 4, 5, 6])
))
def test_parse_pages(strings, expected):
    """Test parse pages"""
    res = parser.parse_pages(strings)
    assert res == expected, \
        "Result '{}' does not match expected '{}' for {}".format(
            res, expected, strings)


@pytest.mark.parametrize("strings", (
    "a", "a,b,c", "1-b", "c-6, 1,d,5-e"
))
def test_parse_pages_with_error(strings):
    """Test if parse_pages throws a ValueError on invalid input"""
    with pytest.raises(ValueError):
        parser.parse_pages(strings)
