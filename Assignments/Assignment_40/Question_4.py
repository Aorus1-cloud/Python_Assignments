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
        "PreviousScore",
        "AssignmentsCompleted",
        "SleepHours"
    ]

    X = Dataset[Features]
    Y = Dataset["FinalResult"]

    X_train,X_test,Y_train,Y_test = train_test_split(X,Y,random_state=42,test_size=0.2)


    X_test = pd.DataFrame([
        [9.0,60,80,7,6],
        [5.0,90,50,8,7],
        [2.0,97,40,4,8],
        [5.0,70,65,7,7],
        [1.0,90,80,9,7]
        ],
        columns=Features
        )
 
    Y_test = [1,1,1,0,1]
    
    model = DecisionTreeClassifier(random_state=42)

    trained_model = model.fit(X_train,Y_train)

    result = trained_model.predict(X_test)

    for i,res in enumerate(result):
        if res :
            print(f"Predicted Output is Pass and Expected ouput is {Y_test[i]}.")
        else:
            print(f"Predicted Ouptut is Fail and Expected output is {Y_test[i]}")

    print("The feature importance is :",trained_model.feature_importances_)
    print("The accuracy of this model is :",accuracy_score(Y_test,result)*100)
    print("I ran multiple test without setting a random_state during that stage the feature importance were changing and i got 100% accuracy when the feature importance was given to attendance and for the other it kept being in range of 20 to 60 from this i get to know that the outcome of my model depends on the feature importance.")

if __name__ == "__main__":
    main()