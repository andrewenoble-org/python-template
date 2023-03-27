import os
import sys

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
version = "0.0.6"
license = "MIT"

# insert path to source code
sys.path.insert(0, os.path.abspath(".."))
