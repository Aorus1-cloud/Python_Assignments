import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler,OneHotEncoder
from sklearn.metrics import accuracy_score,roc_auc_score,confusion_matrix,ConfusionMatrixDisplay,classification_report,roc_curve,auc
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.compose import ColumnTransformer

import matplotlib.pyplot as plt
import seaborn as sns

#----------------------------------------------------------
# Step 1 : Load the dataset
#----------------------------------------------------------
def DisplayInfo(title):
    border = "="*50
    print(border)
    print(title)
    print(border+"\n")

def main():
    DisplayInfo("Step 1 : Load the dataset")

    dataset = pd.read_csv("bank-full.csv")
    print("Dataset loaded Successfully.\n")
    print("First few entries from the dataset :\n")
    print(dataset.head(),"\n")

    X,Y = EDA_bank_marketing(dataset)

    Model_Training_Testing_Evaluatin(X,Y)

#----------------------------------------------------------
# Step 2 : EDA of Dataset
#----------------------------------------------------------
def EDA_bank_marketing(dataset):
    DisplayInfo("Step 2 : EDA of the dataset")
    print("Shape of Dataset :",dataset.shape,"\n")
    print("Columns in Dataset :\n",dataset.columns,"\n")
    print("Null Values :\n",dataset.isnull().sum())
    print("NaN values :\n",dataset.isna().sum())
    print("Description of the dataset:\n",dataset.describe(),"\n")

    print("The distribution of the target Variable :")
    sns.countplot(data=dataset,x ="y",fill=True)
    plt.show()

    # print("Heatmap:\n")
    # plt.figure(figsize=(15,15))
    # sns.heatmap(dataset.corr(),cmap='coolwarm')
    # plt.show()
    
    
    print("Dataset before cleaning:\n")
    print(dataset.head())

    # Columns cleaning
    if "age" in dataset.columns:
        DisplayInfo("Age Column")
        unknown_values_age = (dataset["age"] == "unknown").sum()
        print("Unknown values in age :",unknown_values_age,"\n")


    if "job" in dataset.columns:
        DisplayInfo("Job Column")
        unknown_values_job = (dataset["job"] == "unknown").sum()
        print("Unknown values in job before preprocessing :",unknown_values_job)

        mode_job_yes = dataset[dataset["y"] == "yes"]["job"].mode().iloc[0]
        mode_job_no = dataset[dataset["y"] == "no"]["job"].mode().iloc[0]

        dataset.loc[((dataset["job"] == "unknown") & (dataset["y"] == "yes")),"job"] = mode_job_yes
        dataset.loc[((dataset["job"] == "unknown") & (dataset["y"] == "no")),"job"] = mode_job_no

        unknown_values_job = (dataset["job"] == "unknown").sum()
        print("Unknown values in job after preprocessing:",unknown_values_job,"\n")

    if "marital" in dataset.columns:
        DisplayInfo("Marital Column")
        unknown_values_marital = (dataset["marital"] == "unknown").sum()
        print("Unknown values in marital :",unknown_values_marital,"\n")

    if "education" in dataset.columns:
        DisplayInfo("Education Column")
        unknown_values_education = (dataset["education"] == "unknown").sum()
        print("Unknown values in education before preprocessing :",unknown_values_education)

        mode_education_yes = dataset[dataset["y"] == "yes"]["education"].mode().iloc[0]
        mode_education_no = dataset[dataset["y"] == "no"]["education"].mode().iloc[0]

        dataset.loc[((dataset["education"] == "unknown") & (dataset["y"] == "yes")),"education"] = mode_education_yes
        dataset.loc[((dataset["education"] == "unknown") & (dataset["y"] == "no")),"education"] = mode_education_no

        unknown_values_education = (dataset["education"] == "unknown").sum()
        print("Unknown values in education after preprocessing:",unknown_values_education,"\n")

    if "default" in dataset.columns:
        DisplayInfo("Default Column")
        unknown_values_default = (dataset["default"] == "unknown").sum()
        print("Unknown values in default  :",unknown_values_default,"\n")

    if "balance" in dataset.columns:
        DisplayInfo("Balance Column")
        unknown_values_balance = (dataset["balance"] == "unknown").sum()
        print("Unknown values in balance :",unknown_values_balance,"\n")
    
    if "housing" in dataset.columns:
        DisplayInfo("Housing Column")
        unknown_values_housing = (dataset["housing"] == "unknown").sum()
        print("Unknown values in housing :",unknown_values_housing,"\n")
    
    if "loan" in dataset.columns:
        DisplayInfo("Loan Column")
        unknown_values_loan = (dataset["loan"] == "unknown").sum()
        print("Unknown values in loan :",unknown_values_loan,"\n")
    
    if "contact" in dataset.columns:
        DisplayInfo("Contact Column")
        unknown_values_contact = (dataset["contact"] == "unknown").sum()
        print("Unknown values in contact before preprocessing :",unknown_values_contact,"\n")

        mode_contact_yes = dataset[dataset["y"] == "yes"]["contact"].mode().iloc[0]
        mode_contact_no = dataset[dataset["y"] == "no"]["contact"].mode().iloc[0]

        dataset.loc[((dataset["contact"] == "unknown") & (dataset["y"] == "yes")),"contact"] = mode_contact_yes
        dataset.loc[((dataset["contact"] == "unknown") & (dataset["y"] == "no")),"contact"] = mode_contact_no
    
        unknown_values_contact = (dataset["contact"] == "unknown").sum()
        print("Unknown values in contact after preprocessing:",unknown_values_contact,"\n")
    
    if "day" in dataset.columns:
        DisplayInfo("Day Column")
        unknown_values_day = (dataset["day"] == "unknown").sum()
        print("Unknown values in day :",unknown_values_day,"\n")

    if "month" in dataset.columns:
        DisplayInfo("Month Column")
        unknown_values_month = (dataset["month"] == "unknown").sum()
        print("Unknown values in month :",unknown_values_month,"\n")

    if "duration" in dataset.columns:
        DisplayInfo("Duration Column")
        unknown_values_duration = (dataset["duration"] == "unknown").sum()
        print("Unknown values in duration :",unknown_values_duration,"\n")

    if "campaign" in dataset.columns:
        DisplayInfo("Campaign Column")
        unknown_values_campaign = (dataset["campaign"] == "unknown").sum()
        print("Unknown values in campaign :",unknown_values_campaign,"\n")

    if "pdays" in dataset.columns:
        DisplayInfo("pdays Column")
        unknown_values_pdays = (dataset["pdays"] == "unknown").sum()
        print("Unknown values in pdays :",unknown_values_pdays,"\n")

    if "previous" in dataset.columns:
        DisplayInfo("Previous Column")
        unknown_values_previous = (dataset["previous"] == "unknown").sum()
        print("Unknown values in previous :",unknown_values_previous,"\n")

    if "poutcome" in dataset.columns:
        DisplayInfo("poutcome Column")
        unknown_values_poutcome = (dataset["poutcome"] == "unknown").sum()
        print("Unknown values in poutcome :",unknown_values_poutcome,"\n")

        mode_poutcome_yes = dataset[(dataset["y"] == "yes") & (dataset["poutcome"]!= "unknown")]["poutcome"].mode().iloc[0]
        mode_poutcome_no = dataset[(dataset["y"] == "no") & (dataset["poutcome"]!= "unknown")]["poutcome"].mode().iloc[0]

        print(mode_poutcome_yes)
        print(mode_poutcome_no)

        dataset.loc[((dataset["poutcome"] == "unknown") & (dataset["y"] == "yes")),"poutcome"] = mode_poutcome_yes
        dataset.loc[((dataset["poutcome"] == "unknown") & (dataset["y"] == "no")),"poutcome"] = mode_poutcome_no
    
        unknown_values_poutcome = (dataset["poutcome"] == "unknown").sum()
        print("Unknown values in poutcome after preprocessing:",unknown_values_poutcome,"\n")

    X = dataset.drop("y",axis = 1)
    y = dataset["y"]

    print("Seperating dataset in independant and dependant variables :\n")
    print("Independant Variables :\n")
    print(X.head())

    print("Dependant Variables :\n")
    print(y.head())

    print("Independant Variables before encoding:\n")
    print(X.head())

    categoical_col = [
        "job",
        "marital",
        "education",
        "default",
        "housing",
        "loan",
        "contact",
        "month",
        "poutcome"
    ]
    numeric_col = [
        "age",
        "balance",
        "day",
        "duration",
        "campaign",
        "pdays",
        "previous",
    ]

    print(categoical_col == numeric_col)
    preprocessor = ColumnTransformer([
        ('cat',OneHotEncoder(drop='first'),categoical_col),
        ('num',StandardScaler(),numeric_col),
    ])

    X_processed = preprocessor.fit_transform(X)

    print("Independant Variables after encoding:\n")
    print(X_processed[:5])

    return X_processed,y

#----------------------------------------------------------
# Step 3 : Train & Test The Model And also Evaluate
#----------------------------------------------------------
def Model_Training_Testing_Evaluatin(X,Y):
    DisplayInfo("Step 3 : Train the Model")

    X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,stratify=Y,random_state=42)

    print("Dataset splitting in Training and Testing:\n")
    print("Shape of X_train :",X_train.shape)
    print("Shape of X_test:",X_test.shape)
    print("Shape of Y_train :",Y_train.shape)
    print("Shape of Y_test :",Y_test.shape)

    model_dt = DecisionTreeClassifier()
    model_lr = LogisticRegression()
    model_knn = KNeighborsClassifier()

    print("Trained Models are :")

    print("Model 1 :",model_dt)
    print("Model 2 :",model_knn)
    print("Model 3 :",model_lr,"\n")

    model_dt = model_dt.fit(X_train,Y_train)
    model_lr = model_lr.fit(X_train,Y_train)
    model_knn = model_knn.fit(X_train,Y_train)

    result_dt = model_dt.predict(X_test)
    result_lr = model_lr.predict(X_test)
    result_knn = model_knn.predict(X_test)

    DisplayInfo("Step 4 : Models Evaluation")

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

    result_dt = model_dt.predict_proba(X_test)[:,1]
    result_lr = model_lr.predict_proba(X_test)[:,1]
    result_knn = model_knn.predict_proba(X_test)[:,1]

    print("ROC-AUC Score of each model:\n")
    print("ROC-AUC Score of decision tree :",roc_auc_score(Y_test,result_dt))
    print("ROC-AUC Score of Logistic Regression :",roc_auc_score(Y_test,result_lr))
    print("ROC-AUC Score of KNN:",roc_auc_score(Y_test,result_knn))

    fpr,tpr,thresholds = roc_curve(Y_test,result_dt,pos_label='yes')
    roc_auc = auc(fpr,tpr)

    plt.figure()
    plt.plot(fpr,tpr,color = 'darkorange',label = f'ROC Curve (AUC = {roc_auc:.2f})')
    plt.plot([0,1],[0,1],color ='navy',linestyle='--', label='Random Guess Line')
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('ROC Curve Decision Tree')
    plt.legend()
    plt.grid(True)
    plt.show()

    fpr,tpr,thresholds = roc_curve(Y_test,result_lr,pos_label='yes')
    roc_auc = auc(fpr,tpr)

    plt.figure()
    plt.plot(fpr,tpr,color = 'darkorange',label = f'ROC Curve (AUC = {roc_auc:.2f})')
    plt.plot([0,1],[0,1],color ='navy',linestyle='--', label='Random Guess Line')
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('ROC Curve Logistic Regression')
    plt.legend()
    plt.grid(True)
    plt.show()

    fpr,tpr,thresholds = roc_curve(Y_test,result_knn,pos_label='yes')
    roc_auc = auc(fpr,tpr)

    plt.figure()
    plt.plot(fpr,tpr,color = 'darkorange',label = f'ROC Curve (AUC = {roc_auc:.2f})')
    plt.plot([0,1],[0,1],color ='navy',linestyle='--', label='Random Guess Line')
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('ROC Curve KNN')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()