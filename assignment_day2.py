import os

path=r"C:\Users\Sai Charan\Desktop\Python"

#question 3 function to return file of maximum size
def max_sized_file(path,max_file={}):
    for file in os.listdir(path):
        file=path+"\\"+file
        if os.path.isfile(file):
            max_file[file]=os.path.getsize(file)
        elif os.path.isdir(file):
            max_sized_file(file,max_file)
                
    return sorted(max_file,key=lambda file:max_file[file])[-1]

#question 4 function to return all files in given directory with provided extension
def list_files_by_given_type(path,ext):
    with open("files_list.txt","wt") as f:
        for item in os.listdir(path):
            item=path+"\\"+item
            if os.path.isdir(item):
                list_files_by_given_type(item,ext)
            elif ext in item:
                f.writelines(item+"\n")
            



list_files_by_given_type(path,".py")


#print(max_sized_file(path))
                
    

