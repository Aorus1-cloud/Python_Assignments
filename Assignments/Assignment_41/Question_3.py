from Question_2 import KNearestNeighbour2Dx
import pandas as pd

def main():
    dataset = pd.DataFrame([
        {'StudyHours':2,'Attendance':60,"Result":"Fail"},
        {'StudyHours':5,'Attendance':80,"Result":"Pass"},
        {'StudyHours':6,'Attendance':85,"Result":"Pass"},
        {'StudyHours':1,'Attendance':50,"Result":"Fail"},
    ])

    model = KNearestNeighbour2Dx(k = 1)

    model.fit(X=dataset[['StudyHours','Attendance']],y=dataset[['Result']])

    X1_test = int(input("Enter the Testing StudyHours :"))
    X2_test = int(input("Enter the Attendance :"))

    result = model.predict(X_test=X1_test,Y_test=X2_test)

    print("The predicted result is :",result)

if __name__ == "__main__":
    main()







