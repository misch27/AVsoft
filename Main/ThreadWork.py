import threading

from Main.FTPConnection import FTPConnection
# work with Threads
class ThreadWork(threading.Thread):
    # static values
    lock = threading.Lock()
    url = log = pas = None
    globArr = []
    maxGlobCount = 0
    globCount = 0
    def __init__(self):
        super(ThreadWork, self).__init__()


    # props
    def setProp(self, url, log, pas):
        self.url = url
        self.log = log
        self.pas = pas

    # get static value for all threads
    # synchronized part
    def getCount(self):
        ThreadWork.lock.acquire(1)
        if(ThreadWork.globCount==ThreadWork.maxGlobCount):
            ThreadWork.lock.release()
            return None
        else:
            ThreadWork.globCount = ThreadWork.globCount + 1
            ThreadWork.lock.release()
            return ThreadWork.globCount

    # pars path to file
    def parsPath(self, path):
        arr = [str(path[0]), str(path[1]).split("\\")]
        return arr
    # run thred
    def run(self):
        while(True):
            nextInt = self.getCount()
            if(nextInt == None):
                break
            else:
                path = self.globArr[nextInt-1]
                con = FTPConnection(self.url, self.log, self.pas)
                con.ftp_upload(self.parsPath(path))


