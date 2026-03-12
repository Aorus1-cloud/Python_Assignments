import pandas as pd 
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import numpy as np

def main():
    Border = "-"*40

    print(Border)
    print("Step 1 : Load the dataset")
    print(Border)

    dataset = pd.DataFrame([
        {"Study_Hours":1,"Marks":50},
        {"Study_Hours":2,"Marks":55},
        {"Study_Hours":3,"Marks":60},
        {"Study_Hours":4,"Marks":65},
        {"Study_Hours":5,"Marks":70},
    ])

    print(dataset)

    print(Border)
    print("Step 2 : Analyze,Clean,Prepare the dataset")
    print(Border)

    print("the dataset have one feature and a single label as:")

    print([i for i in dataset.columns])

    X = pd.DataFrame(dataset["Study_Hours"])
    Y = pd.DataFrame(dataset["Marks"])

    print("Seperating the feature and label as:")
    print(X,"\n")
    print(Y,"\n")

    print(Border)
    print("Step 3 : Train the model")
    print(Border)

    print("As the labels are contiguous we are going to use LinearRegression Model")

    model = LinearRegression()

    model.fit(X,Y)

    print("Model is as :",model)
    print("The Coefficient is :",model.coef_)
    print("The intercept is as:",model.intercept_)

    print(Border)
    print("Step 4 : Test the model")
    print(Border)

    result = model.predict([[6]])

    print("The prediction for the input 6 is :",result)

if __name__ == "__main__":
    main()