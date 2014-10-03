import handlers.index
import handlers.files
import tornado.web
import config
import os

handler_urls = [
                (r'/', handlers.index.Index),
                (r'/([-a-zA-Z0-9._]+)', handlers.files.Files),
                (r'/([-a-zA-Z0-9._/]+)', tornado.web.StaticFileHandler, 
                                                    {'path': config.UPLOAD_DIR})
               ]
        

