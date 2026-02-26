import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

def main():
    # Data file : CSV 
    FileName = "student_performance_ml.csv"

    # Data Loading Using Pandas
    Dataset = pd.read_csv(FileName)

    Features = [
        "StudyHours",
        "Attendance",
        "PreviousScore",
        "AssignmentsCompleted",
        "SleepHours"
    ]

    # Independant And Dependant Variable Seperation
    X = Dataset[Features]
    y = Dataset["FinalResult"]

    # Training and testing split (80:20)
    X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42)

    # Model Object 
    model = DecisionTreeClassifier(random_state=42)

    # Training 
    trained_model = model.fit(X_train,y_train)

if __name__ == "__main__":
    main()