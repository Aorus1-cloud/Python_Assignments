def vow_or_con(Char):
    vowels = ["a","e","i","o","u"]

    for vow in vowels:
        if vow == Char.lower():
            return True
        
    return False


def main():
    result = False 

    character = str(input("Enter the character :"))

    result = vow_or_con(character)

    if result:
        print("The character is Vowel")
    else:
        print("The character is Consonent")

if __name__ == "__main__":  
    main()