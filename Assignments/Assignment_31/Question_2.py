from UserDefinedModule import ExtChanging
from sys import argv

def main():
    if len(argv)==2:
        if argv[1].lower() == "--h":
            print("This is a files renaming script which renames files with specified extension to specified extension.")
            print("This is a automation script.")
            return

        if argv[1].lower() == "--u":
            print("Use the given script as:")
            print("ScriptName.py Argument1 Argument2 Argument3")
            print("Argument 1 : Directory_Name ")
            print("Argument 2 : Extension intial")
            print("Argument 3 : Extension final")

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
            
        Foldername = str()
        ext_intially = str()
        ext_final = str()

        Foldername = argv[1]
        ext_intially = argv[2]
        ext_final = argv[3]

        ExtChanging(Directory=Foldername,from_ext=ext_intially,to_ext=ext_final)


if __name__ == "__main__":
    main()