import threading
from math import sqrt
def prime_no(arr):
    result = []

    for num in arr:
        if ChkPrime(num):
            result.append(num)

    print("The prime numbers from the list are :",result)
    
def ChkPrime(Num):

    if Num == 1:
        return False
    
    if Num == 2:
        return True
    
    for i in range(2,int(sqrt(Num)+1)):
        if Num % i == 0:
            return False
        
    return True

def non_prime_no(arr):
    result = []

    for num in arr:
        if ChkPrime(num) == False:
            result.append(num)

    print("The non prime numbers from the list are :",result)

def main():
    data = []
    elements = 0 

    elements = int(input("Enter number of inputs :"))

    print("Enter elements :")
    for i in range(elements):
        data.append(int(input()))

    Prime = threading.Thread(target=prime_no,args=(data,))
    NonPrime = threading.Thread(target=non_prime_no,args=(data,))

    Prime.start()
    NonPrime.start()

    Prime.join()
    NonPrime.join()

if __name__ == "__main__":
    main()

