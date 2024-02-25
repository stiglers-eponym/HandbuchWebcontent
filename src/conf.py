project = 'Handbuch Webcontent'
copyright = '2024, Valentin Bruch, CC BY-SA 4.0'
author = 'Valentin Bruch'
release = '0.1'
extensions = []
language = 'de'
html_theme = 'furo'
master_doc = 'index'
html_show_sourcelink = False
html_title = "Handbuch Webcontent"

latex_engine = 'lualatex'
latex_elements = {
    'pointsize':'12pt',
    'papersize':'a4paper',
    'releasename':'Version',
    'fontpkg': r'''
\setmainfont{DejaVu Sans}
\setsansfont{DejaVu Sans}
\setmonofont{DejaVu Sans Mono}
''',
}
latex_show_urls = 'footnote'
