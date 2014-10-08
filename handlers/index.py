
from handlers.base import Base
  
class Index(Base):
    def get(self):
        if "Mozilla" in self.request.headers['User-Agent']:
            self.render("index.html")
        else:
            self.write("""
       
        termfiles(1)                    User Manuals                    termfiles(1)


        NAME
            termfiles.com - share files from your terminal

        SYNOPSIS
            curl --upload-file [FILE] http://termfiles.com/[FILE]

        DESCRIPTION
            Share FILE(s) from your terminal using any application that supports HTTP PUT.

        EXAMPLES
            Upload a file:
                curl --upload-file [FILE] http://termfiles.com/[FILE]
            
            Retrieve a file:
                wget http://termfiles.com/ABCDEFGH/[FILE]

            
            Retrieve multiple files as an archive:
                wget http://termfiles.com/ABCDEFGH/[FILE]+ZYXWVUTS/[FILE]=[ARCHIVE]
            Supported archive types are zip, tar, tar.gz, tar.bz2
        
        BUGS
            Please report any issues at https://github.com/awsh/termfiles/issues

        SEE ALSO
            http://transfer.sh - command line and web file sharing
            
        

        termfiles(1)                    October 2014                    termfiles(1)\n\r\n""") 
 
