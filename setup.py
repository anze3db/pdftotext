from setuptools import setup

setup(
    name='pdf2text',
    packages=['pdf2text'],
    include_package_data=True,
    install_requires=[
        'flask',
        'pdfminer.six',
    ],
    setup_requires=[
        'pytest-runner',
    ],
    tests_require=[
        'pytest',
        'pytest-cov',
    ],
)
