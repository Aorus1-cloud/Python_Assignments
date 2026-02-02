import os

def DisplayContent(filename):
    content = str()
    ret = False

    ret = os.path.exists(filename)
    if not ret:
        print("File does not exist in current directory ")
        return 
    
    f = open(filename,"r")

    content = f.read()

    print("The content of the file is :",content)

def main():
    fname = str()

    fname = input("Enter the file name :")

    DisplayContent(fname)

if __name__ == "__main__":
    main()