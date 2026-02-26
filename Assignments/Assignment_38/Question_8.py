import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def main():
    FileName = "student_performance_ml.csv"

    Dataset = pd.read_csv(FileName)

    sns.boxplot(x=Dataset["Attendance"])

    plt.show()

    '''
    
    No outliers are present here the range is clean.

    '''
  
if __name__ == "__main__":
    main()