from sys import argv
from UserDefinedModule import CheckSumDir,logFileMaker

def main():
    if len(argv) <= 1 or len(argv) > 2:
        print("Invalid number of command line arguments")
        print("Use the given flags as :")
        print("--u: use to display the usage")
        print("--h: use to display the help")
        return

    if argv[1].lower() == "--h":
        print("This application gives the checksum of all files in the given directory.")    
        print("This is a automation script.")
        return

    if argv[1].lower() == "--u":
        print("Use the given script as:")
        print("ScriptName.py Argument1 ")
        print("Argument 1 : Directory_Name")
        return

    else:
        Dir = str()
        ret = []

        Dir = argv[1]

        ret = CheckSumDir(Dir=Dir)

        if len(ret)==0:
            logFileMaker("log","No file found.")

        logFileMaker("log",f"The checksum of all the files is :\n {ret}")

if __name__ == "__main__":
    main()

