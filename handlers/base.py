
import config
import tornado.web

class Base(tornado.web.RequestHandler):
    '''
    Base class for handlers
    '''
    def write_error(self, status_code, **kwargs):
        '''
        Overrides default write_error to print
        plain text instead of html.
        '''
        if status_code == 404:
            self.write('\n404: Not Found\n\n')
