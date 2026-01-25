import gc

class Arithmetic:
    def __init__(self):
        self.Value1 = 0
        self.Value2 = 0
    
    def Accept(self):
        self.Value1 = int(input("Enter first number :"))
        self.Value2 = int(input("Enter second number :"))

    def Addition(self):
        return self.Value1 + self.Value2
    
    def Substraction(self):
        return self.Value1 - self.Value2
    
    def Multiplication(self):
        return self.Value1 * self.Value2
    
    def Division(self):
        try: 
            return self.Value1 / self.Value2
        
        except ZeroDivisionError as zobj:
            print("Error Occured :",zobj)
        
        

obj1 = Arithmetic()
obj1.Accept()
print("Addition is :",obj1.Addition())
print("substraction is :",obj1.Substraction())
print("Multiplication is :",obj1.Multiplication())
print("Division is :",obj1.Division())

obj2 = Arithmetic()
obj2.Accept()
print("Addition is :",obj2.Addition())
print("substraction is :",obj2.Substraction())
print("Multiplication is :",obj2.Multiplication())
print("Division is :",obj2.Division())

del obj1
del obj2

gc.collect()