"""Test upload endpoint"""

import pytest
from StringIO import StringIO


def test_upload_redirect(uploadfn):
    """Test if /upload redirects to /"""
    upload = uploadfn(None)
    assert upload.status_code == 302, upload.status_code
    assert upload.location == 'http://localhost/', upload.location


def test_no_toast_on_index(index):
    """Test if index page shows no toast messages by default"""
    assert "No file uploaded!" not in index.data, index.data


def test_no_toast_on_file(uploadfn):
    """Test if toast messages appear on errors only"""
    upload = uploadfn({'pdf': (StringIO('Contents'), 'p.pdf')}, True)
    assert "No file uploaded!" not in upload.data


@pytest.mark.parametrize('uploadFile', (
    None,
    {'pdf': ''},
    {'pdf': None},
    {'pdf': (StringIO(''), '')}))
def test_toast_on_empty(uploadfn, uploadFile):
    """Test if a warning toast is displayed when no file is selected"""
    upload = uploadfn(uploadFile, True)
    assert upload.status_code == 200, upload.status_code
    assert "No file uploaded!" in upload.data, upload.data


def test_toast_on_invalid(uploadfn):
    """Test if toast notifies the user when the file is not a pdf"""
    upload = uploadfn({'pdf': (StringIO('hello'), 'invalid.pdf')}, True)
    assert "Uploaded file is not a valid PDF" in upload.data, upload.data


def test_show_text_on_upload(uploadfn):
    """Test if pdf text is correctly shown"""
    with open('tests/pdfs/hello.pdf') as f:
        upload = uploadfn({'pdf': f}, True)
    assert "hello world" in upload.data, upload.data


def test_page_numbers(uploadfn):
    """Test if pdf text is correctly shown"""
    with open('tests/pdfs/multipage.pdf') as f:
        upload = uploadfn({'pdf': f, 'pages': "2"}, True)
    assert "Second" in upload.data, "Missing second page"
    assert "First" not in upload.data, "First page should not be present"


def test_toast_on_invalid_page_numbers(uploadfn):
    """Test if toast notifies the user the page numbers were not used"""
    with open('tests/pdfs/hello.pdf') as f:
        upload = uploadfn({'pdf': f, 'pages': 'a'}, True)
    assert "Was not able to parse page numbers" in upload.data, upload.data
