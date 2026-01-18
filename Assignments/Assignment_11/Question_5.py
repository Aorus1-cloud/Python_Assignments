def Palindrome(No):
    reverse = No[::-1]

    if No == reverse:
        return True
    else :
        return False
    
    # for short
    #return No == No[::-1]
    

def main():
    res = True

    number = input("Enter the number :").strip()

    res = Palindrome(number)

    if res == True:
        print("The number is Palidrome")
    else:
        print("The number is not Palidrome")

if __name__ == "__main__":  
    main()