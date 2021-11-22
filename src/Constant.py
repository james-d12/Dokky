from jinja2 import Environment, FileSystemLoader

JINJA2_ENV = Environment(loader=FileSystemLoader('src/Templates'))

INCLUDE_DIRECTORY_KEY = "includeDirectory"
OUTPUT_DIRECTORY_KEY = "outputDirectory"
COMMENT_DENOTION_KEY = "commentDenotion"
FILTER_LIST_KEY = "filterList"
LANGUAGE_KEY = "language"
REPOSITORY_KEY = "repository"