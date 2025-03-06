import os
from datetime import timedelta

basedir = os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

class Config:
    MONGO_URI = 'mongodb+srv://root:root@catalogcarros.8eqf6.mongodb.net/vehicles_db'
    JWT_SECRET_KEY = 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTc0MTI3NjM3MiwianRpIjoiNGUyNjc3NmYtYWVlYi00Y2QyLTliMTgtMDVhZTE1MGQ1MzM2IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6IjY3Yzc5YjI4ZTM0OGJiY2RiMTk5Zjg2ZiIsIm5iZiI6MTc0MTI3NjM3MiwiZXhwIjoxNzQxMzYyNzcyfQ.B0rjH6tlLHUou6Bq9Da5SQjUzu1mSHixXtXOzG9dQ80'
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=1)
