import threading

def Even_sum(No):
    data = []
    sum = 0
    for i in range(1,No):
        if No % i == 0 and i % 2 == 0:
            data.append(i)
        
    for num in data:
        sum = sum + int(num)
    
    print(f"The sum of even factors of {No} is : {sum}")


def Odd_sum(No):
    data = []
    sum = 0

    for i in range(1,No):
        if No % i == 0 and i % 2 != 0: 
            data.append(i)

    for num in data:
        sum = sum + num
    
    print(f"The sum of odd factors of {No} is : {sum}")

    
def main():
    num = int(input("Enter a number :"))

    EvenFactor = threading.Thread(target=Even_sum,args=[num,])
    OddFactor = threading.Thread(target=Odd_sum,args=[num,])

    EvenFactor.start()
    OddFactor.start()

    EvenFactor.join()
    OddFactor.join()

    print("Exit from main")

if __name__ == "__main__":
    main()