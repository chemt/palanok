# -*- coding: utf-8 -*-
# Django settings for cms project.
import os
PROJECT_DIR = os.path.dirname(__file__)
PROJECT_NAME = 'palanok'

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

CACHE_BACKEND = 'locmem:///'

MANAGERS = ADMINS



DATABASE_ENGINE = 'sqlite3'     #postgresql_psycopg2'       # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
DATABASE_NAME = 'cms.db'           # Or path to database file if using sqlite3.
DATABASE_USER = ''           # Not used with sqlite3.
DATABASE_PASSWORD = ''       # Not used with sqlite3.
DATABASE_HOST = ''     # Set to empty string for localhost. Not used with sqlite3.
DATABASE_PORT = ''              # Set to empty string for default. Not used with sqlite3.

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be avilable on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Chicago'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# Absolute path to the directory that holds media.
MEDIA_ROOT = os.path.join(PROJECT_DIR, 'media/')
#ADMIN_MEDIA_ROOT = os.path.join(PROJECT_DIR, '../admin_media/')
MEDIA_URL = '/media/'

ADMIN_MEDIA_PREFIX = '/media/admin/'

FIXTURE_DIRS = [os.path.join(PROJECT_DIR, 'fixtures')]

# Make this unique, and don't share it with anybody.
SECRET_KEY = '*xq7m@)*sdf213f2awoj!spa0(jibsrz9%c0d=e(g)v*!17y(vx0ue_3'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
    'django.template.loaders.eggs.load_template_source',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.core.context_processors.auth",
    "django.core.context_processors.i18n",
    "django.core.context_processors.debug",
    "django.core.context_processors.request",
    "django.core.context_processors.media",
    "cms.context_processors.media",
)

INTERNAL_IPS = ('127.0.0.1',)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.doc.XViewMiddleware',

    #'django.contrib.csrf.middleware.CsrfMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.multilingual.MultilingualURLMiddleware',
    #'cms.middleware.toolbar.ToolbarMiddleware',
    #'debug_toolbar.middleware.DebugToolbarMiddleware',
    
)

ROOT_URLCONF = PROJECT_NAME + '.urls'


TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(PROJECT_DIR, 'templates'),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.sites',
    #'tagging',
    
    'cms',
    'publisher',
    
    'cms.plugins.text',
    'cms.plugins.picture',
    'cms.plugins.file',
    'cms.plugins.flash',
    'cms.plugins.link',
    'cms.plugins.snippet',
    'cms.plugins.googlemap',
    'cms.plugins.teaser',
    #'cms.plugins.video',

    'mptt',
    'reversion',
    'django_extensions',
    #'debug_toolbar',
    'south',
	'tagging',
	
    'photologue',
    'cmsplugin_photologue',

    # sample application
    #'test_utils',
    #'store',
)

gettext = lambda s: s

LANGUAGE_CODE = "ru-RU"

LANGUAGES = (
    ('en', gettext('English')),
    ('ru', gettext('Russian')),
    ('uk', gettext('Ukrainian')),
    ('hu', gettext('Hungarian')),
)

CMS_LANGUAGE_FALLBACK = True
CMS_LANGUAGE_CONF = {
    'de':['en'],
    'ru':['uk', 'en'],
    'uk':['ru', 'en'],
    'hu':['en'],
}

APPEND_SLASH = True

CMS_TEMPLATES = (
    ('2col-left.html',  gettext(u'с левой колонкой')),
    ('2col-right.html', gettext(u'с правой колонкой')),
    ('main.htm', gettext(u'Главная страница')),
)

CMS_APPLICATIONS_URLS = (
    ('cmsplugin_photologue.urls', 'Photologue app'),
)

CMS_PLACEHOLDER_CONF = {                        
    'body': {
        "extra_context": {"width":450},
        "name":gettext("body"),
    },

    'top': {
        "extra_context": {"width":810},
        "name":gettext("top"),
    },
    
    'side-column': {
        "extra_context": {"width":250},
        "name":gettext("column")
    },
    
    'info1':{"extra_context": {"width":200},
        "name":gettext("info1")
    },
    'info2':{"extra_context": {"width":200},
        "name":gettext("info2")
    },
    'info3':{"extra_context": {"width":200},
        "name":gettext("info3")
    },
    'info4':{"extra_context": {"width":200},
        "name":gettext("info4")
    },
}


CMS_NAVIGATION_EXTENDERS = (
    ('cmsplugin_photologue.menu.get_nodes', gettext('Photologue navigation')),
)

CMSPLUGIN_PHOTOLOGUE_CSS_CHOICES = (('0', ''),('1', 'small-gallery'),('2', 'left'),('3', 'right'),('4', 'center'),)

CMS_SOFTROOT = True
CMS_MODERATOR = False
CMS_PERMISSION = False
CMS_REDIRECTS = False
CMS_SEO_FIELDS = True
CMS_FLAT_URLS = False
CMS_MENU_TITLE_OVERWRITE = True
CMS_HIDE_UNTRANSLATED = True
CMS_URL_OVERWRITE = False
CMS_TEMPLATE_INHERITANCE = True


try:
    from local_settings import *
except ImportError:
    pass

