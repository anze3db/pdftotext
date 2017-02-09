"""Commonly used fixtures"""

import pytest
import pdf2text


@pytest.fixture
def app():
    """Return the pdf2text app context"""
    pdf2text.app.config['TESTING'] = True
    return pdf2text.app.test_client()


@pytest.fixture
def index(app):
    """Return the app's index page object"""
    return app.get('/')


@pytest.fixture
def uploadfn(app):
    """Return the app's index page object"""
    def _upload(data=None, follow_redirects=False):
        return app.post('/upload',
                        data=data,
                        follow_redirects=follow_redirects)


    return _upload
