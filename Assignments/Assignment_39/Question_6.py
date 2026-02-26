import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score,confusion_matrix,ConfusionMatrixDisplay
import matplotlib.pyplot as plt

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

    # Model Object's
    model_1 = DecisionTreeClassifier(random_state=42,max_depth=1)
    model_3 = DecisionTreeClassifier(random_state=42,max_depth=3)
    model_none = DecisionTreeClassifier(random_state=42,max_depth=None)

    # Model's Training
    trained_model_1 = model_1.fit(X_train,y_train)
    trained_model_3 = model_3.fit(X_train,y_train)
    trained_model_none = model_none.fit(X_train,y_train)

    # Model's Testing
    result1 = trained_model_1.predict(X_test)
    result3 = trained_model_3.predict(X_test)
    result_none = trained_model_none.predict(X_test)

    # Testing Result Evaluation 
    print("The accuracy of the model with max_depth 1 is :",accuracy_score(y_test,result1)*100)
    print("The accuracy of the model with max_depth 3 is :",accuracy_score(y_test,result3)*100)
    print("The accuracy of the model with max_depth none is :",accuracy_score(y_test,result_none)*100)

    '''
    The result of the 3 scenarios in which we are changing the hyper_parameter max_depth is same
    we are consistenly getting 100% accuracy across all the models.
    
    '''


if __name__ == "__main__":
    main()