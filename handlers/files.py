from handlers.base import Base
import config
import tornado.web
import tempfile
import os
import hashlib
import string
import random
import zipfile
import tarfile

@tornado.web.stream_request_body
class UploadFile(Base):
    '''
    Streams input from http put request to a tempfile and writes 
    out to config.UPLOAD_DIR
    '''
    def put(self, filename):
        url = ''.join(random.choice(string.digits) for _ in range(8))
        
        self.write('\nmd5sum: {0}\n{1}/{2}/{3}\n\n'.format(self.hash.hexdigest(),
                                                   config.URL,
                                                   url,
                                                   filename))
        self.finish()
        
        if not os.path.exists(os.path.join(config.UPLOAD_DIR, url)):
            os.makedirs(os.path.join(config.UPLOAD_DIR, url))

        self.temp_file.seek(0)
        with open(os.path.join(os.path.join(config.UPLOAD_DIR, url), filename), 'wb') as file:
            file.write(self.temp_file.read())
        self.temp_file.close()

    def prepare(self):
        self.temp_file = tempfile.NamedTemporaryFile()
        self.received = 0
        self.hash = hashlib.md5()

    def data_received(self, chunk):
        self.received += len(chunk)
        if self.received > config.MAX_UPLOAD_SIZE:
            self.write_error(413)
            self.finish()
        else:
            self.hash.update(chunk)
            self.temp_file.write(chunk)

    def write_error(self, status_code, **kwargs):
        self.set_status(status_code)
        self.write('Upload too large')


class Archive(Base):
    '''
    Generates an archive of files and 
    redirects user to download link
    '''
    def get(self, files, filename, ext):
        ext = ext.lower()
        url = ''.join(random.choice(string.digits) for _ in range(8))
        if not os.path.exists(os.path.join(config.UPLOAD_DIR, url)):
            os.makedirs(os.path.join(config.UPLOAD_DIR, url))
    
        full_filename = "{0}.{1}".format(filename, ext)
        file_out = os.path.join(config.UPLOAD_DIR,
                                os.path.join(url, full_filename))

        if ext == "zip": 
            with zipfile.ZipFile(file_out, 'w') as f:
                for file in files.split('+'):
                    f.write(os.path.join(config.UPLOAD_DIR, file), file.split('/')[1])
        elif ext == "tar":
            with tarfile.open(file_out, 'w') as f:
                for file in files.split('+'):
                    f.add(os.path.join(config.UPLOAD_DIR, file), file.split('/')[1])
        elif ext == "tar.gz":
            with tarfile.open(file_out, 'w:gz') as f:
                for file in files.split('+'):
                    f.add(os.path.join(config.UPLOAD_DIR, file), file.split('/')[1])
        elif ext == "tar.bz2":
            with tarfile.open(file_out, 'w:bz2') as f:
                for file in files.split('+'):
                    f.add(os.path.join(config.UPLOAD_DIR, file), file.split('/')[1])
        else:
            self.write("\nUnsupported archive type.\n\n")
            return
        self.redirect("{0}/{1}/{2}.{3}".format(config.URL, url, filename, ext))
        
