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
        "SleepHours",
    ]

    X = Dataset[Features]
    Y = Dataset["FinalResult"]

    X_train,X_test,Y_train,Y_test = train_test_split(X,Y,random_state=42,test_size=0.2)

    model = DecisionTreeClassifier(random_state=42)

    trained_model = model.fit(X_train,Y_train)

    tree.plot_tree(trained_model)

    plt.show()

    print("At root node Attendance feature appears.")
    print("This feature was selected because it had a clear range of 75 where all the students above this level were pass and below this were fail so it would be easy to identify based on this feature alone.")
    # result = trained_model.predict(X_test)

if __name__ == "__main__":
    main()