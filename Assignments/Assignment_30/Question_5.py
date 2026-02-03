import os
import string

def FindWord(fname,word):
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

    for words in content:
        if words == word:
            return True

    return False

def main():
    filename = str()
    cnt = False

    filename = input("Enter file name :")
    w = input("Enter the word :")

    cnt = FindWord(filename,w)

    print(f"Is the word in the file {filename} : {cnt}.")

if __name__ == "__main__":
    main()