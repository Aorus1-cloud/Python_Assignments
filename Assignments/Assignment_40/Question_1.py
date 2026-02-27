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

    model = DecisionTreeClassifier()

    trained_model = model.fit(X_train,Y_train)

    result = trained_model.predict(X_test)

    print("The accuracy of this model is :",accuracy_score(Y_test,result)*100)

    print("The importance of the features is :")
    feature_importance = trained_model.feature_importances_
    print(feature_importance)

    important_feature_index = 0

    for i,feature in enumerate(feature_importance):
        if feature == 1:
            important_feature_index = i

    print(f"From the importance score i get to know that the {Features[important_feature_index]} contributes more than the else.")
    print("And all the others contributes the least.")

if __name__ == "__main__":
    main()