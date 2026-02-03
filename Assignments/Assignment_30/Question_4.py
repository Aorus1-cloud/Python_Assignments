def copydata(from_file,to_file):
    content = str()

    copying_file = open(from_file,"r")
    into_file = open(to_file,"w")

    content = copying_file.read()

    copying_file.close()

    into_file.write(content)

    into_file.close()

    print("The content is successfully copied")    

def main():
    file1 = str()
    file2 = str()

    file1 = input("Enter the file to copy from :")

    file2 = input("Enter the file to copy to :")

    copydata(from_file=file1,to_file=file2)

if __name__ == "__main__":
    main()