AUTHOR = 'qu1ck'
SITENAME = 'OpenScopeProject'
SITEURL = ""

PATH = "content"

TIMEZONE = 'US/Pacific'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
# LINKS = (
#     ("Pelican", "https://getpelican.com/"),
#     ("Python.org", "https://www.python.org/"),
#     ("Jinja2", "https://palletsprojects.com/p/jinja/"),
#     ("You can modify those links in your config file", "#"),
# )

# Social widget
# SOCIAL = (
#     ("Github", "https://github.com/openscopeproject"),
# )

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

STATIC_PATHS = [
    ".well-known",
    "img",
    "static",
]

# THEME config
THEME = "theme"
PLUGIN_PATHS = ['pelican-plugins', ]
PLUGINS = ['i18n_subsites', ]
JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}

BOOTSTRAP_THEME = "flatly"
# BOOTSTRAP_FLUID = True
SIDEBAR_ON_LEFT = True
DISPLAY_PAGES_ON_MENU = True
GITHUB_USER = "openscopeproject"
GITHUB_REPO_COUNT = 10
GITHUB_SKIP_FORK = True
GITHUB_SHOW_USER_LINK = True
CUSTOM_CSS = "static/custom.css"
