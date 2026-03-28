import pandas as pd

from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import VotingClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,classification_report,confusion_matrix,roc_auc_score
from sklearn.pipeline import Pipeline

import matplotlib.pyplot as plt
import seaborn as sns

def DisplayInfo(title):
    border = "="*50
    print(border)
    print(title)
    print(border+"\n")

def NewsDatasetCombined():
    fake_csv = pd.read_csv("Fake.csv")
    true_csv = pd.read_csv("True.csv")

    fake_csv["label"] = 0
    true_csv["label"] = 1
    
    dataset = pd.concat([fake_csv,true_csv],ignore_index=True)

    return dataset

def EDA_Cleaning_news(dataset):
    DisplayInfo("Step 2 : EDA")
    print("Shape of dataset :",dataset.shape,"\n")
    print("Columns Name:\n",dataset.columns,"\n")
    print("Null values :\n",dataset.isnull().sum(),"\n")
    print("NaN values :\n",dataset.isna().sum(),"\n")

    print("Label Distribution:\n")
    sns.countplot(data=dataset,x="label",fill=True,hue="label")
    plt.legend()
    plt.title("Label Distribution of dataset")
    plt.show()

    DisplayInfo("Step 3 : Cleaning The Dataset")
    print("The columns subject and date is not useful therefore we will remove it.")
    print("Shape before column removal :",dataset.shape,"\n")
    print("Columns before removal :\n",dataset.columns,"\n")

    dataset = dataset.drop(columns = ["subject","date"])

    print("Shape after column removal :",dataset.shape,"\n")
    print("Columns after removal :\n",dataset.columns,"\n")

    DisplayInfo("Step 4 : Splitting the dataset into Independant And Dependant Variables:\n")

    print("Dataset before splitting:\n",dataset.head(),"\n")
    print("Shape of dataset before splitting :",dataset.shape,"\n")

    X = dataset.drop("label",axis=1)
    Y = dataset["label"]

    print("Dataset after splitting :\n")
    print("Shape of X :",X.shape)
    print("Shape of Y :",Y.shape,"\n")

    DisplayInfo("Step 5 : Encoding the Indepedant Variables")
    print("Independant variables before encoding :\n")
    print(X.head(),"\n")

    encoder = TfidfVectorizer(max_features=5000,stop_words='english')

    pipeline = Pipeline([
        ('tfidf_vectorizer',TfidfVectorizer()),
        ('decision_tree',DecisionTreeClassifier()),
        ('Logistic',LogisticRegression())
    ])

    X_train,X_test,Y_train,Y_test = train_test_split(
        X,
        Y,
        random_state=42,
        stratify=Y,
        test_size=0.2,
    )

    pipeline.fit(X_train,Y_train)

    result = pipeline.predict(X_test)

    print(classification_report(Y_test,result))

    # X_combined = X['title'].fillna('')+' '+X['text'].fillna('')

    # print("Combined columns of dataset is as :\n",X_combined.head(),"\n")

    # X_encoded = encoder.fit_transform(X_combined)

    # print("Independant variables after encoding:\n")
    # print(X_encoded.toarray(),"\n")

    # print(encoder.vocabulary_)
    # feature_names = encoder.get_feature_names_out()

    # for word in feature_names:
    #     index = encoder.vocabulary_.get(word)
    #     print(f"{word} : {encoder.idf_[index]}")


     
def main():
    DisplayInfo("Step 1 : Load the dataset")

    dataset = NewsDatasetCombined()

    print(dataset.head())
    
    EDA_Cleaning_news(dataset)
    
if __name__ == "__main__":
    main()