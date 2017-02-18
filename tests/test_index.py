"""Test index page"""

import pytest


@pytest.mark.parametrize("element", (b'html', b'body', b'head', b'title'))
def test_basic_tags(element, index):
    """Test if the index page has the basic tags"""
    assert index.data.count("<{}>".format(element)) == 1
    assert index.data.count("</{}>".format(element)) == 1


def test_page_title(index):
    """Test the title of the index page"""
    assert b'<title>pdf to text</title>' in index.data
    assert b'<h1 class="text-muted">pdf to text</h1>' in index.data


def test_upload_form(index):
    """Test if the index page has the upload elements"""
    assert b'action="/upload" method="post" enctype="multipart/form-data"'\
        in index.data, "Upload form missing from index"
    assert (b'<input type="file" name="pdf" id="pdf"'
            b' accept="application/pdf"') in index.data, \
        "File input missing from index page"
    assert (b'<button type="submit" class="btn btn-primary"'
            b'>Submit</button>') in index.data, \
        "Submit button missing from index page"
    assert (b'<input type="text" name="pages"' in index.data), \
        "Pages input missing from index page"


@pytest.mark.parametrize('dep', ('bootstrap.min.css',
                                 'jquery-3.1.1.slim.min.js',
                                 'tether.min.js',
                                 'bootstrap.min.js'))
def test_bootstrap(index, dep):
    """Test if all bootstrap dependencies get loaded"""
    assert dep in index.data


def test_hide_parsed_text(index):
    """Test if textarea with parsed text is hidden by default"""
    assert '<textarea' not in index.data, index.data
