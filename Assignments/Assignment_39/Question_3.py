import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
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

    # Testing 
    result = trained_model.predict(X_test)

    # Expected and Predicted Output
    for i,value in enumerate(result):
        print(f"Predicted Output is : {value} and Expected output is : {y_test.iloc[i]}")

    # Accuracy Score 
    accuracy = accuracy_score(y_test,result)

    print(f"The accuracy of model is : {accuracy*100} %")
    
        
if __name__ == "__main__":
    main()