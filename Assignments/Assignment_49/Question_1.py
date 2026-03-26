import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report,ConfusionMatrixDisplay

import seaborn as sns
import matplotlib.pyplot as plt

#----------------------------------------------------------
# Step 1 : Load the dataset
#----------------------------------------------------------
def main():
    DisplayInfo("Step 1 : Load the dataset")
    dataset = pd.read_csv("diabetes.csv")

    print("Data Loaded Successfully")
    print("First few entries:")
    print(dataset.head(),"\n")

    EDA_diabetes(dataset)
    X,Y = DataPreprocessingDiabetes(dataset)

    Model_Training_Testing_Evaluating(X,Y)

#----------------------------------------------------------
# Step 2 : EDA
#----------------------------------------------------------
def DisplayInfo(title):
    border = "-"*50

    print(border)
    print(title)
    print(border+"\n")


def EDA_diabetes(dataset):
    DisplayInfo("Step 2 : Exploratory Data Analysis ")
    print("Shape of the dataset is :",dataset.shape)

    print("All column names of the dataset:\n",dataset.columns,"\n")

    print("Null Values in the dataset :\n",dataset.isnull().sum(),"\n")
    dataset.dropna(inplace = True)      # If any then the column will be removed

    print("Description of the dataset:\n",dataset.describe(),"\n")

    print("Seperating the independant and dependant variables :")
    X = dataset.drop("Outcome",axis = 1)
    y = dataset["Outcome"]

    print("Few entries of the Independant Variables :\n",X.head(),"\n")
    print("Few entries of the dependant variables :\n",y.head(),"\n")

    print("Shape of independant variables :",X.shape)
    print("Shape of dependant variable :",y.shape)

    print("The distribution of the target Variable :")
    sns.countplot(data=dataset,x ="Outcome",fill=True)
    plt.show()

    print("As we can see from the target variable distribution that it is not correctly distributed therefore we will need to use stratify to provide correct number of sample for training and testing.")

    # print("Plotting Boxplot to check if any outliers in the dataset:\n")
    # for column in dataset.columns:
    #     sns.boxplot(dataset,x=column,hue="Outcome")
    #     plt.show()

    # print("Plotting Boxplot to check if any outliers in the dataset:\n")
    # for column in dataset.columns:
    #     sns.histplot(dataset,x=column,hue="Outcome")
    #     plt.show()

    print("Heatmap:\n")
    plt.figure(figsize=(15,15))
    sns.heatmap(dataset.corr(),cmap='coolwarm')
    plt.show()

#----------------------------------------------------------
# Step 3 : Data Preprocessing
#----------------------------------------------------------

def DataPreprocessingDiabetes(dataset):

    DisplayInfo("Step 3 : Data preprocessing")

    print("Zero values in the independant varibles :\n")

    X = dataset.drop("Outcome",axis=1)
    for col in X.columns:
        print("Column Name :",col)
        print((dataset[col]==0).sum(),"\n")

    print("From the above output we can see that some columns have 0 values which are biologically not possible therefore we need to handle them by putting median by outcome group accordingly")

    cols = [
        "Glucose",
        "BloodPressure",
        "SkinThickness",
        "Insulin",
        "BMI"
    ]

    for col in cols:
        col_outcome_1 = dataset[dataset["Outcome"] == 1][col]

        col_outcome_0 = dataset[dataset["Outcome"] == 0][col]

        mean_1 = col_outcome_1.mean()
        mean_0 = col_outcome_0.mean()

        if type(mean_1) or type(mean_0) == np.float64:
            dataset = dataset.astype(float)

        dataset.loc[(dataset[col]==0) & (dataset["Outcome"]==1),col] = mean_1
        dataset.loc[(dataset[col]==0) & (dataset["Outcome"]==0),col] = mean_0

    print("\n0 values after preprocessing :\n")

    for col in X.columns:
        print("Column Name :",col)
        print((dataset[col]==0).sum(),"\n")

    X = dataset.drop("Outcome",axis = 1)
    y = dataset["Outcome"]

    print("Values before scaling:\n")
    print(X.head())

    scaler = StandardScaler()
    X = pd.DataFrame(scaler.fit_transform(X),columns=X.columns)

    print("Values after scaling:\n")
    print(X.head())

    return X,y

#----------------------------------------------------------
# Step 4 : Model Building
#----------------------------------------------------------
def Model_Training_Testing_Evaluating(X,y):
    DisplayInfo("Step 4 : Models Building")

    model_dt = DecisionTreeClassifier()
    model_lr = LogisticRegression()
    model_knn = KNeighborsClassifier()
    print("Trained Models are :")
    print("Model 1 :",model_dt)
    print("Model 2 :",model_knn)
    print("Model 3 :",model_lr,"\n")

    X_train,X_test,Y_train,Y_test = train_test_split(X,y,test_size=0.2,stratify=y,random_state=42)

    model_dt = model_dt.fit(X_train,Y_train)
    model_lr = model_lr.fit(X_train,Y_train)
    model_knn = model_knn.fit(X_train,Y_train)

    result_dt = model_dt.predict(X_test)
    result_lr = model_lr.predict(X_test)
    result_knn = model_knn.predict(X_test)

    DisplayInfo("Step 5 : Models Evaluation")

    print("Accuracy Scores :\n")
    print("Accuracy of Decision Tree :",accuracy_score(Y_test,result_dt)*100)
    print("Accuracy of Logistic Regression :",accuracy_score(Y_test,result_lr)*100)
    print("Accuracy of KNN :",accuracy_score(Y_test,result_knn)*100,"\n")

    print("Confusion Matrix :\n")
    cm_dt = confusion_matrix(Y_test,result_dt)
    cm_lr = confusion_matrix(Y_test,result_lr)
    cm_knn = confusion_matrix(Y_test,result_knn)

    cmd_dt = ConfusionMatrixDisplay(confusion_matrix=cm_dt)
    cmd_dt.plot()
    plt.title("Decision Tree Confusion Matrix")
    plt.show()

    cmd_lr = ConfusionMatrixDisplay(confusion_matrix=cm_lr)
    cmd_lr.plot()
    plt.title("Logistic Regression Confusion Matrix")
    plt.show()

    cmd_knn = ConfusionMatrixDisplay(confusion_matrix=cm_knn)
    cmd_knn.plot()
    plt.title("KNN Confusion Matrix")
    plt.show()

    print("\nClassification Reports of every Model:\n")
    print("Decision Tree Classification Report :\n",classification_report(Y_test,result_dt))
    print("Logistic Regression Classification Report :\n",classification_report(Y_test,result_lr))
    print("KNN Classification Report :\n",classification_report(Y_test,result_knn))

    DisplayInfo("Step 6 : Final Prediction ")

    result = model_dt.predict(X_test)

    for i,opt in enumerate(Y_test):
        print(f"Expected Result = {opt},Predicted Output = {result[i]}")
        
    final = pd.DataFrame(zip(Y_test,result),columns=["Expected","Predicted"])
    final.to_csv("Final.csv",index=False)

if __name__ == "__main__":
    main()