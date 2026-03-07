import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier,plot_tree
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

def main():
    Border = "-"*40

    print(Border)
    print("Step 1 : Load the data")
    print(Border)

    dataset = pd.read_csv("WinePredictor.csv")
    print("Dataset loaded successfully...\n")
    print(dataset.head())

    print(Border)
    print("Step 2 : Clean,Analyze and Manipulate data")
    print(Border)

    print("NaN values :",dataset.isna(),"\n")

    print("Shape of dataset :",dataset.shape)
    print("Splitting the dataset in Independant and dependant variables:\n")
    feature_cols = [
        "Alcohol",
        "Malic acid",
        "Ash",
        "Alcalinity of ash",
        "Magnesium",
        "Total phenols",
        "Flavanoids",
        "Nonflavanoid phenols",
        "Proanthocyanins",
        "Color intensity",
        "Hue",
        "OD280/OD315 of diluted wines",
        "Proline",
        ]
    X = dataset[feature_cols]
    y = dataset['Class']

    print("Independant Variables :\n",X.head())
    print("Dependant Variables :\n",y.head())

    print("Splitting the dataset in training and splitting...\n")
    X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42)

    print("Shape of X_train:",X_train.shape)
    print("Shape of X_test:",X_test.shape)
    print("Shape of y_train:",y_train.shape)
    print("Shape of y_test:",y_test.shape)

    print(Border)
    print("Step 3 : Training the model ")
    print(Border)

    print("For this case study we will choose DecisionTreeClassifier as we have dependant variable categorical")

    model = DecisionTreeClassifier(random_state=42)

    model.fit(X_train,y_train)

    print("Model trained successfully :",model,"\n")
    print("The Decision tree of is as :")

    plot_tree(model,feature_names=feature_cols,filled=True,class_names=y.unique().astype(dtype=str))
    plt.show()

    print(Border)
    print("Step 4 : Test the model ")
    print(Border)

    result = model.predict(X_test)

    print("Model tested successsfully:")
    print(result[:5])

    print(Border)
    print("Step 5 : Accuracy Of model ")
    print(Border)

    for i,value in enumerate(y_test):
        print(f"Expected output is {value},Predicted Output is {result[i]}")

    print("\nThe accuracy of the model is :",accuracy_score(y_test,result))

if __name__ == "__main__":
    main()