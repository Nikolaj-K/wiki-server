import os.path as path


ROOT = path.join("/Users", "amoogle", "Documents", "Git", "wiki-server")
FILEPATH_HTML_HOME = path.join(ROOT, 'README.md')

HTML = path.join(ROOT, 'html')
FILEPATH_HTML_SCHEME = path.join(HTML, 'scheme.html')
FILEPATH_HTML_DEBUG = path.join(HTML, 'page_debug.html')
FILEPATH_SEARCH_RESULTS = path.join(HTML, "tmp_search_results.txt")

FILE_EDITOR_COMMAND = "atom"

HOST = "127.0.0.1" # Note: currently hardcoded in the html_scheme file
PORT = "8080" # Note: currently hardcoded in the html_scheme file

SEARCH_FILEPATH_LEGAL_EXTENSIONS = [
    'txt',
    'md',
    'rtf',
    'py',
    'csv',
    'json',
]
WORD_FINDER_IGNORE_EXTENSIONS = [
    ".html",
    ".gif",
    ".png",
    ".jpg",
    ".pyc",
    ".git",
    ".idx",
    ".pack",
    ".sample",
    ".DS_Store",
]

COLORS = dict(
    light_blue="#eef2ff",
    light_blue_darker="#d6daf0",
    dark_blue="#1e1c68",
    grey_blue="#3f3f66",
    green="#177a49",
    red="#dc2629",
    gray="#D1D5EE",
)
