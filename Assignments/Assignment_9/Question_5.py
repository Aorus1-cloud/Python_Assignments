def Divisible(Num):
    if Num % 5 == 0 and Num % 3 == 0:
        return True
    else:
        return False
    

def main():
    Result = False
    Result = Divisible(30)
    if Result == True :
        print("It is Divisible By Both.")
    else :
        print("The Number isn't divisible by Both.")

if __name__ == "__main__":
    main()