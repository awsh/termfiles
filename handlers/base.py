
import config
import tornado.web

class Base(tornado.web.RequestHandler):
    
    def write_error(self, status_code, **kwargs):
        if status_code == 404:
            self.write('\n404: Not Found\n\n')
