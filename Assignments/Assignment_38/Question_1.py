import pandas as pd

def main():
    FileName = "student_performance_ml.csv"

    Dataset = pd.read_csv(FileName)

    print("Step 1 : Dataset Loading...")

    print("First 5 Entries :")
    print(Dataset.head())

    print("\nLast 5 Entries :")
    print(Dataset.tail())

    print("\nNumber of Rows and Columns :")
    print(Dataset.shape)

    print("\nColumn Names :")
    print(list(Dataset.columns))

    print("\nDatatype of each column is :")
    print(Dataset.dtypes)

if __name__ == "__main__":
    main()