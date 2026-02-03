import os
import string

def cntWords(fname):
    ret = False 

    ret = os.path.exists(fname)
    if not ret:
        print("No such file")
        return

    f = open(fname,"r")

    content = []

    content = f.read()

    f.close()

    content = content.split()
    
    content = [word.strip(string.punctuation) for word in content]

    print(content)
    
    return(len(content))

def main():
    filename = str()
    cnt = 0

    filename = input("Enter file name :")

    cnt = cntWords(filename)

    print(f"The number of words in the file {filename} are {cnt}.")

if __name__ == "__main__":
    main()