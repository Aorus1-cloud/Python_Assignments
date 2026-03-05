from Question_1 import LinearRegression2dX
import pandas as pd 
import matplotlib.pyplot as plt

def main():
    model = LinearRegression2dX()

    X = pd.Series([1,2,3,4,5])
    y = pd.Series([20000,25000,30000,35000,40000])

    model.fit(X=X,y=y)

    years = int(input("Enter the experience years to find salary :"))

    res = model.predict(years)

    print(f"Predicted salary after {years} is : {res}")

    plt.scatter(X,y,marker='o',color='r',label = "Data Points")
    plt.plot(X,y,color='g',label="Regression Line")
    plt.legend()
    plt.xlabel("Salary ->")
    plt.ylabel("Experience ->")
    plt.show()


if __name__ == "__main__":
    main()