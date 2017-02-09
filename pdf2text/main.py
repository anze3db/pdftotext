"""Main app module"""

from flask import Flask
from flask import flash
from flask import request
from flask import redirect
from flask import render_template
from flask import url_for


app = Flask(__name__)
app.secret_key = 'super secret key'

@app.route('/')
def index():
    """Serve the index page"""
    return render_template('index.html')


@app.route('/upload', methods=["POST"])
def upload():
    """Serve the upload page"""
    pdf = request.files.get('pdf', None)
    if pdf is None:
        flash('No file uploaded! Please pick a file to upload.')
        return redirect(url_for('.index'))
    return redirect(url_for('.index'))
