import pandas as pd

from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import VotingClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report,confusion_matrix,accuracy_score,ConfusionMatrixDisplay
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer

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

    column_transformer = ColumnTransformer(
    [   
        ('text_column',encoder,"text"),
        ('title_column',encoder,"title"),
    ],
    remainder='passthrough'  # Keeps the non-text data as it is.
    )

    pipeline1 = Pipeline([
        ('tfidf_vectorizer',column_transformer),
        ('decision_tree',DecisionTreeClassifier()),
    ])

    pipeline2 = Pipeline([
        ('tfidf_vectorizer',column_transformer),
        ('Logistic',LogisticRegression()),
    ])


    X_train,X_test,Y_train,Y_test = train_test_split(
        X,
        Y,
        random_state=42,
        stratify=Y,
        test_size=0.2,
    )
    print("Dataset After Encoding :\n")
    pipeline1.fit(X_train,Y_train)
    pipeline2.fit(X_train,Y_train)

    encoded_data = pipeline1.named_steps['tfidf_vectorizer'].transform(X_train)
    print(encoded_data)
    print("Encoded Training dataset shape is :",encoded_data.shape,"\n")
    print("First 5 rows and 20 columns of the encoded data :\n",encoded_data[:5,:20],"\n")

    DisplayInfo("Step 6 : Train the Model")
    print("Model Decision Tree :",pipeline1,"\n")
    print("Model Logistic Regression :",pipeline2,"\n")

    DisplayInfo("Step 7 : Test the model")

    hard_voting = VotingClassifier(estimators=[
        ('dt',pipeline1),
        ('lr',pipeline2),
    ],
    voting='hard'
    )

    soft_voting = VotingClassifier(estimators=[
        ('dt',pipeline1),
        ('lr',pipeline2),
    ],
    voting='soft'
    )
    hard_voting.fit(X_train,Y_train)
    soft_voting.fit(X_train,Y_train)

    hard_result = hard_voting.predict(X_test)
    soft_result = soft_voting.predict(X_test)
    
    print("Model Testing Completed\n")
    print("Hard Voting Result :\n",hard_result[:5],"\n")
    print("Soft Voting Result :\n",soft_result[:5],"\n")
    
    DisplayInfo("Step 8 : Evaluate the model")
    print("Accuracies:\n")
    print("Accuracy of Hard Voting is :",accuracy_score(Y_test,hard_result),"\n")
    print("Accuracy of Soft Voting is :",accuracy_score(Y_test,soft_result),"\n")

    print("Confusion Matrixs :\n")
    cm_hard = confusion_matrix(Y_test,hard_result)
    cm_soft = confusion_matrix(Y_test,soft_result)

    cmp = ConfusionMatrixDisplay(confusion_matrix=cm_hard)
    cmp.plot()
    plt.title("Confustion Matrix Hard Voting")
    plt.show()

    cmp = ConfusionMatrixDisplay(confusion_matrix=cm_soft)
    cmp.plot()
    plt.title("Confusion Matrix Soft Voting")
    plt.show()

    print("Classification Report of Hard Voting:\n",classification_report(Y_test,hard_result),"\n")
    print("Classification Report of Soft Voting:\n",classification_report(Y_test,soft_result),"\n")

    # print(pipeline1[:-1].get_feature_names_out())
    # print(pipeline2[:-1].get_feature_names_out())

    # result1 = pipeline1.predict(sample_que)
    # result2 = pipeline2.predict(sample_que)

    # print(result1)
    # print(result2)

    # print(sample_ans)
    
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