from os import environ

class Config:
    ##################### Application config ##################

    ENV = environ.get("THECHLAND_AUTHZ_ENV", "production")
    DEBUG = bool(int(environ.get("THECHLAND_AUTHZ_DEBUG", "0")))
    TESTING = bool(int(environ.get("THECHLAND_AUTHZ_TESTING", "0")))
    SECRET_KEY = environ.get("THECHLAND_AUTHZ_SECRET_KEY", "HARD-HARD-HARD-SECRET-KEY")
    
    ################# Database config ##########################

    SQLALCHEMY_DATABASE_URI = environ.get("THECHLAND_AUTHZ_DATABASE_URI", None)
    SQLALCHEMY_ECHO = DEBUG
    SQLALCHEMY_RECORD_QUERIES = DEBUG
    SQLALCHEMY_TRACK_MODIFICATIONS = DEBUG
    TIMEZONE = environ.get("THECHLAND_AUTHZ_TIMEZONE", "Asia,Tehran")
    
    ###################### user config ##################
    
    USER_DEFAULT_ROLE = environ.get("TECHLAND_AUTHZ_USER_DEFAULT_ROLE", "member")
    USER_DEFAULT_EXPIRY_TIME = int(environ.get("TECHLAND_AUTHZ_USER_DEFAULT_EXPIRY_TIME", "365"))
    USER_DEFAULT_STATUS = int(environ.get("TECHLAND_AUTHZ_USER_DEFAULT_STATUS", "3"))    
