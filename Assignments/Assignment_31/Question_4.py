from sys import argv
from UserDefinedModule import DirectoryCopyExt

def main():
    if len(argv)==2:
        if argv[1].lower() == "--h":
            print("This is a files copying script which copies files with specified extension to another directory.")
            print("This is a automation script.")
            return

        if argv[1].lower() == "--u":
            print("Use the given script as:")
            print("ScriptName.py Argument1 Argument2 Argument3")
            print("Argument 1 : Directory_Name(From)")
            print("Argument 2 : Directory_Name(To)")
            print("Argument 3 : Extension")
            return

        else:
            print("Use the given flags as :")
            print("--u: use to display the usage")
            print("--h: use to display the help")
            return

    elif len(argv) <= 1 or len(argv) > 4:
        print("Invalid number of command line arguments")
        print("Use the given flags as :")
        print("--u: use to display the usage")
        print("--h: use to display the help")
        return

    else:
        Dir1 = str()
        Dir2 = str()
        ext = str()

        Dir1 = argv[1]
        Dir2 = argv[2]
        ext = argv[3]

        DirectoryCopyExt(to_dir=Dir2,from_dir = Dir1,ext=ext)

if __name__ == "__main__":
    main()