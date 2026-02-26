import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def main():
    Border = "-"*40
    FileName = "student_performance_ml.csv"

    Dataset = pd.read_csv(FileName)

    StudyHours = Dataset["StudyHours"]

    sns.histplot(StudyHours)

    plt.show()

    '''
    From the histogram i understand:-

    1) The Study Hour Ranges from 0 to 8 hours.
    2) The Maximum number of student are in range of 1-2 hrs and 
        6-7hrs
    3) The lowest number of students is in range 2-4 hrs
    4) The average student are in range 4-6hrs and 7-8hrs 
    
    '''
if __name__ == "__main__":
    main()