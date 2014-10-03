import os


URL = 'http://localhost:8000'
TEMPLATE_PATH = os.path.join(os.path.dirname(__file__), "templates")
STATIC_PATH = os.path.join(os.path.dirname(__file__), "static")
UPLOAD_DIR = os.path.join(STATIC_PATH, 'uploads')
DEBUG = True
MAX_UPLOAD_SIZE = 100000000000 #in bytes
EXPIRE_TIME = 24 # in hours - expire and remove files after x hours
FILE_CLEANUP_SCHEDULE = 2000 #86400000# - 1 day #in milliseconds - run cleanup every x milliseconds
