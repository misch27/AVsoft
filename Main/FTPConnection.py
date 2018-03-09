from ftplib import FTP
class FTPConnection(object):
    url = log = pas = None
    def __init__(self, url, log, pas):
        # set property
        self.url = url
        self.log = log
        self.pas = pas
    def getCon(self): #get connection
        ftp = FTP(self.url, self.log, self.pas)
        return ftp
    def ftp_upload(self, path): #upload file
        ftp_obj = self.getCon()
        try:
            fileName = path[0].split("\\")
            fileName = fileName[len(fileName)-1]
            for val in path[1]:
                if val in ftp_obj.nlst():
                    #Use old directory
                    ftp_obj.cwd(val)
                else:
                    # Create new directory
                    ftp_obj.mkd(val)
                    ftp_obj.cwd(val)
            try:
                with open(path[0], 'rb') as fobj:
                    # doesn't check for file in the directory, uploads by default
                    ftp_obj.storbinary('STOR ' + fileName, fobj, 1024)
                print("file - " + fileName + " load successful")
            except Exception:
                print("Load file "+fileName + " error")
        finally:
            ftp_obj.quit()

