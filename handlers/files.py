
from handlers.base import Base
import config
import tornado.web
import tempfile
import os

@tornado.web.stream_request_body
class UploadFile(Base):
        
    def put(self, filename):
        self.write('\nhttp://localhost:8000/' + filename + '\n\n')
        self.finish()
        self.temp_file.seek(0)
        with open(os.path.join(config.UPLOAD_DIR, self.filename), 'wb') as file:
            file.write(self.temp_file.read())
        self.temp_file.close()

    def prepare(self):
        self.filename = self.request.uri.strip('/')
        self.temp_file = tempfile.NamedTemporaryFile()
        self.received = 0

    def data_received(self, chunk):
        self.received += len(chunk)
        if self.received > config.MAX_UPLOAD_SIZE:
            self.write_error(413)
            self.finish()
        else:
            self.temp_file.write(chunk)

    def write_error(self, status_code, **kwargs):
        self.set_status(status_code)
        self.write('Upload too large')

class GetFile(Base):
    def get(self, hash, filename):
        pass
