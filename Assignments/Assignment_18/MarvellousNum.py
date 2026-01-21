from math import sqrt
def ChkPrime(No):
    if No == 1:
        return False
    
    if No == 2 :
        return True
    
    for i in range(2,int(sqrt(No))+1):  
        if No % i == 0 :
            return False
    
    return True