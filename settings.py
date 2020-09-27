import os

SQLALCHEMY_DATABASE_URI = "sqlite:///db.sqlite3"  # os.environ.get('sqlite:///db.sqlite3')
SQLALCHEMY_TRACK_MODIFICATIONS = False

ADMIN_USERNAME = os.environ.get('password')
ADMIN_PASSWORD = os.environ.get('admin')
