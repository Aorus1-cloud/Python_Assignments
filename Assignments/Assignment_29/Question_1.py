import os

def exists(filename):
    return os.path.exists(filename)

def main():
    res = False 

    FileName = input("Enter the file name :")

    res = exists(FileName)

    print("files Exists :",res)

if __name__ == "__main__":
    main()