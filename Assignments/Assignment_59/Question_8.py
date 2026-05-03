from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn.metrics import accuracy_score
from tensorflow.keras.metrics import BinaryAccuracy

def main():
    # Load the data
    X,y = load_breast_cancer(return_X_y=True)

    # EDA 
    print("Independant variables are :\n",X[:5])
    print("Dependant variables are :\n",y[:5])

    print("Shape of independant variables is :",X.shape)
    print("Shape of dependant variable is :",y.shape)

    X_train,X_test,y_train,y_test = train_test_split(X,y,random_state=42,test_size=0.2)

    model = Sequential([
        Dense(8,activation="relu"),
        Dense(4,activation="relu"),
        Dense(1,activation="sigmoid")
    ])

    model.compile(optimizer = "adam",loss="binary_crossentropy",metrics = ['accuracy'])

    model.fit(X_train,y_train,epochs = 500,verbose = 0)

    print("Model trained successfully :",model)

    Result = model.predict(X_test,verbose = 0)

    for y_og,y_pred in zip(y_test,Result):
        print(f"Expected : {y_og} , Predicted : {y_pred}")

    binary = BinaryAccuracy(threshold=0.5)                           # object of BinaryAccuracy class with parameter threshold value

    binary.update_state(y_test,Result)                               # fiting the data

    print("Accuracy of the model is :",binary.result().numpy())      # displaying the output

    binary.reset_state()                                             # Clearing past data for further use

if __name__ == "__main__":
    main()