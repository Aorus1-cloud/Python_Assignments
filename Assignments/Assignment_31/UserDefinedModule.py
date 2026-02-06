import os,sys,time,shutil

def FindFiles(dir,extension):
    Ret = False
    ans = []
  
    Ret = os.path.exists(dir)
    if not Ret:
        print("No such directory")
        return
    
    Ret = os.path.isdir(dir)
    if not Ret:
        print("Not a directory")
        return

    for FolderName,SubFolderName,FileName in os.walk(dir):
        if len(FileName) == 0:
            return ans

        for files in FileName:
            if files.endswith(extension):
                ans.append(os.path.abspath(files))
            
    return ans
            
def logFileMaker(filename,filedata):
    timestamp = str(filename)       #safety
    timestamp = timestamp.replace(" ","_")
    timestamp = timestamp.replace(":","_")

    name = sys.argv[0]

    f = open(f"{timestamp}.log","w")

    f.write(f"The output of script {name} is:\n")

    f.write(str(filedata))      #for safety 

    f.close()
    
def ExtChanging(to_ext,from_ext,Directory):
    Ret = False

    Ret = os.path.exists(Directory)

    if not Ret:
        print("No such directory")
        return
    
    Ret = os.path.isdir(Directory)

    if not Ret:
        print("Not a directory")
        return

    Timestamp = time.ctime()
    res = []

    for FolderName,SubFolderName,FileName in os.walk(Directory):
        for file in FileName:
            if file.endswith(from_ext):
                FileStart = file.split(".")
                os.rename(os.path.join(FolderName,file),os.path.join(FolderName,f"{FileStart[0]}{to_ext}"))
                res.append(file)    
    
    
    logFileMaker(Timestamp,f"Files {res} renamed Successfully.")

def CopyFiles(from_dir,to_dir):
    timestamp = time.ctime()
    os.makedirs(to_dir,exist_ok=True)
    Ret = False
    files = []

    Ret = os.path.exists(from_dir)

    if not Ret:
        print("No such directory")
        return
    
    Ret = os.path.isdir(from_dir)
    
    if not Ret:
        print("Not a directory")
        return

    for FolderName,SubFolderName,FileName in os.walk(from_dir):
        for File in FileName:

            shutil.copy2(os.path.join(FolderName,File),to_dir)          # copy() does not copy metadata(created_at,etc) and permissions
    
            files.append(File)

    logFileMaker(filename=timestamp,filedata=f"files {files} copied to {to_dir} from {from_dir}.")

def DirectoryCopyExt(from_dir,to_dir,ext):
    timestamp = time.ctime()
    result = []
    Ret = False
    os.makedirs(to_dir,exist_ok=True)

    Ret = os.path.exists(from_dir)
    if not Ret:
        print("No such directory")
        return
    
    Ret = os.path.isdir(from_dir)
    if not Ret:
        print("Not a directory")
        return
    
    for FolderName,SubFolderName,FileName in os.walk(from_dir):
        for files in FileName:
            if files.endswith(ext):
                shutil.copy2(os.path.join(FolderName,files),to_dir)
                result.append(files)

    logFileMaker(filename=timestamp,filedata=f"Files with extension {ext} are {result} and are copied to {to_dir} from {from_dir}.")

