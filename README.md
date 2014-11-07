#File hosting for terminal uploads
This code currently powers termfiles.com

##Upload a file:
`curl --upload-file filename.ext http://localhost:8000/filename.ext`

##Retrieve a file:
`wget http://localhost:8000/XXXXXXXX/filename.ext`

##Download several files as an archive:
`wget -O filename.(zip|tar|tar.gz|tar.bz2) http://localhost:8000/XXXXXXXX/file1.ext+XXXXXXXX/file2.ext=filename.(zip|tar|tar.gz|tar.bz2)`


