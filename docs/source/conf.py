import os
import re

# -- Project Information -----------------------------------------------------
project = 'Asha'
copyright = '2026-, آزاداندیش داده‌ساز'
author = 'Dataist'
release = '0.1.7'

# -- General Configuration ---------------------------------------------------
extensions = [
    'myst_parser',
    'sphinx_design',
    'sphinx_sitemap',
    'sphinx_rtd_theme',
    'sphinx_multiversion',
    'sphinx.ext.autosectionlabel',
]

language = 'fa'
templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', 'download.tmpl.rst']
smartquotes = True

# -- HTML Output Options & Theme Options -------------------------------------
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_css_files = ['custom.css']
html_favicon = '_static/favicon.png'

html_theme_options = {
    'navigation_depth': 4,
    'collapse_navigation': False,
    'style_external_links': True,
    'vcs_pageview_mode': 'edit',
}

# -- Site & Template Context -------------------------------------------------
html_baseurl = 'https://asha.dataist.ir/'

html_context = {
    'current_version': 'stable',
    'current_release': release,
    'versions': [('stable', '/')],
    'downloads': [('HTML', '#')],
}

html_sidebars = {
    '**': ['searchbox.html', 'navigation.html', 'versions.html']
}

# -- LaTeX Configuration for Persian ------------------------------------------
latex_engine = 'xelatex'

latex_elements = {
    'preamble': r'''
        \usepackage{bidi}
        \setmainfont{DejaVu Sans}
        \setsansfont{DejaVu Sans}
        \setmonofont{DejaVu Sans Mono}
    ''',
}


# -- Dynamic Stats Engine -----------------------------------------------------
def update_download_page_stats():
    pass


# -- Search & Markdown Optimization -------------------------------------------
myst_enable_extensions = [
    "colon_fence",
    "deflist",
]
