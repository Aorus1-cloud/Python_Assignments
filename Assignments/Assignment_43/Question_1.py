import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

def Accuracy(Y_test,Y_pred):
    accuracy = 0
    for i,value in enumerate(Y_test):
        if value == Y_pred[i]:
            accuracy+=1

    accuracy = accuracy / len(Y_test)

    return accuracy

def main():
    Border = "-"*40
    print(Border+"\n")
    print("--------- Play Predictor Model ---------\n")
    print(Border+"\n")

    print(Border+"\n")
    print("--------- Step 1: Loading Data ---------\n")
    print(Border+"\n")

    dataset = pd.read_csv("MarvellousInfosystems_PlayPredictor.csv")

    print("Dataset Loaded Successfully....")
    print(dataset.head(),"\n")

    print(Border+"\n")
    print("-------- Step 2: Preparing Data --------\n")
    print(Border+"\n")

    print("Using Label Encoder to encode the categorical data into numbers.")
    print("Data before encodin :")
    print(dataset.head(),"\n")

    encoder = LabelEncoder()

    X = dataset[['Weather','Temperature']].apply(encoder.fit_transform)
    y = dataset['Play']

    print("Encode Dataset is as :")
    print(X.head(),"\n")

    X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.5)

    print(Border+"\n")
    print("-------- Step 3: Training Model --------\n")
    print(Border+"\n")

    print("We are going to use KNearestNeighbour for this case study\n")

    model1 = KNeighborsClassifier(n_neighbors=1)
    model3 = KNeighborsClassifier(n_neighbors=3)
    model5 = KNeighborsClassifier(n_neighbors=5)


    model1.fit(X_train,y_train)
    model3.fit(X_train,y_train)
    model5.fit(X_train,y_train)

    print("Trained model is :",model1,"\n")
    print("Trained model is :",model3,"\n")
    print("Trained model is :",model5,"\n")


    print(Border+"\n")
    print("-------- Step 4: Testing Model --------\n")
    print(Border+"\n")

    y_pred1 = model1.predict(X_test)
    y_pred3 = model3.predict(X_test)
    y_pred5 = model5.predict(X_test)


    print("Predicted output of model(k=1) is :\n",y_pred1)
    print("Predicted output of model(k=3) is :\n",y_pred3)
    print("Predicted output of model(k=5) is :\n",y_pred5)

    print(Border+"\n")
    print("------- Step 5: Accuracy of model ------\n")
    print(Border+"\n")
     
    print("The accuracy of our model(k=1) is :",Accuracy(y_test,y_pred1)*100)
    print("The accuracy of our model(k=3) is :",Accuracy(y_test,y_pred3)*100)
    print("The accuracy of our model(k=5) is :",Accuracy(y_test,y_pred5)*100)

if __name__ == "__main__":
    main()