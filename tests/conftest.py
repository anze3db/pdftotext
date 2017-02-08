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
