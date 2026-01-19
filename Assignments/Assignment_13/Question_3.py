def perfect(No):
    Divisor = list()
    sum = 0

    for i in range(1,No):
        if No % i == 0:
            Divisor.append(i)
    
    for i in range(len(Divisor)):
        sum = sum + Divisor[i]
    
    if sum == No:
        return True
    
    return False
    
def main():
    res = False 

    number = int(input("Enter the number :"))

    res = perfect(number)

    if res == True:
        print("The number is perfect number.")
    elif res == None:
        print("Lafda")
    else:
        print("The number is not perfect number.")


if __name__ == "__main__":
    main()