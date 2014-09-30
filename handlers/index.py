
from handlers.base import Base
  
class Index(Base):
    def get(self):
        self.write('index')
