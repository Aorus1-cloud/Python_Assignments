def areaC(Rad):
    PI = 3.14159
    result = 0

    result = PI * (Rad ** 2)

    return result

def main():
    Res = 0

    num = int(input("Enter the radius :"))

    Res = areaC(num)

    print("The area of the circle is :",Res,"square units")

if __name__ == "__main__":
    main()