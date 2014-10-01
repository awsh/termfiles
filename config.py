import os


URL = 'http://localhost:8000'
TEMPLATE_PATH = os.path.join(os.path.dirname(__file__), "templates")
STATIC_PATH = os.path.join(os.path.dirname(__file__), "static")
UPLOAD_DIR = os.path.join(STATIC_PATH, 'uploads')
DEBUG = True
MAX_UPLOAD_SIZE = 100000000000 #in bytes

