
from handlers.base import Base
  
class Index(Base):
    def get(self):
        contents = """
       
        termfiles(1)                    User Manuals                    termfiles(1)

        NAME
            termfiles.com - terminal based file sharing

        SYNOPSIS
            curl --upload-file [filename] http://termfiles.com/[filename]

        DESCRIPTION
            Share files directly from your terminal using any application that supports HTTP PUT

        EXAMPLES
            To upload a file:

                curl --upload-file test.txt http://termfiles.com/test.txt

            
            To retrieve a file:

                wget http://termfiles.com/ABCDEFGH/test.txt

            
            To retrieve multiple files as an archive:

                wget http://termfiles.com/ABCDEFGH/test1.txt+ZYXWVUTS/test2.txt=myfile.zip
            
            Supported archive types are zip, tar, tar.gz, tar.bz2
        

        BUGS
            Please report any issues at https://github.com/awsh/termfiles/issues

        SEE ALSO
            http://transfer.sh\n\r\n""" 

        self.write(contents)
