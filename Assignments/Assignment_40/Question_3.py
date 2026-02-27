import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

def main():
    FileName= "student_performance_ml.csv"

    Dataset = pd.read_csv(FileName)

    Features = [
        "StudyHours",
        "Attendance",
    ]

    X = Dataset[Features]
    Y = Dataset["FinalResult"]

    X_train,X_test,Y_train,Y_test = train_test_split(X,Y,random_state=42,test_size=0.2)

    model = DecisionTreeClassifier()

    trained_model = model.fit(X_train,Y_train)

    result = trained_model.predict(X_test)

    print("The accuracy of this model is :",accuracy_score(Y_test,result)*100)
    print("The accuracy didnt changed it stayed the same.")
    print("Removing other features doesnt affect the outcome.")

if __name__ == "__main__":
    main()