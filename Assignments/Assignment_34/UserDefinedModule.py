import os,shutil,hashlib,zipfile,time,smtplib
from email.message import EmailMessage

def CalculateChecksum(fileName):
    hobj = hashlib.md5()
    Ret = False 
    Ret = os.path.exists(fileName)

    if not Ret:
        return
    
    Ret = os.path.isdir(fileName)
    if Ret:
        return
    
    f = open(fileName,"rb")

    content = f.read(1024)
    while content :
        hobj.update(content)
        content = f.read(1024)

    result = hobj.hexdigest()

    return result

# def logfile(data):


def Copyfiles(Source_Dir,Dest_Dir):
    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    c_time = time.ctime()
    copied_files = []
    errors = []
    Ret = False
    Ret = os.path.isfile(Dest_Dir)
    if Ret:
        return
    
    Ret = os.path.exists(Dest_Dir)
    if not Ret:
        os.mkdir(Dest_Dir)

    for FolderName,SubFolderName,FileName in os.walk(Source_Dir):
        try:
            for file in FileName:
                if file.endswith((".temp",".log",".exe")):
                    continue

                file = os.path.join(FolderName,file)

                relative = os.path.relpath(file,Source_Dir)

                dest_path = os.path.join(Dest_Dir,relative)

                os.makedirs(os.path.dirname(dest_path),exist_ok=True)


                if not os.path.exists(dest_path) or CalculateChecksum(file) != CalculateChecksum(dest_path):
                    shutil.copy2(file,dest_path)
                    copied_files.append(dest_path)

        except Exception as eobj:
            errors.append(eobj)

    return copied_files,timestamp,errors,c_time

def zipFile(FolderName,zipfilename):
    fileName =  FolderName+"_"+zipfilename + ".zip"
    
    result = []
    Ret = False
    Ret = os.path.isfile(FolderName)
    if Ret:
        result.append("Not a folder")
        return
    
    Ret = os.path.exists(FolderName)
    if not Ret:
        result.append("No such Path")
        return

    zobj = zipfile.ZipFile(fileName,'w',zipfile.ZIP_DEFLATED)

    for root,sub,files in os.walk(FolderName):
        for file in files:
            try:
                fname = os.path.join(root,file)
                relative = os.path.relpath(fname,FolderName)

                zobj.write(fname,relative)
            except Exception:
                pass

    zobj.close()
    return fileName

def log(time,copied_filess,zip_filename,err):
    LogFilePath = os.path.join("Logs",f"{time}_Backlinux.log")

    os.makedirs(os.path.dirname(LogFilePath),exist_ok=True)

    f = open(LogFilePath,"w")

    Border = "-"*50

    f.write(Border+"\n")
    f.write("-------------- Folder Backup Report --------------\n")
    f.write(Border+"\n\n")

    f.write(f"Time :- {time}\n\n")
    # f.write(Border+"\n")

    f.write(f"----------------- Files Copied -------------------\n")
    if len(copied_filess) == 0:
        f.write("No file to backup.\n\n")

    for files in copied_filess:
        f.write(f"{files}\n")
        f.write(Border+"\n\n")
    
    f.write(f"-------------------- Errors ----------------------\n")
    if len(err) == 0:
        f.write("No err occured.\n\n\n")
    for files in err:
        f.write(f"{files}\n")
        f.write(Border+"\n\n")

    f.write(f"Zip File Name :- {zip_filename}\n\n\n")
    f.write(Border+"\n")
    f.write("----------------- End Of Report ------------------\n")
    f.write(Border+"\n")

    return(LogFilePath)

def Email(zipFile,logFile):
    message = EmailMessage()

    message["To"] = "patiljayesh9923@gmail.com"
    message["From"] = "demo89631@gmail.com"
    message["Subject"] = "BackUp Log and Zip File Report"

    message.set_content(f"This is email with attached log and zip file of the data backup of the system after periodic time.")
    f = open(zipFile,"rb")
    content = f.read()

    message.add_attachment(content,maintype = 'application',subtype = 'zip',filename = zipFile)

    f = open(logFile,"rb")
    content = f.read()
    message.add_attachment(content,maintype='application',subtype='log',filename = os.path.basename(logFile))

    smtp = smtplib.SMTP_SSL("smtp.gmail.com",465)

    smtp.login("demo89631@gmail.com","qexpqfwefsfbytcu")

    smtp.send_message(message)

    smtp.close()

def extract(ZipName,Destination):
    Ret = False
    Ret = os.path.exists(ZipName)
    if not Ret:
        print("No such Zip file")
        return
    
    Ret = os.path.isdir(ZipName)
    if Ret:
        print("Not a Zip file")
        return
    
    Ret = os.path.exists(Destination)
    if not Ret:
        os.makedirs(Destination)

    try:
        zip = zipfile.ZipFile(ZipName,"r")

        zip.extractall(Destination)

    except Exception as eobj:
        print(eobj)
        return

def History(timestamp,files,zipfile,c_time):
    Border = "-"*50
    Date = time.strftime("%d_%m_%Y")
    history_file = Date +".log"

    f = open(history_file,"a")

    f.write(Border+"\n")
    f.write("---------------- BackUp History ------------------\n")
    f.write(Border+"\n")

    f.write(f"BackUp Proccesed At : {timestamp}\n")
    f.write(f"Files Backuped : {len(files)}\n")
    f.write(f"Zip size : {os.path.getsize(zipfile)/1024**2} MB\n\n")

    return history_file
