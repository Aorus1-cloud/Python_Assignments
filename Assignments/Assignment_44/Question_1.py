import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error,r2_score

def main():
    Border = "-"*40

    print(Border)
    print("Step 1: Load the data")
    print(Border)

    dataset = pd.read_csv("Advertising.csv")

    print("Dataset loaded successfully....")
    print(dataset.head())

    print(Border)
    print("Step 2: Clean,Analyze and prepare the data")
    print(Border)

    print("NaN values?:",dataset.notna(),"\n")

    print("Splitting the dataset into training and testing...\n")

    X = dataset[['TV','radio','newspaper']]
    y = dataset['sales']

    print("Feature(Independant variables) :")
    print(X.head(),"\n")

    print("Labels (Dependant Variables):")
    print(y.head(),"\n")

    print("Splitting the dataset into training and testing....\n")

    X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.5)

    print("Shape of X_train:",X_train.shape,"\n")
    print("Shape of X_test:",X_test.shape,"\n")
    print("Shape of y_train:",y_train.shape,"\n")
    print("Shape of y_test:",y_test.shape,"\n")

    print(Border)
    print("Step 3 : Train the model")
    print(Border)

    print("For this case study we choosed Linear Regressin Model.\n")

    model = LinearRegression()

    model.fit(X_train,y_train)

    print("The trained model is:",model,"\n")

    print(Border)
    print("Step 4 : Test the model")
    print(Border)

    result = model.predict(X_test)
    print("Model testing successfull...")

    print(Border)
    print("Step 5 : Output  Of the model")
    print(Border)

    for i,value in enumerate(y_test):
        print(f"Expected Output is {value},Predicted output is {result[i]}")

    print("R2 score is :",r2_score(y_test,result))
    print("Mean Squarred Error is :",mean_squared_error(y_test,result))

if __name__ == "__main__":
    main()