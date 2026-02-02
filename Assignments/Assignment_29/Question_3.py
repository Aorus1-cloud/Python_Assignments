import os
import sys
def copy(fname):
    ret = False
    file_content = str()

    ret = os.path.exists(fname)
    if not ret:
        print("Enter valid path")
        return

    file = open(fname,"r")

    file_content = file.read()

    new_file = open("Demo.txt","w")

    new_file.write(file_content)

    print("Data copied successfully")

def main():
    filename = str()

    filename = sys.argv[1]

    copy(filename)

if __name__ == "__main__":
    main()