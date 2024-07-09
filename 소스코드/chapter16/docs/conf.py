# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'My Project'
copyright = '2024, Your Name'
author = 'Your Name'

# -- General configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
]

templates_path = ['_templates']

exclude_patterns = []

# -- Options for HTML output

html_theme = 'alabaster'
html_static_path = ['_static']
