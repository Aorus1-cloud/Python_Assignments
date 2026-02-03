import os

def LineRead(fname):
    ret = False 

    ret = os.path.exists(fname)
    if not ret:
        print("No such file")
        return

    f = open(fname,"r")

    content = []

    content = f.readlines()

    f.close()

    for line in content:
        print(line,end="\n")

def main():
    filename = str()

    filename = input("Enter file name :")

    LineRead(filename)

if __name__ == "__main__":
    main()