import hashlib,os,sys,time

def logFileMaker(filename,filedata):
    timestamp = str(filename)       #safety
    timestamp = timestamp.replace(" ","_")
    timestamp = timestamp.replace(":","_")

    name = sys.argv[0]

    f = open(f"{timestamp}.txt","w")

    f.write(f"The output of script {name} is:\n")

    f.write(f"{str(filedata)} \n")      #for safety 

    f.close()
    

def Checksum(file):
    error = False

    error = os.path.exists(file)

    if not error:
        print("No such file")
        return
    
    error = os.path.isdir(file)

    if error:
        print("Not a file")
        return
    
    hobj = hashlib.md5()
    ret = str()
    content = str()

    Buffer = 1024

    f = open(file,"rb")

    content = f.read(Buffer)

    while len(content) > 0 :
        hobj.update(content)
        content = f.read(Buffer)

    ret = hobj.hexdigest()

    return ret

def CheckSumDir(Dir):
    Ret = False
    result = []

    Ret = os.path.exists(Dir)

    if not Ret:
        print("No such path")
        return
    
    Ret = os.path.isdir(Dir)

    if not Ret:
        print("Not a directory")
        return
    
    for FolderName,SubFolderName,FileName in os.walk(Dir):
        for file in FileName:
            result.append(Checksum(os.path.join(FolderName,file)))

    return result

def CheckDuplicate(dir):
    timestamp = time.ctime()

    Ret = False
    result = {}
    res = []

    Ret = os.path.exists(dir)

    if not Ret:
        print("No such path")
        return
    
    Ret = os.path.isdir(dir)

    if not Ret:
        print("Not a directory")
        return
    
    for FolderName,SubFolderName,FileName in os.walk(dir):
        for file in FileName:
            file = os.path.join(FolderName,file)
            checksum = Checksum(file)
            if checksum not in result:
                result[checksum] = [file]

            else:
                result[checksum].append(file)

    return result
    

def DeleteDuplicate(Dir):
    timestamp = time.ctime()
    duplicate = {}
    count = 0
    removed_files = []

    duplicate = CheckDuplicate(Dir)

    for values in duplicate.values():
        for subvalues in values:
            count = count + 1
            if count > 1 :
                removed_files.append(subvalues)
                os.remove(subvalues)

        count = 0

    return(removed_files) 

 