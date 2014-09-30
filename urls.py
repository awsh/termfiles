import handlers.index
import handlers.files
import tornado.web

handler_urls = [
                (r'/', handlers.index.Index),
                (r'/(.*)', handlers.files.UploadFile),
                (r'/([\w]+)/(.*)', handlers.files.GetFile)
               ]
        

