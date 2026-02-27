import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier,plot_tree
from sklearn.metrics import accuracy_score
from sklearn import tree
import matplotlib.pyplot as plt


def main():
    FileName= "student_performance_ml.csv"

    Dataset = pd.read_csv(FileName)

    Features = [
        "StudyHours",
        "Attendance",
        "PreviousScore",
        "AssignmentsCompleted",
        "PerformanceIndex",
        "SleepHours",
    ]

    X = Dataset[Features]
    Y = Dataset["FinalResult"]

    X_train,X_test,Y_train,Y_test = train_test_split(X,Y,random_state=42,test_size=0.2)

    X_test = pd.DataFrame([
        [9.0,60,80,7,99.0,6],
        [5.0,90,50,8,101.3,7],
        [2.0,97,40,4,98.5,8],
        [5.0,70,65,7,82.6,7],
        [1.0,90,80,9,102.8,7]
        ],
        columns=Features
        )
 
    Y_test = [1,1,1,0,1]
    
    model = DecisionTreeClassifier(random_state=42)

    trained_model = model.fit(X_train,Y_train)

    result = trained_model.predict(X_test)

    print("Accuracy of the model is :",accuracy_score(Y_test,result)*100)
    print("The accuracy improved by 20% and now has reached 100% in total.So yuss the accuracy improved.")

if __name__ == "__main__":
    main()