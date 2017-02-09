"""Main app module"""

from flask import Flask
from flask import flash
from flask import request
from flask import redirect
from flask import render_template
from flask import url_for
from pdf2text.parser import parse
from pdfminer.pdfparser import PDFSyntaxError


app = Flask(__name__)
app.secret_key = 'super secret key'

@app.route('/')
def index():
    """Serve the index page"""
    return render_template('index.html', parsed_text=request.args.get('messages', None))


@app.route('/upload', methods=["POST"])
def upload():
    """Serve the upload page"""
    pdf = request.files.get('pdf', None)
    if pdf is None or not pdf.filename:
        flash('No file uploaded! Please pick a file to upload.')
        return redirect(url_for('.index'))
    try:
        parsed = parse(pdf)
    except PDFSyntaxError:
        flash("Uploaded file is not a valid PDF")
        return redirect(url_for('.index'))
    return redirect(url_for('.index', messages=parsed))
