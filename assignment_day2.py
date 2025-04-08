import os

path=r"C:\Users\Sai Charan\Desktop\Python\\"

#function to return file of maximum size
def max_sized_file(path):
    max_file=""
    max_file_size=0
    if os.path.isdir(path):
        for file in os.listdir(path):
            if os.path.isfile(path+file) and os.path.getsize(path+file)>max_file_size:
                max_file_size=os.path.getsize(path+file)
                max_file=file
    return max_file if len(max_file)>0 else "No files in path"

#function to return all files in given directory with provided extension
def list_files_by_given_type(path,ext):
    files=[]
    for item in os.listdir(path):
        if os.path.isdir(path+item):
            files+=list_files_by_given_type(path+item,ext)
        elif ext in item:
            files.append(item)
    return files
            

print(list_files_by_given_type(path,".py"))


#print(max_sized_file(path))
                
    

