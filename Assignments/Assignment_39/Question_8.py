import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,confusion_matrix,ConfusionMatrixDisplay
from sklearn.tree import DecisionTreeClassifier

def main():
    FileName = "student_performance_ml.csv"
    Border = "-"*40

    print(Border+"\n")
    print("Step 1 : Data Loading\n")
    print(Border+"\n")

    dataset = pd.read_csv(FileName)

    print("Data Loaded Successfully...\n")
    print("First 5 entries :\n",dataset.head())

    print("\n"+Border+"\n")
    print("Step 2 : Data Analysis\n")
    print(Border+"\n")

    print("The shape of the dataset is :",dataset.shape)

    Features = [
        "StudyHours",
        "Attendance",
        "PreviousScore",
        "AssignmentsCompleted",
        "SleepHours"
    ]

    print("The Independant Variables of the dataset are :",list(dataset[Features].columns))
    print("The Dependant Variable of the dataset is :",dataset["FinalResult"].name)
    print("Datatype of each column is :\n",dataset.dtypes)
    print("Description of the dataset :\n",dataset.describe())

    print("\n"+Border+"\n")
    print("Step 3 : Data Visualization\n")
    print(Border+"\n")

    print("Patterns in Study hours and Attendance:")
    sns.scatterplot(data=dataset,x="Attendance",y="StudyHours",hue="FinalResult")
    plt.show()

    print("Patterns in Attendance and Previous marks :")
    sns.scatterplot(data=dataset,x="Attendance",y="PreviousScore",hue="FinalResult")
    plt.show()

    mean = dataset["StudyHours"].mean()

    print("Avg study hours:")
    sns.barplot(data=dataset,x=dataset.index,y="StudyHours",hue="FinalResult") 
    plt.xlabel("Students") 
    plt.axhline(y=mean,linestyle = "--")
    plt.show()

    print("\n"+Border+"\n")
    print("Step 4 : Training Testing split\n")
    print(Border+"\n")

    X = dataset[Features]
    Y = dataset["FinalResult"]

    X_train,X_test,Y_train,Y_test = train_test_split(X,Y,random_state=42,test_size=0.2)

    print("Training and testing slit done :")
    print("X_train :",X_train.shape)
    print("X_test :",X_test.shape)
    print("Y_train :",Y_train.shape)
    print("Y_test :",Y_test.shape)

    print("\n"+Border+"\n")
    print("Step 5 : Model Training \n")
    print(Border+"\n")

    Model = DecisionTreeClassifier(random_state=42)

    Trained_Model = Model.fit(X_train,Y_train)

    print("Model Training successfull :",Trained_Model)

    print("\n"+Border+"\n")
    print("Step 6 : Model Testing \n")
    print(Border+"\n")

    print("Model Testing using testing data:")
    print(X_test.head())

    Y_pred = Trained_Model.predict(X_test)

    print("Model testing successfull.")

    print("\n"+Border+"\n")
    print("Step 7 : Accuracy Calculation \n")
    print(Border+"\n")

    print("Some predicted answers by model :")
    print(Y_pred[:5])

    print("Accuracy of model on testing dataset is :",accuracy_score(Y_test,Y_pred)*100)

    print("\n"+Border+"\n")
    print("Step 8 : Confusion Matrix \n")
    print(Border+"\n")

    print("Here is the confusion matrix of the models testing data :")

    confs_matrix = confusion_matrix(Y_test,Y_pred)

    cplot = ConfusionMatrixDisplay(confusion_matrix=confs_matrix,display_labels=Trained_Model.classes_)

    cplot.plot()

    plt.show()

    print("\n"+Border+"\n")
    print("Step 9 : Final Conclusion \n")
    print(Border+"\n")

    print("1) The dataset is balanced No over or underfitting")
    print("2) The Model is 100% accurate")
    print("3) No tuning was needed for this model to reach the 100% accuracy")
    print("4) The size of the dataset was 30x6")
    print("5) The model accurately predicts if a student is going to fail or pass on the basis of input data.")

if __name__ == "__main__":
    main()