import UserdefinedModule
from sys import argv
import schedule
import time

def intermediate():
    UserdefinedModule.Log(argv[1])
    
def main():
    if len(argv)==2:
        if argv[1].lower() == "--h":
            print("This is a system info logging script then the lof file is send to the user through mail.")
            print("This is a automation script.")
            return

        if argv[1].lower() == "--u":
            print("Use the given script as:")
            print("ScriptName.py Argument1 Argument2 Argument3")
            print("Argument 1 : Directory_Name")
            print("Argument 2 : Receivers Email")
            print("Argument 3 : Time interval in minutes")
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
        print("The script is running.")
        print("Press Ctrl + C to stop the execution")
        schedule.every(int(argv[3])).minutes.do(intermediate)

        while True:
            schedule.run_pending()
            time.sleep(1)
            

if __name__ == "__main__":
    main()