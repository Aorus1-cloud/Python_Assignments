def EvenNumbers(No):
    res = list()

    for i in range(2,No+1,2):
        res.append(i)

    return res
def main():
    result = 0 
    
    number = int(input("Enter the number : "))
    
    result = EvenNumbers(number)

    print(f"The even number till {number} are : ",result)

if __name__ == "__main__":
    main()