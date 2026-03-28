import pandas as pd

from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

import matplotlib.pyplot as plt
import seaborn as sns 


def DisplayInfo(title):
    border = "="*50
    print(border)
    print(title)
    print(border+"\n")

def main():
    DisplayInfo("Step 1 : Load the dataset")
    dataset = pd.read_csv("student-mat.csv")

    print("Some entries from the dataset :\n",dataset.head(),"\n")

    EDA_student_per(dataset)

def EDA_student_per(dataset):
    DisplayInfo("Step 2 : EDA")

    print("Shape of dataset :",dataset.shape,"\n")
    print("Columns of dataset :\n",dataset.columns,"\n")
    # print(dataset.G1.value_counts())
    print("Null Values :\n",dataset.isnull().sum(),"\n")
    print("NaN values :\n",dataset.isna().sum(),"\n")

    DisplayInfo("Step 3 : Clean the data")

    wanted_columns = [
        "G1",
        "G2",
        "G3",
        "studytime",
        "failures",
        "absences",
    ]

    print("Wanted Columns : \n",wanted_columns,"\n")

    df = dataset[wanted_columns]

    print("Shape of dataset after removing unwanted columns :",df.shape,"\n")

    DisplayInfo("Step 4 : Scaling the dataset ")

    print("Dataset before scaling :\n",df.head(),"\n")

    scaler = StandardScaler()

    df_scaled = scaler.fit_transform(df)

    print("Dataset after scaling :\n",df_scaled[:5],"\n")

    DisplayInfo("Step 5 : Train the model")

    model = KMeans(n_clusters=3)

    result = model.fit_predict(df_scaled)

    df["Clusters"] = result

    print(result)
    print(type(result))

    DisplayInfo("Step 6 : Evaluate the model")
    
    sct = sns.scatterplot(data=df,x='G1',y='G3',markers='*',palette='Dark2',hue='Clusters',s=100)
    sct.plot()
    plt.title("Clusters On basis G1 vs G3")
    plt.xlabel("G1")
    plt.ylabel("G3")
    plt.grid(True)
    plt.legend(title='Clusters')
    plt.show()

    print(model.cluster_centers_)
    print(model.inertia_)
    
    # print(model.labels_)

    # print(df.to_string())
    # Alternative: Pairplot for all numeric columns
    # sns.pairplot(df, hue='Clusters', palette='Dark2')
    # plt.suptitle("Student Performance Clusters", y=1.02)
    # plt.show()

if __name__ == "__main__":
    main()