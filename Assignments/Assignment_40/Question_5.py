import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

def accuracyX(Y_test,Y_pred):
    if len(Y_test) != len(Y_pred):
        return ("Test size and Prediction result size don't match.")
    
    correct_pred = 0
    total_pred = len(Y_test)
    
    for i in range(len(Y_test)):
        if Y_test[i] == Y_pred[i]:
            correct_pred = correct_pred + 1
    
    acc = correct_pred/total_pred

    return acc

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

    print("The accuracy of the model is (accuracyX):",accuracyX(Y_test,result)*100)
    print("The accuracy of the model is (accuracy_score):",accuracy_score(Y_test,result)*100)

if __name__ == "__main__":
    main()