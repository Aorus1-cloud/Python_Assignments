import hashlib
import os
import sys

def compare(f1name,f2name):
    ret = False 

    ret = os.path.exists(f1name)
    if not ret:
        print("No such files")
        return
    
    ret = os.path.exists(f2name)
    if not ret:
        print("No such files")
        return

    File1 = open(f1name,"rb")
    File2 = open(f2name,"rb")

    F1Content = File1.read()
    F2Content = File2.read()

    checksum1 = hashlib.md5()
    checksum2 = hashlib.md5()

    checksum1.update(F1Content)
    F1Checksum = checksum1.hexdigest()

    checksum2.update(F2Content)
    F2Checksum = checksum2.hexdigest()

    if F1Checksum == F2Checksum :
        return True 
    
    else:
        return False

def main():
    fname = str()
    Ret = False

    fname1 = sys.argv[1]
    fname2 = sys.argv[2]

    Ret = compare(fname1,fname2)
    if Ret:
        print("Success")

    else:
        print("Failure")

if __name__ == "__main__":
    main()