# Configuration file for the Sphinx documentation builder.

import os
import sys
import django

sys.path.insert(0, os.path.abspath('..'))
os.environ['DJANGO_SETTINGS_MODULE'] = 'oc_lettings_site.settings'
django.setup()

# -- Project information -----------------------------------------------------

project = 'Holiday Homes'
copyright = '2024, Anna'
author = 'Anna'
release = '0.1'

# -- General configuration ---------------------------------------------------

extensions = [
    'sphinx_rtd_theme',
    'sphinx.ext.autodoc',
    ]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_logo = "logo.png"
