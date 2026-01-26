class Numbers:
    def __init__(self,no):
        self.Value = int(no)

    def ChkPrime(self):
        if self.Value == 1:
            return False
        
        elif self.Value == 2:
            return True
        
        for i in range(2,self.Value):
            if self.Value % i == 0:
                return False 
            
        return True

    def ChkPerfect(self):
        num = []
        res = 0

        # for i in range(1,self.Value):
        #     if self.Value % i == 0:
        #         num.append(i)

        # for number in num:
        #     res = res + number

        res = Numbers.SumFactors(self)      #If we use the instance function from our class
        
        if res == self.Value:
            return True
        
        return False
    
        
    def Factors(self):
        ans = []
        for i in range(1,self.Value):
            if self.Value % i == 0:
                ans.append(i)

        print("All factors are :",ans)

    def SumFactors(self):
        ans = []
        res = 0

        for i in range(1,self.Value):
            if self.Value % i == 0:
                ans.append(i)

        for num in ans :
            res = res + num

        return res


obj1 = Numbers(int(input("Enter a number :")))
print(obj1.ChkPrime())
print(obj1.ChkPerfect())
print(obj1.SumFactors())
obj1.Factors()

obj2 = Numbers(int(input("Enter a number :")))
print(obj2.ChkPrime())
print(obj2.SumFactors())
print(obj2.ChkPerfect())
obj2.Factors()