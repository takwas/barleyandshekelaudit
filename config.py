import os


BASE_URI = os.path.abspath(os.path.curdir)#os.path.dirname(__file__)

# Get absolute path to user's home directory                
HOME_DIR = os.path.expanduser('~/')                 # '/' is added to ensure the path has a trailing slash

# Let's store the name of the application
# package here.
APP_NAME = 'audit'



"""
Configuration classes.

Class `Config` class is the base/super class.

`DevConfig`, `TestingConfig` and `ProductionConfig` all extend the base
class: `Config`
"""
class Config(object):
    """
    Base configuration class. Has all the common configuration
    properties.
    """
    DEBUG = False
    TESTING = False
    WTF_CSRF_ENABLED = True
    SECRET_KEY = os.environ.get('CSRF_SESSION_SECRET_KEY') or \
        '023g8fnotsecureenoughavdRVA0RB'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    THREADS_PER_PAGE = 2    
    APP_NAME = APP_NAME


    # DB_URI = os.path.join(BASE_URI, '.barleyandshekelaudit.sqlite')
    DB_URI = ""
    # SQLALCHEMY_DATABASE_URI = 'postgresql:///' + DB_URI
    SQLALCHEMY_DATABASE_URI = 'postgresql://barley:password@localhost:5432/barleyandshekelaudit'
    #APP_STATIC_DATA_URI = os.path.join(BASE_URI, APP_NAME, 'data')
