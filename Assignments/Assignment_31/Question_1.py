from UserDefinedModule import FindFiles,logFileMaker
import sys,time

def main():

    if len(sys.argv)==2:
        if sys.argv[1].lower() == "--h":
            print("This is a files finding script with file extension.")
            print("This is a automation script.")
            return

        if sys.argv[1].lower() == "--u":
            print("Use the given script as:")
            print("ScriptName.py Argument1 Argument2")
            print("Argument 1 : Directory_Name ")
            print("Argument 2 : Extension ")
            return

        else:
            print("Use the given flags as :")
            print("--u: use to display the usage")
            print("--h: use to display the help")
            return

    elif len(sys.argv )<= 1 or len(sys.argv) > 3:
        print("Invalid number of command line arguments")
        print("Use the given flags as :")
        print("--u: use to display the usage")
        print("--h: use to display the help")
        return

    else:
        file = str()
        ret = []

        directory = sys.argv[1]
        extension = sys.argv[2]

        file = time.ctime()
        ret = FindFiles(dir=directory,extension=extension)

        logFileMaker(filename=file,filedata=ret)

if __name__ == "__main__":
    main()