from sys import argv
from UserDefinedModule import DeleteDuplicate,logFileMaker

def main():
    if len(argv) <= 1 or len(argv) > 2:
        print("Invalid number of command line arguments")
        print("Use the given flags as :")
        print("--u: use to display the usage")
        print("--h: use to display the help")
        return

    if argv[1].lower() == "--h":
        print("This application deletes the duplicate files in the given directory.")    
        print("This is a automation script.")
        return

    if argv[1].lower() == "--u":
        print("Use the given script as:")
        print("ScriptName.py Argument1 ")
        print("Argument 1 : Directory_Name")
        return

    else:
        Dir = str()

        Dir = argv[1]

        res = DeleteDuplicate(Dir)
        
        logFileMaker(filename="log",filedata=f"Removed Duplicate files : {res}")
        
if __name__ == "__main__":
    main()

