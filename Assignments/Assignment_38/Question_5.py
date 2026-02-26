import pandas as pd

def main():
    Border = "-"*40
    FileName = "student_performance_ml.csv"

    Dataset = pd.read_csv(FileName)

    print(Dataset[["StudyHours","FinalResult"]])


    print(Border+"\n")
    print("StudyHours vs FinalResult\n")
    print("relation btw Passed Students and StudyHours")
    print(Dataset.loc[Dataset["FinalResult"]==1,["StudyHours","FinalResult"]])

    print("relation btw failed Students and StudyHours")
    print(Dataset.loc[Dataset["FinalResult"]==0,["StudyHours","FinalResult"]])

    print(f"Average Study Hours of Passed Students is :{Dataset.loc[Dataset["FinalResult"]==1,"StudyHours"].mean()} hrs")
    print(f"Average Study Hours of Failed Students is :{Dataset.loc[Dataset["FinalResult"]==0,"StudyHours"].mean()} hrs")


    '''
    Analysis:
    According to the data we can clearly see that with higher study hours the chances of student
    passing rate is also high.The average study duration of passed student is more than the 
    avg of the failed which tells that more the study hours more the chance of getting 
    passed.

    ''' 
    print(Border+"\n")
    print("Attendance vs FinalResult\n")

    print("relation btw Passed Students and Attendance")
    print(Dataset.loc[Dataset["FinalResult"]==1,["Attendance","FinalResult"]])

    print("relation btw failed Students and Attendance")
    print(Dataset.loc[Dataset["FinalResult"]==0,["Attendance","FinalResult"]])

    print(f"Average Attendance of Passed Students is :{Dataset.loc[Dataset["FinalResult"]==1,"Attendance"].mean()} days")
    print(f"Average Attendance of Failed Students is :{Dataset.loc[Dataset["FinalResult"]==0,"Attendance"].mean()} days")


    '''
    Analysis:
    According to the data we can clearly see that with higher study hours the chances of student
    passing is also high.The average attendance of a passed student is more than that of failed student 
    which tells us that the more a student attends the more his chances of passing the exam is.

    ''' 

if __name__ == "__main__":
    main()