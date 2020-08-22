import os

class Config:
    # General Config
  SECRET_KEY = os.environ.get('SECRET_KEY')
  FLASK_APP = os.environ.get('FLASK_APP')
  FLASK_DEBUG = os.environ.get('FLASK_DEBUG')


  # Database
  SQLALCHEMY_DATABASE_URI = "sqlite:///" +  os.path.dirname(os.path.realpath(__file__)) + "/db/lame.db"
  SQLALCHEMY_TRACK_MODIFICATIONS = True
  
