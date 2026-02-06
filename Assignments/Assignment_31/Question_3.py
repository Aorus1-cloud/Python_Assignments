from sys import argv
from UserDefinedModule import CopyFiles

def main():
    if len(argv)==2:
        if argv[1].lower() == "--h":
            print("This is a files copying script which copies files from a dir to another.")
            print("This is a automation script.")
            return

        if argv[1].lower() == "--u":
            print("Use the given script as:")
            print("ScriptName.py Argument1 Argument2")
            print("Argument 1 : Directory_Name(From) ")
            print("Argument 2 : Directory_Name(To)")
            return

        else:
            print("Use the given flags as :")
            print("--u: use to display the usage")
            print("--h: use to display the help")
            return

    elif len(argv) <= 1 or len(argv) > 3:
        print("Invalid number of command line arguments")
        print("Use the given flags as :")
        print("--u: use to display the usage")
        print("--h: use to display the help")
        return

    else:

        Dir1 = str()
        Dir2 = str()

        Dir1 = argv[1]
        Dir2 = argv[2]

        CopyFiles(to_dir=Dir2,from_dir = Dir1)
        
if __name__ == "__main__":
    main()
