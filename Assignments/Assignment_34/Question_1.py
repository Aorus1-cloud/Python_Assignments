import sys,schedule,time
from UserDefinedModule import Copyfiles,zipFile,log,Email,extract,History


def intermediate(Dir):
    global History_file
    Dest = "BackLinux"
    copied_files,timestamp,errors,c_time = Copyfiles(Dir,Dest)
    zipfile = zipFile(Dest,timestamp)
    logFile = log(timestamp,copied_files,zipfile,errors)
    Email(zipfile,logFile)
    History(timestamp,copied_files,zipfile,c_time)

def main():
    Border = "-"*53
    print(Border)
    print("-------Marvellous Platform Surveillance System-------")
    print(Border)

    if len(sys.argv) == 2:
        if sys.argv[1] == "--h" or sys.argv[1] == "--H":
            print("This script is used to :")
            print("1 : Takes auto backup at given time")
            print("2 : Backup only new and updated files")
            print("3 : Create an archieve of the backup periodically")
            print("4 : Extract zip into designated destination")
            print("5 : Automatically send email to the user after logging and backup")

        elif sys.argv[1] == "--u" or sys.argv[1] == "--U":
            print("Use the automation script as :\n")
            print("Scriptname.py TimeInterval SourceDirectory ")
            print("TimeInterval : The time in minutes for periodic scheduling")
            print("DirectoryName : The name of directory to be backed up\n")

            print("Use the extracting script as :\n")
            print("Scriptname.py --restore ZipFileName DestinationDirectory ")
            print("--restore : flag for extracting the zip file")
            print("ZipFileName : Name of zip file to extract")
            print("DestinationDirectory : The name of directory to extract the zip into")

        elif sys.argv[1].lower() == "--history":
            History_file = time.strftime("%d_%m_%Y")
            History_file = History_file +".log"
            try:
                    
                f = open(History_file,"r")
                content = f.read()
                print(content)
            except Exception as eobj:
                print(eobj)

        else:
            print("Unable to proceed as their is no such option")
            print("Please use --h or --u to get more details")

    # python Demo.py 5 Marvellous
    elif len(sys.argv) == 3:
        # Apply The Scheduler 
        schedule.every(int(sys.argv[1])).seconds.do(intermediate,sys.argv[2])

        print(Border)
        print("Data Shield System Started Successfully")
        print("Time interval in minutes :",sys.argv[1])
        print("Press Ctrl + C to stop the execution")
        print(Border)


        # Wait till abort
        while True:
            schedule.run_pending()
            time.sleep(1)

    # python Demo.py --restore .zip Dir
    elif len(sys.argv) == 4:
        if sys.argv[1].lower() == "--restore":
            extract(sys.argv[2],sys.argv[3])
            
    else:
        print("Invalid number of command line arguments")
        print("Unable to proceed as their is no such option")
        print("Please use --h or --u to get more details")


    print(Border)
    print("--------- Thank You for using our script ------------")
    print(Border)
    


if __name__ == "__main__":
    main()