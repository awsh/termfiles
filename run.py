
import tornado.httpserver
import tornado.ioloop
import tornado.options
import config
import tools


from app import Application

from tornado.options import define, options

define("port", default=8000, help="run on the given port", type=int)

if __name__ == "__main__":

    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application(), max_body_size=100000000000)#100GB
    http_server.listen(options.port)
    tornado.ioloop.PeriodicCallback(tools.expire_files, config.FILE_CLEANUP_SCHEDULE).start()
    tornado.ioloop.IOLoop.instance().start()
