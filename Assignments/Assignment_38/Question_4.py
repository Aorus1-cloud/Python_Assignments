import pandas as pd

def main():
    FileName = "student_performance_ml.csv"

    Dataset = pd.read_csv(FileName)

    print("The distribution of pass and fail students is :")
    print(Dataset["FinalResult"].value_counts())

    print("Percentage of pass students is :")
    print((Dataset["FinalResult"].value_counts()[1]/Dataset["FinalResult"].value_counts().sum())*100)

    print("Percentage of fail students is :")
    print((Dataset["FinalResult"].value_counts()[0]/Dataset["FinalResult"].value_counts().sum())*100)

    '''
    #? Analysis :
    #* The dataset is not balanced as the data of passed students is 20% more than the fail students
    #* the model is trained on a such a data where passed students are more,so the accuracy might drop 
    #* if the test set have data with features of failed students are similar to passed from trained data.
    '''

if __name__ == "__main__":
    main()