import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def main():
    FileName = "student_performance_ml.csv"

    Dataset = pd.read_csv(FileName)

    sns.scatterplot(data=Dataset,x="StudyHours",y="PreviousScore",hue="FinalResult")

    plt.show()

  
if __name__ == "__main__":
    main()