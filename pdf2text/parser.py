"""PDF parser"""

import pdfminer.high_level
from tempfile import TemporaryFile


def parse(f, pages=""):
    """Parse the input file f and return plain text"""
    with TemporaryFile() as out:
        laparams = pdfminer.layout.LAParams()
        pdfminer.high_level.extract_text_to_fp(
            f, out, laparams=laparams, page_numbers=parse_pages(pages)
        )
        out.seek(0)
        lines = out.read()
        return lines


def parse_pages(pages):
    """Parse pages string into a list of pages"""
    if not len(pages):
        return None
    res = set()
    for p in pages.split(','):
        res = res.union(_parse_single_page(p))
    return list(res)


def _parse_single_page(page):
    """Parse a single page literal"""
    if "-" not in page:
        return [int(page) - 1]
    a, b = [int(x) - 1 for x in page.split('-')]
    return set(range(a, b + 1, 1))
