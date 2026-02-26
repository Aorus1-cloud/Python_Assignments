import pandas as pd

def main():
    FileName = "student_performance_ml.csv"

    Dataset = pd.read_csv(FileName)

    print("Number of students :")
    print(Dataset.value_counts().sum())

    FinalResult = Dataset["FinalResult"]

    print("Students Passed :")
    print(len(list(filter(lambda x : x==1,FinalResult))))

    print("Students Failed :")
    print(len(list(filter(lambda x : x == 0,FinalResult))))

if __name__ == "__main__":
    main()