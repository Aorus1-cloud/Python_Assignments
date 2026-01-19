def grade(No):

    if No>=75:
        return "Distinction"
    elif No>=60:
        return "First"
    elif No>=50:
        return "Second"
    else:
        return "Fail"


def main():
    Res = str()

    num = int(input("Enter your marks :"))

    Res = grade(num)

    if Res == "Fail":
        print("You have failed !!!")
    else:
        print("You have passed with",Res,"class !!!")

if __name__ == "__main__":
    main()