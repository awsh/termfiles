import config
import urls
import tornado.web

class Application(tornado.web.Application):
    def __init__(self):
        app_urls = urls.handler_urls
        
        settings = {
            "template_path"       : config.TEMPLATE_PATH,
            "static_path"         : config.STATIC_PATH,
            "debug"               : config.DEBUG,
            "compress_response"   : config.COMPRESS_RESPONSE
            }
        
        tornado.web.Application.__init__(self, app_urls, **settings)

