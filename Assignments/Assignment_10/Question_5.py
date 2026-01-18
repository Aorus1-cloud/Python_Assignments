def OddNumber(No):
    res = list()

    for i in range(1,No+1,2):
        res.append(i)

    return res
def main():
    result = 0 
    
    number = int(input("Enter the number : "))
    
    result = OddNumber(number)

    print(f"The odd number till {number} are : ",result)

if __name__ == "__main__":
    main()