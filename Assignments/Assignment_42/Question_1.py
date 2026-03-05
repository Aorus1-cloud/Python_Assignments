import pandas as pd 

class LinearRegression2dX:
    def __init__(self,return_temp = False):
        self.return_temp = return_temp

    def fit(self,X,y):
        self.X_mean = X.mean()
        self.y_mean = y.mean()

        numerator = 0
        denominator = 0

        for i in range(len(X)):
            numerator = numerator + ((X[i] - self.X_mean) * (y[i] - self.y_mean))
            denominator = denominator + ((X[i] - self.X_mean)**2)
        
        self.m = numerator / denominator 

        self.C =  self.y_mean - (self.X_mean * self.m)

    def predict(self,X_test):

        if type(X_test) != int:
            result = []
            for i in range(len(X_test)):
                Y_pred = (self.m * X_test[i]) + self.C
                result.append(Y_pred)

        else:
            result = 0
            Y_pred = (self.m * X_test) + self.C
            result = Y_pred

        if self.return_temp == True:
            return self.X_mean,self.y_mean,self.m,self.C,result
        
        else:
            return result

def main():
    X = pd.Series([1,2,3,4,5])
    y = pd.Series([3,4,2,4,5])

    model = LinearRegression2dX(return_temp=True)

    model.fit(X,y)

    X_mean,Y_mean,m,C,res = model.predict(6)

    print("Mean of X is :",X_mean)
    print("Mean of Y is :",Y_mean)

    print("Slope :",m)
    print("Intercept :",C)

    print("Regression Equation :")
    print(f"Y = {m}X + {C}")

    print(f"The predicted output is : {res:.2f}")
    
if __name__ == "__main__":
    main()