import glob
import os
import datetime

class File():
    def __init__(self,path):
        self.path =path
       
    def getMaxSizeFile(self,n=1):
        def get_files(path, files_dic={}):
            files = glob.glob(os.path.join(path, "*"))
            for file in files:
                if os.path.isfile(file):
                    files_dic[file] = os.path.getsize(file)
                elif os.path.isdir(file):
                    get_files(file, files_dic)
            return files_dic
        files=get_files(self.path)
       
        print(sorted(files,key=lambda file:files[file])[-n:])
        
    #def getLatestFiles(self,date):
    #    print(date)

        
        
        

fs = File(r"C:\Users\Sai Charan\Desktop\Python\assignments")
fs.getMaxSizeFile(2) # gives two max file names 
#fs.getLatestFiles(datetime.date(2018,2,1))
#Returns list of files after 1st Feb 2018 