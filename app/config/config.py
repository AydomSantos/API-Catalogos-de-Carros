import os
from datetime import timedelta

basedir = os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET') or 'super-secret-key'
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=1)
