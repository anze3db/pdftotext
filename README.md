# pdf to text

[![CircleCI](https://circleci.com/gh/Smotko/pdftotext.svg?style=svg)](https://circleci.com/gh/Smotko/pdftotext) [![codecov](https://codecov.io/gh/Smotko/pdftotext/branch/master/graph/badge.svg)](https://codecov.io/gh/Smotko/pdftotext)

Simple frontend for pdfminer.

## Install local environemnt:

```bash
python setup.py develop
export FLASK_APP=pdf2text
export FLASK_DEBUG=true
flask run
```

## Run tests:

```bash
run setup.py test
ptw # run continously and reload on file change
```
