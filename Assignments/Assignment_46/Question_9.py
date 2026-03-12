import pandas as pd
from sklearn.linear_model import LinearRegression

def main():
    Border = "-"*40

    print(Border)
    print("Step 1 : Load the dataset")
    print(Border)

    dataset = pd.DataFrame([
        {"Study_Hours":1,"Sleep_Hours":7,"Marks":50},
        {"Study_Hours":2,"Sleep_Hours":6,"Marks":55},
        {"Study_Hours":3,"Sleep_Hours":7,"Marks":60},
        {"Study_Hours":4,"Sleep_Hours":6,"Marks":65},
        {"Study_Hours":5,"Sleep_Hours":8,"Marks":70},
    ])

    print(dataset)

    print(Border)
    print("Step 2 : Analyze,Clean,Prepare the dataset")
    print(Border)

    print("the dataset have two features and a single label as:")

    print([i for i in dataset.columns])

    X = pd.DataFrame(dataset[["Study_Hours","Sleep_Hours"]])
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

    print("Model is trained successfully :",model)
    print("The Coefficient is :",model.coef_)
    print("The intercept is as:",model.intercept_)

if __name__ == "__main__":
    main()