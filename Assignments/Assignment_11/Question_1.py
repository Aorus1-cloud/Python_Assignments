def Prime(No):
    if No == 0 or No == 1 or No < 1:
        return False 

    for i in range(2,No):

        if No % i == 0 :
            return False
        
    return True

def main():
    Res = True

    num = int(input("Enter the number : "))

    Res = Prime(num)

    if Res == True:
        print("The number is Prime")
    else:
        print("The number is not Prime")

if __name__ == "__main__":
    main()