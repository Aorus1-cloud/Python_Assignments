import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def main():
    FileName = "student_performance_ml.csv"

    Dataset = pd.read_csv(FileName)


    sns.barplot(data=Dataset,x=Dataset.index,y="SleepHours",hue="FinalResult")
    plt.xlabel("Students")
    plt.show()
    '''
    From the barplot i am getting to know that the students that sleep less than or equal to 6 hours 
    have a higher chance of failing in exam.So,in this sense we can conclude that sleeping more can increase
    the chance of passing.

    '''

if __name__ == "__main__":
    main()