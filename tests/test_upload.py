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
