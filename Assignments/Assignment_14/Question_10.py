greater = lambda x,y,z : x if x > y and x > z else (y if y > z else z)

def main():
    result = 0 

    num1 = int(input("Enter first number :"))
    num2 = int(input("Enter second number :"))
    num3 = int(input("Enter third number :"))
 
    result = greater(x=num1,y=num2,z=num3)

    print(f"{result} is greatest amongs the three ")

if __name__ == "__main__":
    main()