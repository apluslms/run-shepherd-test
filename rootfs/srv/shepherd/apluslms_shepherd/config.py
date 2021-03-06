import os
import string
from builtins import object, frozenset
from os.path import dirname, join

class Config(object):
    DEBUG = False
    TESTING = False
    BASE_DIR = "/srv/shepherd/"
    SQLALCHEMY_DATABASE_URI = "postgresql:///apluslms_shepherd"
    LOGIN_REDIRECT_URL = "/auth/success/"
    LOGIN_DISABLED = False
    BASE_CHARACTERS = string.ascii_letters + string.digits
    SAFE_CHARACTERS = frozenset(BASE_CHARACTERS + '-')
    KEY_LENGTH_RANGE = (6, 128)
    NONCE_LENGTH = (6, 128)
    SECRET_LENGTH_RANGE = (6, 128)
    KEY_LENGTH = 16
    SECRET_LENGTH = 64
    USER_NAME_LENGTH = 120
    FIRST_NAME_LENGTH = 50
    LAST_NAME_LENGTH = 50
    EMAIL_LENGTH = 50
    CREATE_UNKNOWN_USER = True
    SECRET_KEY = 'my super secret key'.encode('utf8')
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    LTI_CONFIG = {
        'secret': {
            "Bleks2FiObiMpd5C": "uf7OtOjcCclxGZBzzRoll87vledSK8cK3koL6BRCSwelICYIc8eyG56qxDJKtV6l"
        }
    }
    USE_SSH_FOR_GIT = True
    BROKER_URL = "amqp://"
    CELERY_NAME = "test"
    CELERY_IMPORTS = ("apluslms_shepherd.celery_tasks.build",
                      "apluslms_shepherd.celery_tasks.repos"
                      )
    COURSE_REPO_BASEPATH = join(BASE_DIR, "shepherd_test_clone/")

class DevelopmentConfig(Config):
    DEBUG = True
    BUILD_WEBHOOK_TOKEN = "Secret"
    BUILD_WEBHOOK_URL = "http://127.0.0.1:5000/webhooks/state/"
    COURSE_DEPLOYMENT_PATH = join(Config.BASE_DIR, "shepherd_deploy/")
    REPO_KEYS_PATH = join(Config.BASE_DIR, "shepherd_repo_keys/")

class TestingConfig(Config):
    TESTING = True
