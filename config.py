import os

class Config:
    '''
    General configuration parent class
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://wayne:123456@localhost/pitches'
    SECRET_KEY = "123456789"
    UPLOADED_PHOTOS_DEST = 'app/static/photos'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    SSL_DISABLE = False
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLCLCHEMY_RECORD_QUERIES = True
    CSRF_ENABLED = True
    MAIL_SERVER = os.environ.get('MAIL_SERVER','smtp.gmail.com')
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME','wkudoi@gmail.com')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD','@Sop123@')
    MAIL_SENDER = os.environ.get('MAIL_SENDER', 'Project Admin<wkudoi@gmail.com>')
    PROJECT_ADMIN = os.environ.get('PROJECT_ADMIN', 'PROJECT_ADMIN')
    MAIL_PORT = int(os.environ.get('MAIL_PORT', '465'))
    MAIL_USE_TLS = int(os.environ.get('MAIL_USE_TLS', False))
    MAIL_USE_SSL = int(os.environ.get('MAIL_USE_SSL',  True))
    MAIL_SUBJECT_PREFIX = '[PROJECT]'

    # simple mde  configurations
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True

class ProdConfig(Config):
    '''
    Production configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    # SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://wayne:123456@localhost/pitches'

class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://wayne:123456@localhost/pitches'

    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}
