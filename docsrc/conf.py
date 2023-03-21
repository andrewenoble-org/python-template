import os
from sys import path

# doc theme
html_theme = "sphinx_rtd_theme"

# doc extensions
extensions = [
    "numpydoc",
    "sphinx.ext.viewcode",
    "sphinx.ext.mathjax",
]

# doc parameters
numfig = True

# project details for docs
project = "python_template"
version = "0.0.0"
license = "MIT"

# insert path to source code
path.insert(0, os.path.abspath("/home/project/python_template"))
