import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

def Incorrect_Prediction(Y_test,Y_pred):
    if len(Y_test) != len(Y_pred):
        return ("Test size and Prediction result size don't match.")
    
    incorrect_pred = []
    
    for i in range(len(Y_test)):
        if Y_test[i] != Y_pred[i]:
            incorrect_pred.append(i)

    return incorrect_pred

def multiple_random_state(random):
    print("-"*40)
    print(f"Output of random_state {random} is:")
    print("-"*40)


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

    X_train,X_test,Y_train,Y_test = train_test_split(X,Y,random_state=random,test_size=0.2)


    X_test = pd.DataFrame(
        [
        [9.0,60,80,7,6],
        [5.0,90,50,8,7],
        [2.0,97,40,4,8],
        [5.0,70,65,7,7],
        [1.0,90,80,9,7],
        ],
        columns=Features
    )

    Y_test = [1,1,1,0,1]
    
    model = DecisionTreeClassifier(random_state=random) 

    trained_model = model.fit(X_train,Y_train)

    result = trained_model.predict(X_test)

    Wrong_Pred = Incorrect_Prediction(Y_test,result)
    print("The important feature is :",trained_model.feature_importances_)
    print("The Predicted output is :",result)
    print("The expected output is :",Y_test)

    for i in Wrong_Pred:
        print("The incorrect guessed students is :",X_test.iloc[i])

    print(f"{len(Wrong_Pred)} students were classified incorrectly.")

    print("The accuracy of the model is :",accuracy_score(Y_test,result),"\n")
    print("-"*40)
    print(f"End of Model Info with random state {random} ends")
    print("-"*40,"\n")

def main():
    random_States = [0,10,42]
    for i in random_States:
        print(f"The model info of random state {i} is :")
        multiple_random_state(i)

if __name__ == "__main__":
    main()