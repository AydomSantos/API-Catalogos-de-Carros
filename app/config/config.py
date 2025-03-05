import os
from datetime import timedelta

basedir = os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

class Config:
    MONGO_URI = 'mongodb+srv://root:root@catalogcarros.8eqf6.mongodb.net/vehicles_db'
    JWT_SECRET_KEY = 'your-secret-key'
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=1)
