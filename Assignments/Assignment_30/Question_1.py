import os

def cntLines(fname):
    ret = False 

    ret = os.path.exists(fname)
    if not ret:
        print("No such file")
        return

    f = open(fname,"r")

    content = []

    content = f.readlines()

    f.close()

    return(len(content))

def main():
    filename = str()
    cnt = 0

    filename = input("Enter file name :")

    cnt = cntLines(filename)

    print(f"The number of lines in the file {filename} are {cnt}.")

if __name__ == "__main__":
    main()