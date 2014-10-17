import os


# URL is the domain name of the site
URL = 'http://localhost:8000'

# TEMPLATE_PATH is the path to your template folder
# By default it is set to ./templates
TEMPLATE_PATH = os.path.join(os.path.dirname(__file__), "templates")

# STATIC_PATH is the path to your static folder
# By default is set to ./static
STATIC_PATH = os.path.join(os.path.dirname(__file__), "static")

# UPLOAD_DIR is the path to your uploads directory
# By default it is set to ./static/uploads
UPLOAD_DIR = os.path.join(STATIC_PATH, 'uploads')

# Turn debugging on or off.
# default is True
DEBUG = True

# Compress the response
# By default COMPRESS_RESPONSE = True
COMPRESS_RESPONSE = True

# MAX_UPLOAD_SIZE is the maximum allowable size in bytes for a single file upload 
MAX_UPLOAD_SIZE = 100000000000

# EXPIRE_TIME is the number of hours before a file is expired and deleted
# Default value is 24 hours
EXPIRE_TIME = 24

# FILE_CLEANUP_SCHEDULE is the number of milliseconds between file
# cleanup operations. By default the file cleanup routine will run 
# once every 86400000 milliseconds which is 1 day. 
FILE_CLEANUP_SCHEDULE = 2000
