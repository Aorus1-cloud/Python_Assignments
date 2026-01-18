def calculator(No1,No2):
    return No1 + No2, No1 - No2 , No1 * No2 ,No1 / No2

def main():
    add = 0
    sub = 0 
    mult = 0
    div = 0

    num1 = int(input("Enter the Number 1 :"))
    num2 = int(input("Enter the Number 2 :"))

    add, sub, mult, div = calculator(No1=num1,No2=num2)

    print(f"Addition = {add} ,Substraction = {sub},Multiplication = {mult},Division = {div}")

if __name__ == "__main__":
    main()