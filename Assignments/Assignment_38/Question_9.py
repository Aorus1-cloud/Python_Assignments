import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def main():
    FileName = "student_performance_ml.csv"

    Dataset = pd.read_csv(FileName)

    mean = Dataset["AssignmentsCompleted"].mean()

    sns.barplot(data=Dataset,x=Dataset.index,y="AssignmentsCompleted",hue="FinalResult")
    plt.axhline(y=mean,linestyle="--",)
    plt.xlabel("Students")
    plt.show()
    '''
    From the barplot i am getting to know that the students that have completed assignments 
    more than or equal to 5 have a higher chance of passing.

    '''

if __name__ == "__main__":
    main()