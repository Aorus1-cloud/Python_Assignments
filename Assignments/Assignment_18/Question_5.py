from MarvellousNum import ChkPrime

def ListPrime(No):
    Res = []

    for i in range(len(No)):
        prime = False

        prime = ChkPrime(No[i])

        if prime:
            Res.append(No[i])
            
    return Res

def Add_list(arr):
    sum = 0 

    for num in arr:
        sum = sum + num
    
    return sum


def main():
    result = 0
    data = []

    elements = int(input("Enter Number of elements :"))
    for i in range(elements):
        data.append(int(input()))

    data = ListPrime(data)

    result = Add_list(data)

    print("The addition of the prime from the given number is :",result)
    

if __name__ == "__main__":
    main()