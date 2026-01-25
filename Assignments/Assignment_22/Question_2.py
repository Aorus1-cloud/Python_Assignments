import gc

class Circle:
    Pi = 3.14

    def __init__(self):
        self.radius = 0
        self.area = 0
        self.circumference = 0

    def Accept(self):
        self.radius = int(input("Enter the radius :"))

    def CalculateArea(self):
        result = 0

        result = Circle.Pi * (self.radius ** 2) 

        self.area = result
    
    def CalculateCircumference(self):
        result = 0

        result = 2 * Circle.Pi * self.radius

        self.circumference = result

    def Display(self):
        print("The radius is :",self.radius)

        print("The area of circle is :",self.area)

        print(f"The circumference of circle is : {self.circumference :.3f}",)

obj1 = Circle()
obj2 = Circle()
obj3 = Circle()

obj1.Accept()
obj1.CalculateArea()
obj1.CalculateCircumference()
obj1.Display() 

obj2.Accept()
obj2.CalculateArea()
obj2.CalculateCircumference()
obj2.Display()

obj3.Accept()
obj3.CalculateArea()
obj3.CalculateCircumference()
obj3.Display()
        
del obj1
del obj2
del obj3

# for i in range(3):       
#     print(i)
#     obj = Circle()
#     obj.Accept()
#     obj.CalculateArea()
#     obj.CalculateCircumference()
#     obj.Display()

#     del obj

gc.collect()
