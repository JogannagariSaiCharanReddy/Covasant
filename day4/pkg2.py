import glob
import os
from datetime import datetime,date
import time

class File():
    def __init__(self,path):
        self.path =path
        
    def get_files(self,path,files_dic={}):
        files = glob.glob(os.path.join(path, "*"))
        for file in files:
            if os.path.isfile(file):
                files_dic[file] = os.path.getsize(file)
            elif os.path.isdir(file):
                self.get_files(file, files_dic)
        return files_dic
       
    def getMaxSizeFile(self,n=1):
        files=self.get_files(self.path)
        return sorted(files,key=lambda file:files[file])[-n:]
        
    def getLatestFiles(self,cdate):
        files=self.get_files(self.path)
        d = datetime.combine(cdate,datetime.min.time())
        seconds = int(d.timestamp())
        latest_files={file:os.path.getctime(file)
                        for file in files
                                 if os.path.getctime(file)>seconds}
        return list(latest_files.keys())
        
            
        
        

        
   