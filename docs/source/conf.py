# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'bioactivity analysis'
copyright = '2024, Anne Deslattes Mays, PhD'
author = 'Anne Deslattes Mays, PhD'
release = '1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

# -- Project information -----------------------------------------------------
project = 'Bioactivity Analysis'
copyright = '2024'
author = 'Anne Deslattes Mays, PhD'
release = '1.0'

# -- General configuration ---------------------------------------------------


extensions = [
    "myst_parser",
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_rtd_theme",
    "nbsphinx",
]

myst_enable_extensions = [
    "dollarmath",
    "colon_fence",
]

# Paths
import os
import sys
sys.path.insert(0, os.path.abspath('../..'))

# Exclude build and checkpoint files
exclude_patterns = ["build", "**.ipynb", "**.ipynb_checkpoints"]

# HTML theme
html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]


