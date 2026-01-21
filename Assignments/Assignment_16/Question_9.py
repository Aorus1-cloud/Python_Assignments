def even_10():
    even_no = []
    i = 2 
    
    while (len(even_no) <= 10):
        if (i % 2 == 0):
            even_no.append(i)
        i = i + 1 
        
    return even_no

def main():
    result = [] 
    
    result = even_10()

    for i in range(len(result)):
        print(result[i],end="")

if __name__ == "__main__":
    main()
