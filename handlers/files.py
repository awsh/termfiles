
from handlers.base import Base
  
class UploadFile(Base):
    def put(self, filename):
        file = self.request.body
        with open(filename, 'wb') as file:
            file.write(self.request.body)
        self.write('\nhttp://localhost:8000/' + filename + '\n\n')

class GetFile(Base):
    def get(self, hash, filename):
        pass
