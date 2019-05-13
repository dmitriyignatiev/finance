import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@localhost:3306/fin_test_1'
    SQLALCHEMY_TRACK_MODIFICATIONS = False