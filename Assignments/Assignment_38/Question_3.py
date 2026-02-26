import pandas as pd

def main():
    FileName = "student_performance_ml.csv"

    Dataset = pd.read_csv(FileName)

    print("The average of the Study Hours is :")
    print(Dataset["StudyHours"].mean(),end=" Hours")

    print("\nThe average of attendance is :")
    print(Dataset["Attendance"].mean(),end=" %")

    print("\nMaximum of the previous score is :")
    print(Dataset["PreviousScore"].max(),end=" Marks")

    print("\nMinimum of the sleep hours is :")
    print(Dataset["SleepHours"].min(),end=" hrs\n")

if __name__ == "__main__":
    main() 