import psutil,time,os
from functools import reduce
import smtplib
from email.message import EmailMessage
from sys import argv


def SendMail(email,path):
    message = EmailMessage()

    message["To"] = email
    message["From"] = "demo89631@gmail.com"
    message["Subject"] = "Periodic Email About Server System Info with Hot Process Monitoring"

    message.set_content("This mail is about the system info and the hot processes running on it.")
    
    f = open(path,"rb")
    content = f.read()

    message.add_attachment(content,maintype = "application",subtype = "log",filename = f"{os.path.basename(path)}")

    smtp = smtplib.SMTP_SSL("smtp.gmail.com",465)

    smtp.login("demo89631@gmail.com","qexpqfwefsfbytcu")

    smtp.send_message(message)

    smtp.close()

def filter_process(list):
    hot = []
    for proc in range(len(list)-1):
        if len(hot)<1:
            hot.append(list[proc])
        
        elif list[proc]["ram_usage"] == 0.00:
            pass

        else:
            for hotest in hot:
                if hotest["ram_usage"] < list[proc]["ram_usage"]:
                    hot.append(list[proc])
                    break

    result = []

    while len(result) < 10:
        res = {}

        res = reduce((lambda x,y:x if x["ram_usage"] > y["ram_usage"] else y),hot)

        hot.remove(res)

        result.append(res)

    return result
    
def Log(Folder):

    Ret = False

    Ret = os.path.isfile(Folder)
    if Ret:
        print("Cannot create such file")
        return
    
    Ret = os.path.exists(Folder)

    if not Ret:
        os.mkdir(Folder)

    Border = "-"*66
    timestamp = f"{time.strftime("%Y-%m-%d_%H-%M-%S")}_sysInfo.log"
    log_file = os.path.join(Folder,timestamp)
    f = open(log_file,"w")

    f.write(Border+"\n")
    f.write("------This is the log report of the system info of the server.----\n")
    f.write(Border+"\n")
    f.write("\n\n")

    f.write("---------------------------System Report--------------------------\n")

    # print("CPU Usage : ",psutil.cpu_percent())
    f.write("CPU Usage : %s %%\n" %psutil.cpu_percent())
    f.write(Border+"\n")

    mem = psutil.virtual_memory()
    # print("RAM Usage : ",mem.percent)
    f.write("RAM Usage : %s %% \n" %mem.percent)
    f.write(Border+"\n")


    f.write("\n Disk Usage Report \n")
    f.write(Border+"\n")

    for part in psutil.disk_partitions():
        try:
            usage = psutil.disk_usage(part.mountpoint)
            # print(f"{part.mountpoint} used {usage.percent}%%")
            f.write("%s -> %s %% used \n" %(part.mountpoint,usage.percent))

        except:
            pass
    f.write(Border+"\n")

    net = psutil.net_io_counters()

    f.write("\nNetwork Usage Report\n")

    f.write("Sent : %.2f Mb\n" %(net.bytes_sent / (1024*1024)))
    f.write("Recv : %.2f Mb\n" %(net.bytes_recv / (1024*1024)))
    f.write(Border+"\n")

    process_info = Process_and_thread_info()

    hot_processes = []

    hot_processes = filter_process(process_info)
    f.write("------------------Top Memory Consuming Processes------------------\n")
    for hot in (hot_processes):
        f.write(Border+"\n")
        f.write(f"PID : {hot.get("pid")}\n")
        f.write(f"Process Name : {hot.get("name")}\n")
        f.write(f"Owner : {hot.get("username")}\n")
        f.write("CPU Usage : %.2f %% \n" %hot.get("cpu_percent"))
        f.write("RAM Usage in percent : %.2f %% \n" %hot.get("memory_percent"))
        f.write("RAM Usage : %.2f MB \n" %hot.get("ram_usage"))
        f.write("Virtual Memory: %.2f MB \n" %hot.get("virtual_memory"))
        f.write(f"Status : {hot.get("status")}\n")
        f.write(f"Create Time : {hot.get("create_time")}\n")
        f.write(f"Threads Count : {hot.get("threads")}\n")
        f.write(f"File Opened Count : {hot.get("file_opened")}\n")

    f.write(Border+"\n")
    f.write("----------------------All Running Process-------------------------\n")
    for proc in process_info:
        f.write(Border+"\n")
        f.write(f"PID : {proc.get("pid")}\n")
        f.write(f"Process Name : {proc.get("name")}\n")
        f.write(f"Owner : {proc.get("username")}\n")
        f.write("CPU Usage : %.2f %% \n" %proc.get("cpu_percent"))
        f.write("RAM Usage in percent : %.2f %% \n" %proc.get("memory_percent"))
        f.write("RAM Usage : %.2f MB \n" %proc.get("ram_usage"))
        f.write("Virtual Memory: %.2f MB \n" %proc.get("virtual_memory"))
        f.write(f"Status : {proc.get("status")}\n")
        f.write(f"Create Time : {proc.get("create_time")}\n")
        f.write(f"Threads Count : {proc.get("threads")}\n")
        f.write(f"File Opened Count : {proc.get("file_opened")}\n")

    f.write(Border+"\n")
    f.write("------------------------ End of log file -------------------------\n")
    f.write(Border+"\n")

    SendMail(argv[2],log_file)

def ProcessMonitor():
    process_info = []

    # WarmUp Try
    for proc in psutil.process_iter():
        try:
            proc.cpu_percent()
        except:
            pass

    time.sleep(0.2)

    try:
        for proc in psutil.process_iter(attrs=["pid","name","username","cpu_percent","memory_percent","status","create_time"]):

            info = proc.as_dict(attrs=["pid","name","username","cpu_percent","memory_percent","status","create_time"])
            try:
                info["create_time"] = time.strftime("%Y-%m-%d_%H-%M-%S",time.localtime(info["create_time"]))
                
            except:
                info["create_time"] = "NA"

            process_info.append(info)
        
    except(psutil.NoSuchProcess,psutil.AccessDenied,psutil.ZombieProcess):
        pass

    return process_info


def Process_and_thread_info():
    process = ProcessMonitor()
    try:
        for proc in process:
            single_proc = psutil.Process(proc.get("pid"))

            proc["threads"] = single_proc.num_threads()
            proc["file_opened"] =  len(single_proc.open_files())
            proc["ram_usage"] = single_proc.memory_info().rss / 1024 ** 2
            proc["virtual_memory"] = single_proc.memory_info().vms / 1024 ** 2

            if proc["ram_usage"] == None:
                proc["ram_usage"] = 0.0
                 
            # proc["file_opened"].append(f"path ='{file.path}',fd = {file.fd} , position = {file.position}, mode = {file.mode} , flags = {file.flags}")

    except PermissionError:
        pass

    except psutil.AccessDenied:
        for proc in process:
            proc["file_count"] = "Error -> Access Denied"

    return(process)
            
